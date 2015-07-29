#!/usr/bin/env python
import re

def extract_patent(patent, extract_re):
    if "_source" in patent:
        source = patent["_source"]
        if "crawl_data" in source:
            crawl_data = source["crawl_data"]
            if "full-text" in crawl_data:
                text = crawl_data["full-text"]
                isPatent = False
                if text.find("patent") != -1 or text.find("Patent") != -1 or text.find("PATENT") != -1:
                    isPatent = True
                crawl_data["isPatent"] = isPatent
                if isPatent is True:
                    start = 0
                    numbers = []
                    while True:
                        x = extract_re.search(text, start)
                        if x:
                            num = x.group().strip()
                            if num.startswith(",") is False:
                                numbers.append(num)
                            start = x.end() + 1
                        else:
                            break
                    crawl_data["mentions-patents"] = numbers
    return patent

if __name__ == "__main__":
    from pyspark import SparkContext
    import json
    import sys

    sc = SparkContext(appName="CourtListener")
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    patentno_re = re.compile("[^\$][D5-9]?,?[0-9]{3},?[0-9]{3}")

    rdd = sc.textFile(inputFilename)\
            .filter(lambda x: x.find("https://www.courtlistener.com") == 0)\
            .map(lambda x: x.split("\t", 2))\
            .mapValues(lambda x: json.loads(x))\
            .mapValues(lambda x: extract_patent(x, patentno_re))\
            .mapValues(lambda x: json.dumps(x))
    rdd.saveAsSequenceFile(outputFilename)
