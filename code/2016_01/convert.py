#!/usr/bin/env python3

import sys

infile_name = sys.argv[1]
outfile_name = sys.argv[2]


with open(infile_name, encoding='big5') as f :
    content = f.read()

with open(outfile_name, 'w', encoding='utf8') as f:
    f.write(content)

