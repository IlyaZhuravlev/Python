a = map(int, input().replace(' ',''))
a = sorted(a)
g = False 
for i in range(0, len(a)):
    if a.count(i) > 1:
        g = True
print(g)
