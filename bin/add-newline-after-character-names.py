#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    # deal with abbreviated character names
    for name in [ 'FRANCISCO', 'BERNARDO', 'MARCELLUS', 'HORATIO']:
        line = re.sub('^'+name, name+'\n', line.rstrip())

    print(line)

