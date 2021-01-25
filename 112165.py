x, y = map(float, input().split())
if ((x * x) + (y * y) >= 4) and (y <= x <= 2) and (y >= 0):
    print("YES")
else:
    print("NO")
