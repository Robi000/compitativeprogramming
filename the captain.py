# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input ()
y = input()
# print(x)
# print(y)
m = y.split(" ")
# print(m)
d = {}
for j in m:
    if j not in d:
        d[j]=0
    d[j] += 1

# print(d)
for j in d:
    if d[j] != int(x):
        print(j)
        break
    
