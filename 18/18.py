#This program solves Project Euler #18
#Create a list of lists, where each list is a level of this pyramid
ps =""" 
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
ps = [int(x) for x in ps.split()]
path = [[ps[0]],ps[1:3],ps[3:6],ps[6:10],ps[10:15],ps[15:21],ps[21:28],ps[28:36],
        ps[36:45],ps[45:55],ps[55:66],ps[66:78],ps[78:91],ps[91:105],ps[105:120]]

#Starting at the second from the top level, for each block on each level add the
#highest reachable block from the previous level.
for step in range(14):
    current = path[step]
    next = path[step+1]
    for index,value in enumerate(next):
        if index == 0:
            path[step+1][0] += current[0]
        elif index == len(next)-1:
            path[step+1][-1] += current[-1]
        else:
            path[step+1][index] += max([current[index-1],current[index]])
print(max(path[-1]))
#Once at the bottom, each blocks value represents the highest sum of any path
#that could have gotten to it. Display the highest sum