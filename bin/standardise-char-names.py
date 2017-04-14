#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():

    # deal with abbreviated character names
    line = line.replace('Fran.', 'FRANCISCO')
    line = line.replace('Ber.','BERNARDO')
    line = line.replace('Mar.','MARCELLUS')
    line = line.replace('Hor.','HORATIO')
    

    print(line)

