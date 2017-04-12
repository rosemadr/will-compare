#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    # have we got an empty line? then move on to next line
    if re.match('^\s*$', line):
        continue

    # remove any leading or trailing whitespace
    # e.g. spaces and  newlines
    # and print the result
    print(line.rstrip().lstrip())

