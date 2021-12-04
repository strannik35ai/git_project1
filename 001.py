# y2=x2+1594^2+1594*x
print(11)
for x in range(2, 100000000):
    yy = x * x + 1594 ** 2 + 1594 * x
    z = round((yy) ** 0.5)
    if z*z == yy:
        print(x, z)
print(22)