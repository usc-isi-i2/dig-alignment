import csv

market_id_to_market_info = {}

with open('market_id.csv', 'r') as csvfile:
    rdr = csv.reader(csvfile)
    for row in rdr:
        market_id_to_market_info[row[3]] = row
