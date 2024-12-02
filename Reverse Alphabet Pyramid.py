rows = 5
ascii_value = 65 + rows - 1

for i in range(rows):
    for j in range(i, -1, -1):
        print(chr(ascii_value - j), end="")
    print()


"""

Output:

E
DE
CDE
BCDE
ABCDE

"""