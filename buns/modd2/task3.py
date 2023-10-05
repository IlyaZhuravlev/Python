a , b , c= map(int, input().split())
k=min(a, b, c)
m=max(a, b, c)
h= a + b + c - k - m
print(h)
