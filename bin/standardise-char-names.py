#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():

    # deal with abbreviated character names
    line = line.replace('Fran.', 'FRANCISCO')
    line = line.replace('Ber.','BERNARDO')
    line = line.replace('BARNARDO','BERNARDO')
    line = line.replace('Barnardo', 'Bernardo')
    line = line.replace('Mar.','MARCELLUS')
    line = line.replace('Hor.','HORATIO')
    line = line.replace('King.', 'KING')
    line = line.replace('KING CLAUDIUS','KING')
    line = line.replace('Cor.', 'CORNELIUS')
    line = line.replace('Volt.', 'VOLTEMAND')
    line = line.replace('VOLTIMAND', 'VOLTEMAND')
    line = line.replace('Volitmand', 'Voltemand')
    line = line.replace('Laer.','LAERTES')
    line = line.replace('Pol.', 'POLONIUS')
    line = line.replace('LORD POLONIUS', 'POLONIUS')
    line = line.replace('Ham.','HAMLET')
    line = line.replace('Queen.','QUEEN')
    line = line.replace('QUEEN GERTRUDE','QUEEN')
    line = line.replace('Oph.','OPHELIA')
    line = line.replace('Ghost.','GHOST')
    line = line.replace('Ghost', 'GHOST')
    line = line.replace('Rey.','REYNALDO')
    line = line.replace('Ros.','ROSENCRANTZ')
    line = line.replace('Guil.','GUILDENSTERN')
    line = line.replace('Fort.','FORTINBRAS')
    line = line.replace('PRINCE FORTINBRAS','FORTINBRAS')
    line = line.replace('1 Ambassador.','AMBASSADOR')
    line = line.replace('First Ambassador','AMBASSADOR')
    line = line.replace('Lord.', 'LORD')
    line = line.replace('Osr.', 'OSRIC')
    line = line.replace('I Play.','FIRST PLAYER')
    line = line.replace('First Player','FIRST PLAYER')
    line = line.replace('P. King.','PLAYER KING')
    line = line.replace('Player King','PLAYER KING')
    line = line.replace('P. Queen.','PLAYER QUEEN')
    line = line.replace('Player Queen','PLAYER QUEEN')
    line = line.replace('Luc.', 'LUCIANUS')
    line = line.replace('Pro.','PROLOGUE')
    line = line.replace('Prologue','PROLOGUE')
    line = line.replace('1 Clown', 'GRAVEDIGGER')
    line = line.replace('First Clown','GRAVEDIGGER')
    line = line.replace('2 Clown', 'OTHER')
    line = line.replace('Second Clown','OTHER')

    print(line)

