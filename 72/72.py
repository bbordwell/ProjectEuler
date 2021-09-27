import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import phis

#This program solves Project Euler #72.

print(sum(phis(1_000_000).values()))
#https://wikimedia.org/api/rest_v1/media/math/render/svg/a5946a2637b50c6d7d552808c2c7732216b91fff

