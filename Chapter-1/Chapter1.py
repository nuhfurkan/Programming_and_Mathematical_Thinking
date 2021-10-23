#Finding a name
def example1():
    file = open("name")
    for line in file:
        if line.startswith("John"):
            print(line)

# Finding an email
def example2():
    file = open("emails")
    for line in file:
        name, email = line.split(",")
        if (name == "John Wick"):
            print(email)

# Average of a collection of observations
def example3():
    sum = 0
    count = 0
    file = open("observations")
    for line in file:
        sum += float(line)
        count += 1

    print("Sum is " + str(sum))
    print("Average is " + str(round(sum/count, 2)))

example3()
