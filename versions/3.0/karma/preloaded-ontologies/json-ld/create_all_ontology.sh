### Merge the ontologies and produce a single JSON=LD file for all the ontologies.
cat ../ext-bib.ttl ../memex-ontology.ttl ../schema.ttl > temp.ttl
curl --data-urlencode content@temp.ttl http://rdf-translator.appspot.com/convert/n3/json-ld/content > temp.json
python apply-context.py > all-ontology.json
rm temp.ttl temp.json