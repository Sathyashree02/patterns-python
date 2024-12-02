n = 5
for i in range(1, n+1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i+1)))
for i in range(n-1, 0, -1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i+1)))

"""

Output:

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

"""