#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    # have we got an empty line? then move on
    if re.match('^\s*$', line):
        continue

    # remove any trailing whitespace, e.g. newline characters
    line = line.rstrip()

    # deal with abbreviated character names
    line = line.replace('Fran.', 'FRANCISCO')
    line = line.replace('Ber.','BERNARDO')
    line = line.replace('Mar.','MARCELLUS')
    line = line.replace('Hor.','HORATIO')
    

    print(line)

