import matplotlib.pyplot as plt

#Finding a name
def example1():
    file = open("Chapter 1/name")
    for line in file:
        if line.startswith("John"):
            print(line)

# Finding an email
def example2():
    file = open("Chapter 1/emails")
    for line in file:
        name, email = line.split(",")
        if (name == "John Wick"):
            print(email)

# Average of a collection of observations
def example3():
    temps = []
    days = []
    sum = 0
    count = 0
    file = open("Chapter 1/observations")
    for line in file:
        sum += float(line)
        count += 1
        temps.append(float(line))
        days.append(int(count))

    print("Sum is " + str(sum))
    print("Average is " + str(round(sum/count, 2)))
    plt.plot(days, temps, "o")
    plt.show()

example3()
