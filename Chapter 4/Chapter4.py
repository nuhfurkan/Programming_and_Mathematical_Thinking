# Investigation of derivative function
def exercise1():
    def cube(x):
        return x**3

    def square(x):
        return x*x
    
    def deriv(f, x, dx):
        return (f(x+dx)-f(x))/dx

    res = deriv(square, 3, .00001)
    print(res)
    res = deriv(cube, 4, .00001)
    print(res)

# Investigation of gloabal variable within a function
def exercise2():
    a = 1
    def f(n):
        return n + a
    print(f(1))
    a = 3
    print(f(1))

exercise1()
exercise2()