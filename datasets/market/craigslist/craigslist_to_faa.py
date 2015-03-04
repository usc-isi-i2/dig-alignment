#!/usr/bin/python

import csv
import StringIO

def readManually():
    rows = {}
    with open('manually_fetched.dat', 'rb') as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            k = row[3]
            rows[k] = row
    return rows

def interpretField(field):
    stream = StringIO.StringIO(field[1:-1])
    reader = csv.reader(stream, delimiter=',')
    rows = [row for row in reader]
    row = rows[0]
    return row

def interpretField(field):
    return eval(field)

def mergeAll():
    manually = readManually()
    result = []
    with open('craigslist_to_faa.dat','r') as f:
        lines = f.readlines()
    done = False
    for line in lines:
        fields = line.split('\t')
        k = fields[4].rstrip('\n')
        if k.startswith('*'):
            new = manually[k]
            print "tail is %s" % [new[8:]]
            line = fields[0:3] + [-1] + new[0:3] + [new[4]] + new[5:8] + [new[8]] + new[10:]
            done = True
        else:
            interpreted = interpretField(k)
            line = fields[0:3] + interpreted[0:5] + interpreted[6:9] + interpreted[11:] + ["datahub.io/dataset/open-flights"]
        result.append(line)
        if done:
            break
    return result

m=mergeAll()
print m[0]
print
print m[30]
print
print zip(m[0],m[30])
