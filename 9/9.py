import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import pythagoreanTriples

#This program solves Project Euler #9.
#Generate all Pythagorean triples with sides less than 500
#Check if the sum of the triple is 100, if so it is the answer
triples = pythagoreanTriples(500)
for triple in triples:
    if sum(triple) == 1000:
        print(triple)
        print(triple[0]*triple[1]*triple[2])