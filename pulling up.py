# Enter your code here. Read input from STDIN. Print output to ST# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import inf
testes = int(input())
stack = []
for test in range(testes):
    j = int(input()) - 1
    arr = list(map(int, input().split()))
    i = 0
    last = inf
    while i < j:
        if arr[i] > arr[j]:
            if arr[i] > last:
                print("No")
                break 
            else:
                last = arr[i]
                i += 1
        else:
            if arr[j] > last:
                print("No")
                break 
            else:
                last = arr[j]
                j -= 1
    else:
        print("Yes")
                
