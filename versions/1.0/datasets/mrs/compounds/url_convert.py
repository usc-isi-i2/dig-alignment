import sys
import fileinput

inputFile = sys.argv[1]
mappings = sys.argv[2]

def cleanuri(uri):
    if uri.startswith("\""):
        uri = uri[1:]
    if uri.endswith("\""):
        uri = uri[0:len(uri)-1]
    return uri

fileData = None
file = open(inputFile, 'r')
fileData = file.read()
file.close()

i = 1
for mappingline in open(mappings):
    parts = mappingline.split(",")
    uri = cleanuri(parts[0].strip())
    old_uri = cleanuri(parts[1].strip())
    print str(i) + " " + old_uri + "->" + uri
    fileData = fileData.replace(old_uri, uri)
    i = i+1

file=open(inputFile, 'w')
file.write(fileData)
file.close()
