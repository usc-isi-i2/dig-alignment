from pyld import jsonld
import json


with open('temp.json') as data_file:
	with open('context.json') as context_file:
		doc = json.load(data_file)
		context = json.load(context_file)
		compacted = jsonld.compact(doc, context)
		compacted['@graph'] = sorted(compacted['@graph'], key=lambda x: x['@id'])
		print(json.dumps(compacted, sort_keys=True, indent=2))