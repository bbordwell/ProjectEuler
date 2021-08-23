answers = []
for a in range(999,900,-1):
    for b in range(999,900,-1):
        if str(a*b) == str(a*b)[::-1]:
            answers.append(a*b)
print(max(answers))