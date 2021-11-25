# Print the character '#', for n times (n given in the file "data") 
def exercise1():
    file = open("data")
    for line in file:
        sharps = ""
        for _ in range(1, int(line)+1):
            sharps += "#"
        print(sharps + " " + str(line))

# Print maximum 25 '#' character for n times (n given in the file "data") 
def exercise2():
    file = open("data")
    for line in file:
        sharps = ""
        num = 0
        if int(line) > 25:
            num = 25
        else:
            num = int(line)
        for _ in range(1, num+1):
            sharps += "#"
        print(sharps + " " + str(line))

# Print the character '#', for n times (n given in the file "data")
# Special output for n > 25 as follows "###########/ /###########"
def exercise3():
    file = open("data")
    for line in file:
        sharps = ""
        num = 0
        if int(line) > 25:
            print("###########/ /########### " + line)
        else:
            num = int(line)
            for _ in range(1, num+1):
                sharps += "#"
            print(sharps + " " + line)

# Investivate square root program
def exercise4(n):
    # ATTENTION : Infinite loop if n < 0
    guess = 1.0
    while abs(n - guess*guess) > .00001:
        guess = guess - (guess*guess - n)/(2*guess)
        print(guess)
    root = guess

# Further investigation of square root program
def exercise5(n):
    # ATTENTION : Infinite loop due to int(guess)
    guess = 1
    while abs(n - guess*guess) > .0001:
        guess = guess - (guess*guess - n)/(2*guess)
        print(guess)
    root = guess

exercise1()
exercise2()
exercise3()
exercise4()
exercise5()