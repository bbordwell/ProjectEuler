#This program solves Project Euler #112.

bouncy = 0
for x in range(1,10000000):
    if ''.join(sorted(str(x))) == str(x):
        continue
    if ''.join(sorted(str(x),reverse=True)) == str(x):
        continue
    bouncy += 1
    if bouncy/x >= 0.99:
        print(x)
        break