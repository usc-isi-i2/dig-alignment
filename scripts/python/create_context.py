import json
import urllib
import sys
from httplib import HTTPConnection
from pyld import jsonld


class Entity(object):
    """Represents and entity in the ontology, created from its expanded
    JSON-LD representation.

    Attributes:
        jsonld: the expanded JSON-LD representation of the entity.
    """

    def __init__(self, expanded_jsonld):
        """Creates an Entity from its expanded JSON-LD representation."""
        self.jsonld = expanded_jsonld

    @property
    def is_class(self):
        """True if the entity represents a class."""
        return ('@type' in self.jsonld
                and ('http://www.w3.org/2002/07/owl#Class'
                     in self.jsonld['@type']
                     or 'http://www.w3.org/2000/01/rdf-schema#Class'
                     in self.jsonld['@type']))

    @property
    def is_property(self):
        """True if the entity represents a property."""

        return '@type' in self.jsonld \
            and ('http://www.w3.org/2002/07/owl#DatatypeProperty'
                 in self.jsonld['@type']
                 or 'http://www.w3.org/2002/07/owl#ObjectProperty'
                 in self.jsonld['@type']
                 or 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property'
                 in self.jsonld['@type'])

    @property
    def is_object_property(self):
        """True of the entity represents an object property."""
        return '@type' in self.jsonld \
               and "http://www.w3.org/2002/07/owl#ObjectProperty" \
                   in self.jsonld['@type']

    @property
    def has_set_container(self):
        """True, when the entity represents a property, and has the properties that warrant
            generation of @container: @set"""
        return 'http://schema.dig.isi.edu/ontology/jsonLD_container' \
               in self.jsonld \
               and {'@id': 'http://schema.dig.isi.edu/ontology/JSONLD_Set'} \
            in self.jsonld['http://schema.dig.isi.edu/ontology/jsonLD_container'
                   ]

    @property
    def is_has_type(self):
        """Special case of memex:hasType, which maps to @index"""
        return 'http://schema.dig.isi.edu/ontology/hasType' == self.jsonld['@id']

    @property
    def shortcut(self):
        """Return a tuple of the shortcut name and its expansion."""
        key = self.jsonld['@id']
        tail = key.split('/')[-1]
        return tail.split('#')[-1], key

    @property
    def context(self):
        """Return the context object to use with this entity"""
        (name, expansion) = self.shortcut
        if self.is_class:
            return name, {"@type": "@id", "@id": expansion}
        elif self.is_has_type:
            return name, {"@id": expansion, "@container": '@index'}
        elif self.is_property:
            c = {"@id": expansion}
            if self.is_object_property:
                c['@type'] = '@id'
            if self.has_set_container:
                c['@container'] = '@set'
            return name, c
        else:
            return None, None


class Ontology(object):
    """The Ontology objec supports format conversions and generation
    of the context file.

    Attributes:
        triples: text of N3 rdf.
        context: the context for JSON-LD ontologies.
    """

    def __init__(self):
        """Creates an empty ontology."""
        self.triples = ""
        with open('context.json') as context_file:
            self.context = json.load(context_file)

    def load_ttl(self, ttl_file):
        """Load a .ttl file.
        :param ttl_file: the name of a file containing an ontology in ttl format.
        """
        self.triples += "\n"
        with open(ttl_file) as ttl_data:
            self.triples += ttl_data.read()

    @property
    def compacted_jsonld(self):
        """Return the ontology in compacted JSON-LD format as an object."""

        content = {'content': self.triples}

        conn = HTTPConnection('rdf-translator.appspot.com')
        # conn.set_debuglevel(1)
        conn.request('POST', '/convert/n3/json-ld/content', urllib.urlencode(content))
        response = conn.getresponse()
        assert response.status == 200

        expanded = json.load(response)
        compacted = jsonld.compact(expanded, self.context)
        # print json.dumps(compacted,indent=4)
        compacted['@graph'] = sorted(compacted['@graph'], key=lambda x: x['@id'])
        return compacted

    @property
    def expanded_jsonld(self):
        """Return the ontology in expanded JSON-LD format as an object."""
        return jsonld.expand(self.compacted_jsonld)

    @property
    def ontology_context(self):
        """Construct a context file for the ontology"""
        expanded = jsonld.expand(self.compacted_jsonld)
        body = {"a": "@type", "uri": "@id"}
        ids_with_duplicate_shortcuts = []
        for x in expanded:
            entity = Entity(x)
            (name, entry) = entity.context
            if name is None:
                continue

            if name in body:
                ids_with_duplicate_shortcuts.append(body[name]['@id'])
                ids_with_duplicate_shortcuts.append(entry['@id'])

            body[name] = entry
        return {'@context': body}, ids_with_duplicate_shortcuts


def main(argv):
    """Creates a consolidated ontology and context for the given ttl files.
    :param argv: list of ttl files
    """
    ont = Ontology()
    for file_name in argv[1:]:
        ont.load_ttl(file_name)

    with open('all-ontology.json', 'w') as ontology_file:
        ontology_file.write(json.dumps(ont.compacted_jsonld, indent=4, sort_keys=True))

    context, duplicates = ont.ontology_context
    with open('karma-context.json', 'w') as context_file:
        context_file.write(json.dumps(context, indent=4, sort_keys=True))
    if len(duplicates) > 0:
        sys.stderr.write('List of URIs that would create duplicate context entries:\n')
        for u in duplicates:
            sys.stderr.write("- ")
            sys.stderr.write(u)
            sys.stderr.write("\n")

if __name__ == "__main__":
    main(sys.argv)

# o = Ontology()
# o.load_ttl('../memex-ontology.ttl')
# # o.load_ttl('../ext-bib.ttl')
# # print(json.dumps(x.expanded_jsonld, indent=2))
# a, b = o.ontology_context
# print(json.dumps(a, indent=2, sort_keys=True))
