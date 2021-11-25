import matplotlib.pyplot as plt

#Finding a name
def example1():
    print("Example 1")
    file = open("name")
    for line in file:
        if line.startswith("John"):
            print(line.strip("\n"))
    print("----------\n")

# Finding an email
def example2():
    print("Example 2")
    file = open("emails")
    for line in file:
        name, email = line.split(",")
        if (name == "John Wick"):
            print(email.strip("\n"))
    print("----------\n")

# Average of a collection of observations
def example3():
    print("Example 3")
    temps = []
    days = []
    sum = 0
    count = 0
    file = open("observations")
    for line in file:
        sum += float(line)
        count += 1
        temps.append(float(line))
        days.append(int(count))

    print("Sum is " + str(sum))
    print("Average is " + str(round(sum/count, 2)))
    plt.plot(days, temps, "o")
    plt.show()
    print("----------\n")

example1()
example2()
example3()