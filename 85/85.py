#This program solves Project Euler #85.

def countingRectangles(x,y):
    """Given a rectangle of dimentions x,y return how many rectangles it contains."""
    ans = 0
    for smallX in range(x):
        for smallY in range(y):
            ans += (x-smallX) * (y-smallY)
    return ans

nearest = 2_000_000
for x in range(3,80):
    for y in range(2,80):
        solutions = countingRectangles(x,y)
        if abs(2_000_000 - solutions) < nearest:
            nearest = abs(2_000_000 - solutions)
            ans = (x,y)
print(ans)
print(ans[0]*ans[1])

