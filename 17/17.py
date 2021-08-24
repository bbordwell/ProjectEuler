import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import writtennumber

#This program solves Project Euler #17
#Generate each written number and measure the length. Add to a running total.
#Display the total at the end.
ans = 0
for num in range(1,1_001):
    ans += len(writtennumber(num,withand=True))
print(ans)