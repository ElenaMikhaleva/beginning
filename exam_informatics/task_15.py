def function(n,m):
    if n%m==0:
        return True
    else:
        return False

for a in range (300):
    k = 0
    for x in range (300):
        expression = (x%a!=0) <= ((x%6==0) <= (x%4!=0))
        if expression == 1:
            k += 1
    if k == 300:
        print (a)
