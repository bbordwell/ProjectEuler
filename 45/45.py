#This program solves Project Euler #45.

limit = 5_000_000_000   #The max value to generate numbers to.

#Generate trianlge numbers.
triangles = set()
i = 0
while i*(i+1) /2  < limit:
    i += 1
    triangles.add(i*(i+1) //2)

#generate pentagonal numbers.
pentagons = set()
i = 0
while i*(3*i -1)/2 < limit:
    i += 1
    pentagons.add(i*(3*i -1)/2)

#Generate hexagonal numbers and check if they are triangle and pentagonal
counter = 0
i = 0
while counter < 3 and i*(2*i -1) < limit:
    i += 1
    if i*(2*i -1) in triangles and i*(2*i -1) in pentagons:
        counter += 1
if counter == 3: #First two solution are known, we are looking for the 3rd.
    print(i*(2*i -1))