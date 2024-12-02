rows = 5
for i in range(1, rows + 1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

"""

Output:

A 
A B 
A B C 
A B C D 
A B C D E 

"""