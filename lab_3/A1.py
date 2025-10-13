x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1*x2>0) and (y2*y1>0):
    if x1>0 and y1>0:
        print('Yes, I')
    elif x1<0 and y1>0:
        print('Yes, II')
    elif x1<0 and y1<0:
        print('Yes, III')
    else:
        print('Yes, IV')
else:
    print('No')