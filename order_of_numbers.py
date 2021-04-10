def func1(i):
    if i < 0:
        return
    print(i)
    func2(i - 1)

def func2(i):
    func1(i - 1)
    print(i)

func1(5)
