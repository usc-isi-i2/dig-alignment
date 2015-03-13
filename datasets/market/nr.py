#!/usr/bin/python

import sys
from util import positionIf, echo
from collections import Counter

def isGenderMarker(t):
    return t in ["female", "woman", "male", "shemale", "tstvtg", "man", "couple", "female1"]

def isRaceEthnicMarker(t):
    return t in ["white", "black", "asian", "latin", "latino", "latina", "hispanic", "indian", "other", "european", "oriental", "russian", "mixed",""]

def isCompoundRaceEthnicMarker(t):
    return t in [["middle","eastern"]]

TEST=[

"""http://www.naughtyreviews.com/escorts/heather-of-alabama-birmingham-white-female""",
"""http://www.naughtyreviews.com/escorts/brianna-birmingham-white-female-0""",
"""http://www.naughtyreviews.com/escorts/daphne-birmingham-white-female""",
"""http://www.naughtyreviews.com/escorts/kianna-bradley-huntsville-asian-female""",
"""http://www.naughtyreviews.com/escorts/suzzie-little-rock-asian-female""",
"""http://www.naughtyreviews.com/escorts/meko-flagstaff-asian-female""",
"""http://www.naughtyreviews.com/escorts/the-scarlet-woman-calgary-white-female""",
"""http://www.naughtyreviews.com/escorts/the-scarlet-woman-vancouver-white-female""",
"""http://www.naughtyreviews.com/escorts/black-diamond-woman-jackson-black-female""",
"""http://www.naughtyreviews.com/escorts/vanessa-houston-latin-shemale""",
"""http://www.naughtyreviews.com/escorts/vanessa-houston-latin-shemale""",
"""http://www.naughtyreviews.com/companions/juliette-jakarta-asian-shemale""",
"""http://www.naughtyreviews.com/companions/chanel-dayton-mixed-female""",
"""http://www.naughtyreviews.com/escort-agencies/my-exotic-escape-cleveland""",
"""http://www.naughtyreviews.com/escort-agencies/bogus-agency-new-orleans-0""",
"""http://www.naughtyreviews.com/massage-parlors/renton-spadivine-temple-seattle""",
"""http://www.naughtyreviews.com/escorts/lebanese-middle-eastern-beauty-san-diego-middle-eastern-female"""
]

LOC1 = Counter()
LOC2 = Counter()
LOC3 = Counter()
LOC = [None,LOC1, LOC2, LOC3]

GENDER = Counter()
RACEETHNIC = Counter()

def process(url):
    bits = url.split('/')
    service = bits[3]
    if service in ["escorts", "companions"]:
        line = bits[-1]
        return processEscort(line)
    elif service in ["escort-agencies"]:
        line = bits[-1]
        return processAgency(line)
    elif service in ["na"]:
        print "N",
        line = bits[-1]
        return processEscort(line)
    elif service in ["massage-parlors"]:
        print "M",
        line = bits[-1]
        return processMassage(line)
    else:
        print "Didn't recognize service type %s" % service
        return 0


def recordLocations(fields):
    # print "Location fields: let's look at %s" % ([fields])
    startJ = -min(len(fields),3)
    endJ = -1
    cands = 0
    # print "cands from [%s:%s] to [%s:%s]" % (startJ, "", endJ, "")
    for j in xrange(startJ,0):
        try:
            sub = fields[j:]
            width = len(sub)
            # print "  %s:%s cand %s of width %s" % (j, "", sub, width)
        except Exception as e:
            print "Failed [[%s]]" % e
        #print "Width = %d" % width
        #print "LOC for that is %s" % (LOC[width])
        #print "index by %s" % [tuple(sub)]
        LOC[width][tuple(sub)] += 1
        cands += 1
    return cands

def processMassage(line):
    terms = line.split('-')[1:]
    return recordLocations(terms[-3:])

def processAgency(line):
    terms = line.split('-')[1:]
    try:
        i = int(terms[-1])
        terms.pop()
    except ValueError as e:
        pass
    return recordLocations(terms[-3:])

def trimNumericSuffix(terms):
    suffix = None
    try:
        i = int(terms[-1])
        suffix = terms[-1]
        terms.pop()
    except ValueError as e:
        pass
    return (suffix, terms)

def trimGenderMarker(terms):
    marker = None
    try:
        if isGenderMarker(terms[-1]):
            marker = terms[-1]
            terms.pop()
    except ValueError as e:
        pass
    return (marker, terms)
    
def trimRaceEthnicMarker(terms):
    marker = None
    try:
        if isCompoundRaceEthnicMarker(terms[-2:]):
            marker = "-".join(terms[-2:])
            terms.pop()
            terms.pop()
        elif isRaceEthnicMarker(terms[-1]):
            marker = terms[-1]
            terms.pop()
    except ValueError as e:
        pass
    return (marker, terms)

def processEscort(line):
    cands=0
    terms = line.split('-')[1:]
    terms.reverse()
    # print terms
    gpos = positionIf(isGenderMarker, terms)
    try:
        GENDER[terms[gpos]] +=1
    except TypeError as e:
        pass
    location = None
    try:
        rpos = positionIf(isRaceEthnicMarker, terms, start=gpos)
        try:
            RACEETHNIC[terms[rpos]] + 1
        except TypeError as e:
            pass
        # print "g %s, re %s, loc %s" % (terms[gpos], terms[rpos], terms[rpos+1:rpos+2])
        fields = terms[rpos+1:]
        fields.reverse()
        cands = recordLocations(fields)
        
    except Exception as e:
        print >> sys.stderr, "Give up on %r: [%s]" % (line, e)
        return 0
    return cands

def processEscort(line):
    cands = 0
    try:
        terms = line.split('-')[1:]
        (suffix, terms) = trimNumericSuffix(terms)
        (gender, terms) = trimGenderMarker(terms)
        if gender:
            GENDER[gender] += 1
        (raceEthnic, terms) = trimRaceEthnicMarker(terms)
        if raceEthnic:
            RACEETHNIC[raceEthnic] += 1
        cands = recordLocations(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on escort %r: [%s]" % (line, e)
        return 0
    return cands

def processAgency(line):
    cands = 0
    try:
        terms = line.split('-')[1:]
        (suffix, terms) = trimNumericSuffix(terms)
        cands = recordLocations(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on agency %r: [%s]" % (line, e)
        return 0
    return cands

def main():
    for line in TEST:
        print line, process(line)

def mainlines(lines, limit=100):
    budget=limit
    total = 0
    failed = []
    for line in lines:
        if 'http://' in line:
            line = line.strip('| \n')
            cands = process(line)
            total += cands
            if cands == 0:
                failed.append(line)
            limit -= 1
            if limit <= 0:
                break
    return ["limit", budget, "total", total, "failed", failed]

def line2():
    process(TEST[1])

def mainfile(limit=100):
    with open('nr.txt', 'r') as f:
        return mainlines(f, limit=limit)

def maintest():
    def iter():
        for line in TEST:
            print line
            yield line
    return mainlines(iter())

def dumpFile(c, pathname):
    l = [t for t in c.iteritems()]
    l.sort(key=lambda x: x[1], reverse=True)
    with open(pathname, 'w') as f:
        for t in l:
            print >> f, "%s\t%s" % (t[1], "\t".join(t[0]))

def dumpAll():
    dumpFile(LOC1, "loc1.tsv")
    dumpFile(LOC2, "loc2.tsv")
    dumpFile(LOC3, "loc3.tsv")



# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(mainfile(limit=700000))
