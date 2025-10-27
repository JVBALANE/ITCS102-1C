r = 6
for i in range(1, r + 1):
    print(" "*(r - i), end="")
    for x in range(i, 0, -1):
        print(x, end="")
    for x in range(2, i + 1):
        print(x, end="")
    print()
