# Investigating n-tuples
def n_tuples():
    x = 1
    y = 2
    x, y = y, x
    print(x)
    print(y)
    newTuple = x, y, 1, "test"
    print(newTuple)
    for elem in range(0,4):
        print(newTuple[elem])

# Investigating csv files
def csvTut():
    import csv
    idNum = 1

    def createHeader():
        db_header = ("id", "name", "surname")
        with open("c5_csvTut.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(db_header)

    def addRow(name, surname):
        with open("c5_csvTut.csv", "a") as file:
            nonlocal idNum
            print(idNum)
            writer = csv.writer(file)
            writer.writerow((idNum, name, surname))
            idNum += 1

    def readCsv():
        with open("c5_csvTut.csv") as file:
            reader = csv.reader(file)
            header = 0
            for row in reader:
                if  header == 0:
                    lens = []
                    lens.append(len(row[0]))
                    lens.append(len(row[1]))
                    lens.append(len(row[2]))
                    print(row[0], row[1], row[2], sep="|")
                    lines = ["", "", ""]
                    counter =  0
                    for i in lens:
                        for _ in range(1, i+1):
                            lines[counter] += "-"
                        counter += 1
                    print(lines[0], lines[1], lines[2], sep="|")
                    header = 1
                else: 
                    print(row[0], row[1], row[2], sep="|")

    createHeader()
    addRow("Nuh", "Erturk")
    addRow("Furkan", "Erturk")
    readCsv()


n_tuples()
csvTut()
