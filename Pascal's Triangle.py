def print_pascal_triangle(n):
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")
            C = C * (line - i) // i
        print()

rows = 5
print_pascal_triangle(rows)

"""

Output:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 

"""