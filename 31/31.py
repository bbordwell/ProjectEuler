#This program solves Euler #31.
#Brute force solution.
ans = 0
for p200 in range(2):
    for p100 in range(3):
        if (p200*200)+(p100*100) > 200:
            break
        for p50 in range(5):
            if (p200*200)+(p100*100)+(p50*50) > 200:
                break
            for p20 in range(11):
                if (p200*200)+(p100*100)+(p50*50)+(p20*20) > 200:
                    break
                for p10 in range(21):
                    if (p200*200)+(p100*100)+(p50*50)+(p20*20)+(p10*10) > 200:
                        break
                    for p5 in range(41):
                        if (p200*200)+(p100*100)+(p50*50)+(p20*20)+(p10*10)+(p5*5) > 200:
                            break
                        for p2 in range(101):
                            if (p200*200)+(p100*100)+(p50*50)+(p20*20)+(p10*10)+(p5*5)+(p2*2) > 200:
                                break
                            for p1 in range(1):     #There will be one way to add more 1p coins to get to 200p
                                ans += 1
print(ans)