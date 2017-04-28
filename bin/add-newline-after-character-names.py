#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    # deal with abbreviated character names
    for name in [ 'FRANCISCO', 'BERNARDO', 'MARCELLUS', 'HORATIO',
                  'KING', 'CORNELIUS', 'VOLTENMAND', 'LAERTES',
                  'POLONIUS', 'HAMLET', 'QUEEN', 'OPHELIA',
                  'GHOST', 'REYNALDO', 'ROSENCRANTZ', 'GUILDENSTERN',
                  'FIRST PLAYER', 'PLAYER KING', 'PLAYER QUEEN', 'LUCIANUS',
                  'GRAVEDIGGER', 'OTHER', 'PROLOGUE', 'FORTINBRAS','AMBASSADOR', 'OSRIC', 'LORD',]:
        line = re.sub('^'+name, name+'\n', line.rstrip())

    print(line)

