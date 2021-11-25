import time

def exercise1():
    def fibs(n):
        a = 1
        b = 1
        for i in range(n):
            yield a
            a, b = b, a+b

    def fibsTuple(n):
        result = ()
        a = 1
        b = 1
        for i in range(n):
            result += (a,)
            a, b = b, a+b
        return result

    def fibsList(n):
        result = []
        a = 1
        b = 1
        for i in range(n):
            result.append(a)
            a, b = b, a+b
        return result

    start_time = time.time()
    for i in fibs(500):
        print()
    print((time.time() - start_time))

def exercise2():
    def prefix(n, myStream):
        it = iter(myStream)
        for i in range(n):
            yield next(it, None)

def exercise4():
    def integers(n):
        while True:
            yield n
            n += 1

    l = map(integers, integers(0))
    l = map(integers, range(5))
    print(list(l))
