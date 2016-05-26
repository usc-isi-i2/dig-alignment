import json
import pprint
import sys
import urllib2
from httplib import HTTPConnection


class MappingGenerator(object):
    """Create a mapping file for a frame."""

    def __init__(self, frame, ontology):
        """
        Initialize the mapping generator for a single frame.
        :param frame: a single JSON-LD frame, with @explicit for all objects.
        :type frame: JSON object as a dictionary
        :param ontology: an instance of class Ontology
        """
        self.frame = frame
        self.ontology = ontology

    @staticmethod
    def get_frame(url):
        """
        Fetch a frame from the web, typically from GitHub.
        :param url: to the frame in JSON format.
        :return: parsed frame as a JSON object.
        :rtype: JSON dictionary
        """
        f = urllib2.urlopen(url).read()
        return json.loads(f)

    not_analyzed_keys = [
        "a",
        "uri"
    ]

    def is_not_analyzed(self, key):
        """
        Test whether a property identified by key is tagged as not_analyzed.
        :param key: a property, represented as an attribute in the frame.
        :type key: string.
        :return: true if the property should be not_analyzed.
        """
        return key in self.not_analyzed_keys or self.ontology.is_not_analyzed(key)

    def create_mapping_helper(self, mapping, frame):
        """
        Recursive function to create the mapping for a frame.
        :param mapping: the mapping object being built,
            the properties in the frame will be added to this mapping object.
        :type mapping: JSON object
        :param frame: the top level attributes of the frame will be added to the mapping.
        :type frame: JSON object
        :return: the updated mapping object.
        """
        keys = frame.keys()

        if keys:
            assert '@explicit' in keys and frame['@explicit']
            for key in keys:
                if key[0] != '@':
                    self.add_key(mapping, key, frame[key])
        return mapping

    def add_key(self, mapping, key, value):
        """
        Add the key to the mapping, provided that the key represents a property.
        :param mapping: the mapping being created.
        :type mapping: JSON object.
        :param key: an attribute from the frame.
        :type key: string
        :param value: the value of the property in the frame.
        :type value: a JSON object, either an empty object, or a recursive frame.
        :return: nothing, updates the mapping object.
        """
        if value:
            # if the value is not empty, it represents a nested frame.
            new_entry = {
                "properties": {}
            }
            mapping[key] = new_entry
            self.create_mapping_helper(new_entry['properties'], value)
        else:
            # if the value is empty, add the property to the mapping,
            # processing all the directives contained in the ontology.
            new_entry = {
                "type": "string"
            }
            if self.is_not_analyzed(key):
                new_entry['index'] = 'not_analyzed'
            if self.ontology.is_raw_field(key):
                new_entry['fields'] = {
                    'raw': {
                        'type': 'string',
                        'index': 'not_analyzed'
                    }
                }
            if self.ontology.is_type_date(key):
                new_entry['type'] = 'date'
            if self.ontology.is_format_date_optional_time(key):
                new_entry['format'] = 'dateOptionalTime'
            mapping[key] = new_entry

    def create_mapping(self):
        """
        Convenience function to create the mapping for the frame in self.frame.
        :return: the mapping for self.frame.
        :rtype: JSON object.
        """
        return self.create_mapping_helper({}, self.frame)

