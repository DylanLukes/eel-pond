#! /usr/bin/env python
# take an NCBI file and make a TSV connecting identifier with description.
import screed
import csv
import sys

outfile = sys.argv[2]

rows = []
is_ncbi = False
for record in screed.open(sys.argv[1]):
    if record.name.startswith('gi|'):
        is_ncbi = True
        ident = record.name.split('|')[3]
    else:
        ident = record.name
    rows.append({'ident': ident, 'name': record.name, 'desc': record.description})

with open(outfile, 'w') as tsvfile:
    writer = csv.DictWriter(tsvfile, ['ident', 'name', 'desc'], delimiter='\t')
    writer.writeheader();
    writer.writerows(rows);



