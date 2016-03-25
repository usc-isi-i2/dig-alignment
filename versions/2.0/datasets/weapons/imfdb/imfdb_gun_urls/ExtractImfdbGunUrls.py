import sys
import codecs
import json
import os
from extraction.Landmark import RuleSet
from extraction import Landmark

def main(argv=None):
    baseUrl = 'http://www.imfdb.org'
    rules_file = '/Users/bamana/Documents/InferLink/workspace/memex/memexpython/input/_rules/imfdb_gun_urls_rules.txt'
    imfdb_gun_urls_dir = '/Users/bamana/Documents/InferLink/workspace/memex/memexpython/input/imfdb_gun_urls'
    urls = []
    
    with codecs.open(rules_file, "r", "utf-8") as myfile:
        json_str = myfile.read().encode('utf-8')
    json_object = json.loads(json_str)
    rules = RuleSet(json_object)
    
    for subdir, dirs, files in os.walk(imfdb_gun_urls_dir):
        for the_file in files:
            if the_file.startswith('.'):
                continue
            
            with codecs.open(os.path.join(subdir, the_file), "r", "utf-8") as myfile:
                page_str = myfile.read().encode('utf-8')
                
            result = rules.extract(page_str)
            result = Landmark.flattenResult(result)
            
            for extracted_url in result['urls']:
                urls.append(baseUrl + extracted_url)
                
            print len(urls)
                
    
    for url in urls:
        print url

    
if __name__ == '__main__':
    sys.exit(main())