def task_12(l):
    while ('222' in l) or ('888' in l):
        if ('222' in l):
            l = l.replace('222','8',1)
        else:
            l = l.replace('888','2',1)
    print (l)

l='8'*68
task_12(l)