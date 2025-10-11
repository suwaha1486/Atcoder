x, y = input().split()

os_version_dict = {"Ocelot": 0, "Serval": 1, "Lynx": 2}

if os_version_dict[x] >= os_version_dict[y]:
    print("Yes")
else:
    print("No")