class Ontology(object):
    """
    Represents the entries in the ontology as a dictionary where the keys
    are the URIs of the ontology items (classes, properties or individuals).
    If the prefix is memex: or schema: remove the prefix and use the bare name
    as the key. This means that bare names must be distinct in the schema and memex
    namespaces.
    """

    def __init__(self, jsonld):
        """
        Initialize the ontology from the JSON-LD representation.
        :param jsonld: the ontology
        :type jsonld: JSON object
        :return: nothing
        """
        self.ontolgy = {}
        for item in jsonld['@graph']:
            id = item['@id']
            if id.startswith('memex:'):
                id = id.replace('memex:', '')
            elif id.startswith('schema:'):
                id = id.replace('schema:', '')
            self.ontolgy[id] = item;

    def directives(self, key):
        """
        Return an array of all the ElasticSearch directives for an item in the ontology.
        :param key: name of a property or item in the ontology if the key is in the schema or
        memex namespaces, otherwise the key is the URI of the item.
        :type key: string
        :return: array of directives, empty array if there are no directives.
        :rtype: array
        """
        if key in ['a', 'uri']:
            return []
        item = self.ontolgy[key].get('memex:es_directive')
        if item is None:
            return []
        else:
            return item

    def is_not_analyzed(self, key):
        return 'memex:ES_not_analyzed' in self.directives(key)

    def is_raw_field(self, key):
        return 'memex:ES_include_raw_field' in self.directives(key)

    def is_type_date(self, key):
        return 'memex:ES_type_date' in self.directives(key)

    def is_format_date_optional_time(self, key):
        return 'memex:ES_format_date_optional_time' in self.directives(key)

dig_settings = {
    "index": {
        "number_of_replicas": "0",
        "number_of_shards": "5"
    },
    "analysis": {
        "analyzer": {
            "partial_phone_analyzer": {
                "tokenizer": "keyword",
                "char_filter": [
                    "digits_only"
                ],
                "filter": [
                    "ngram_3_10"
                ]
            },
            "exact_phone_analyzer": {
                "tokenizer": "keyword",
                "char_filter": [
                    "digits_only"
                ]
            },
            "exact_email_analyzer": {
                "tokenizer": "uax_url_email",
                "filter": [
                    "email_splitting_filter_keep_original",
                    "lowercase",
                    "unique"
                ]
            },
            "partial_email_analyzer": {
                "tokenizer": "uax_url_email",
                "filter": [
                    "ngram_5_8"
                ]
            }
        },
        "filter": {
            "filter_stemmer": {
                "type": "porter_stem",
                "language": "English"
            },
            "shingle_filter_2_4": {
                "type": "shingle",
                "min_shingle_size": 2,
                "max_shingle_size": 4,
                "output_unigrams": False
            },
            "shingle_filter_4": {
                "type": "shingle",
                "min_shingle_size": 4,
                "max_shingle_size": 4,
                "output_unigrams": False
            },
            "email_splitting_filter_keep_original": {
                "type": "pattern_capture",
                "preserve_original": 1,
                "patterns": [
                    "(.+)@",
                    "@(.+)"
                ]
            },
            "email_splitting_filter": {
                "type": "pattern_capture",
                "preserve_original": 0,
                "patterns": [
                    "(.+)@",
                    "@(.+)"
                ]
            },
            "ngram_3_10": {
                "type": "nGram",
                "min_gram": 3,
                "max_gram": 10
            },
            "ngram_5_8": {
                "type": "nGram",
                "min_gram": 5,
                "max_gram": 8
            }
        },
        "char_filter": {
            "digits_only": {
                "type": "pattern_replace",
                "pattern": "(\\D)",
                "replacement": ""
            }
        }
    }
}

def main(argv):
    """

    :param argv:
    :type argv:
    :return:
    :rtype:
    """

    pp = pprint.PrettyPrinter(indent=4)

    base_url = "https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/versions/3.0/frames/"
    frame_mapping = {
        "offer": "offer.json",
        "webpage": "webpage.json",
        "email": "email.json",
        "phone": "phone.json",
        "image": "image.json",
        "adultservice": "adultservice.json",
        "seller": "seller.json"
    }

    with open('all-ontology.json') as ontology_file:
        ontology = json.load(ontology_file)
        o = Ontology(ontology)

    mapping = {}
    for key in frame_mapping.keys():
        frame = MappingGenerator.get_frame(
            base_url + frame_mapping[key])
        mapping[key] = {
            'properties': MappingGenerator(frame, o).create_mapping()
        }

    full_mapping = {
        "mappings": mapping,
        "settings": dig_settings
    }
    with open('mapping.json', 'w') as mapping_file:
        mapping_file.write(json.dumps(full_mapping, indent=4, sort_keys=True))

if __name__ == "__main__":
    main(sys.argv)
