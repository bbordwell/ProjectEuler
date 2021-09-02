import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import triangleNumbersGenerator

#This program Solves Project Euler #42

def score(word):
    """Given a name in all capital letters return its alphabetical value"""
    letters = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for letter in word:
        ans += letters.index(letter)
    return ans

f = open("words.txt")
words = f.read()
words = words.split(',')
words = [word.replace('"','') for word in words]

triangles = set(triangleNumbersGenerator(limit=193))

ans = 0
for word in words:
    if score(word) in triangles:
        ans += 1
print(ans)