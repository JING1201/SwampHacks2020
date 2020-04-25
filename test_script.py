def err1():
    print("stuff"+1)

def err2():
    print(10/0)

def err3():
    a = None
    a += 3

def err4():
    a = {}
    a[0] += 1

err3()