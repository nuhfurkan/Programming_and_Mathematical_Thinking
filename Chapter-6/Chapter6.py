# Function implementation of name searching
def example6_1():
    file = open("name")

    def filter(fun, ls):
        for i in ls:
            if fun(i):
                print(i[:-1])

    filter(lambda x: str(x).startswith("John"), file)

# Function implemetation of average values given in the file "observations"
def example6_2():
    file = open("observations")

    def map(fn, ls):
        result = ()
        for i in ls:
            result += ( fn(float(i)), )
        return result

    res = (lambda x: sum(x)/len(x)) (map(float, file))
    print(res)

# Investigating Python's Floating-pont Arithmatic
def exercise1():
    fr = (1/3 + 1/2) + 1/6
    sc = (1/3 + 1/6) + 1/2
    print((fr == sc))
    # fr and sc should be equal in terms of mathematics, however, due to floating-point arithmatic they are not

# Investigation of monoidity of Python integers under "**" operations
def exercise3():
    nfalse = 0
    for n in range(1, 100):
        fr = (1/n)**0.5
        sc = 1/(n**0.5)
        if fr != sc:
            nfalse += 1
            print(fr == sc)
    print (nfalse)

# Investigating commutativity of "and" and "or" operators
def exercise4():
    bool1 = True or False
    bool2 = True or False
    bool3 = True and False
    bool4 = False and True
    print(bool1 == bool2)
    print(bool3 == bool4)

# Sum function implementation
def exercise8():
    def big(param):
        res = 0
        for i in param:
            res += i
        return res
        
    p = tuple([1,23,4])
    print(big(p))

# Implementation of reduce function without initial parameter
def exercise9():
    def reduce(fn, ls):
        if len(ls) <= 0:
            print
        result = ls[0]
        for i in range(1, len(ls)):
            result = fn(result, ls[i])
        return result
