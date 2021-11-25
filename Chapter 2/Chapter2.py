import math

# Trying to calculate f(n) = 2**2**n for different n values
def exercise1():
    print("Exercise 1")
    for n in range(1,20):
        print("For " + str(n))
        print(2**2**n)
    print("----------\n")

# Try to print 2**2**10
# Note: After 5 minutes I stopped program
def exercise2():
    print("Exercise 2")
    print(2**2**100)
    print("----------\n")

# Number of digits in 2**2**100
def exercise3():
    print("Exercise 3")
    res = 10**2*math.log(2, 10)
    res = 10**res*math.log(2, 10)
    print("Estimated number of digits in 2**2**100:")
    print(res)
    print("----------\n")

# Some roundings to take consideration into
def exercise4():
    print("Exercise 4")
    n = 1.0 == 1
    print("1.0 == 1 is " + str(n))
    n = 1/3+1/3+1/3 == 1
    print("1/3+1/3+1/3 == 1 is " + str(n))
    n = (1/3)*3 == 1
    print("(1/3)*3 == 1 is " + str(n))
    print("----------\n")

# To learn difference between startswith("John") and == "John"
def exercise6():
    print("Exercise 6")
    file = open("name")
    for line in file:
        name, rest = line.split(" ", 1)
        if name == "John":
            print(line.strip("\n"))
    print("----------\n")

exercise1()
exercise2()
exercise3()
exercise4()
exercise6()


