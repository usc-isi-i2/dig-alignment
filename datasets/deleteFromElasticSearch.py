import sys
from elasticsearch import Elasticsearch

queryFile = None
esServer = None
index = None


def parse_args():
    global queryFile
    global esServer
    global index

    for arg_idx, arg in enumerate(sys.argv):
        if arg == "--query":
            queryFile = sys.argv[arg_idx+1]
            continue
        if arg == "--server":
            esServer = sys.argv[arg_idx+1]
            continue
        if arg == "--index":
            index = sys.argv[arg_idx+1]
            continue

def die():
    print "Please input the required parameters"
    print "Usage: deleteFromElasticSearch.py --query <Name of query file> --server <Server with port and auth info> --index <index name>"
    exit(1)

parse_args()
if esServer is None or queryFile is None or index is None:
    die()

queryBody = None
with open(queryFile, 'r') as queryFile_handle:
    queryBody = queryFile_handle.read()

print "Connnect:" + esServer
es = Elasticsearch([esServer])
#print es.info()
print "Delete from index:" + index + ", query:" + queryBody
es.delete_by_query(index, body=queryBody)
print "Done deleting from index"