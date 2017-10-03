u, v, x, y = 0, 0, 100, 30
while x > y:
    u = u + y
    print("u=%i" % u)
    x = x - y
    print("x=%i" % x)
    if x < y + 2:
        v = v + x
        print("v=%i" % v)
        x = 0
    else:
        v = v + y + 2
        print("v=%i" % v)
        x = x - y - 2
        print("x=%i" % x)
print("u=%i and v=%i" %(u, v))