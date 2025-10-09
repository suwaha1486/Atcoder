s = input()

world = int(s[0])
stage = int(s[2])

if stage < 8:
    stage += 1
else:
    world += 1
    stage = 1

print(f"{world}-{stage}")