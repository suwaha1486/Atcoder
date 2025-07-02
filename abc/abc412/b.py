s = input()
t = set(list(input()))

pre_str = ""
for i in range(len(s)-1):
    if s[i+1].isupper():
        pre_str += s[i]

for i in range(len(pre_str)):
    if pre_str[i] not in t:
        print("No")
        exit()

print("Yes")
