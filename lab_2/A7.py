x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) %2 == (x2 + y2) %2:
    print("YES", ['White', 'Black'] [(x1 + y1) % 2 == 1])
else:
    print("NO")