s12, s13 = input().split()

if s12 == s13 == 'fine':
    print(4)
elif s12 == s13 == 'sick':
    print(1)
elif s12 == 'fine' and s13 == 'sick':
    print(3)
else:
    print(2)