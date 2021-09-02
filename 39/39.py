import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from collections import Counter

from usefulfunctions import pythagoreanTriples

#This program solves Project Euler #39.

triangles = pythagoreanTriples(500)     #Generate all right triangles with sides below 500
triangles = [sum(x) for x in triangles] #Find the perimeter of those triangles
triangles = Counter(triangles)  #Count how many times each perimeter shows up
print(triangles.most_common()[0][0])    #Display the most common perimiter