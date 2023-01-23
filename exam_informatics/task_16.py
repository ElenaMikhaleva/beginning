def function(n):
    if n==1:
        return 1
    if n==2:
        return 3
    if n>2:
        return function(n-1)*function(n-2) + (n-2)

print (function(5))