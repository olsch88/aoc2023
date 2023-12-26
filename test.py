def f(x):
    while True:
        x = yield x * 2


g = f(7)
# print(g.send(g.send(g.send(None))))
print(g.send(None))
