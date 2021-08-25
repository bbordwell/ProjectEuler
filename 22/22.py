#This program solves Project Euler #22

f = open('names.txt')
names = f.read()
names = names.replace('"','')
names = names.split(',')
names.sort()

def score(name):
    """Given a name in all capital letters return its alphabetical value"""
    letters = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for letter in name:
        ans += letters.index(letter)
    return ans

ans = 0
for index,name in enumerate(names):
    ans += score(name) * (index+1)
print(ans)
