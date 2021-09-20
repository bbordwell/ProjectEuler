from itertools import permutations
from itertools import cycle

#This program solves Project Euler #59

def decode(text,key):
    """Input a list of strings and a key, output a decrypted string"""
    key = [ord(x) for x in key]
    key = cycle(key)
    text = [x ^ key.__next__() for x in text]
    text = [chr(x) for x in text]
    return ''.join(text)

file = open("cipher.txt")
for line in file:
    chars = line.split(',')
chars = [int(x) for x in chars]

keys = permutations('abcdefghijklmnopqrstuvwxyz',3)

most = 0
for key in keys:
    message = decode(chars.copy(),key)
    if message.count('the') > most:
        most = message.count('the')
        ans = key


decryptedText = decode(chars,ans)
print(decryptedText)
print(f'The key is {ans}')
ans = 0
for letter in decryptedText:
    ans += ord(letter)
print(ans)