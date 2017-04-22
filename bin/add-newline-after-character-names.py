#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    # deal with abbreviated character names
    for name in [ 'FRANCISCO', 'BERNARDO', 'MARCELLUS', 'HORATIO', 'KING CLAUDIUS', 'CORNELIUS', 'VOLTENMAND', 'LAERTES', 'POLONIUS', 'HAMLET', 'QUEEN GERTRUDE', 'OPHELIA', 'THE GHOST', 'REYNALDO', 'ROSENCRANTZ', 'GUILDENSTERN', 'FIRST PLAYER', 'PLAYER KING', 'PLAYER QUEEN', 'LUCIANUS', 'GRAVEDIGGER', 'OTHER']:
        line = re.sub('^'+name, name+'\n', line.rstrip())

    print(line)

