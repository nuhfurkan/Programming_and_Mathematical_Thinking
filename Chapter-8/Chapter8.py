from os import name, read


def exercise1():
    def takeNames(filename):
        return { name.strip() for name in open(filename) }

    for names in takeNames("Necessary_Files/namelist_files/first_file") & takeNames("Necessary_Files/namelist_files/second_file"):
        print(names)
    
def exercise2():
    def getDividors(n):
        div = 2
        result = set() 
        while n != 1:
            if n%div == 0:
                result.add(div)
                n/=div
            else:
                div += 1
        return result

    for num in getDividors(1024):
        print(num)

def exercise3():
    import csv
    def getData(filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            return { tuple(row) for row in reader }

    def myInt(str):
        num = str.split(".")
        res = 0
        res += int(num[0]) + int(num[1])*0.1
        return res

    years = {4}
    goodmajors = {"Computer Science", "Electrical Engineering"}
    goodgrades = {3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0}
    names = { name for (name, major, year) in getData("Necessary_Files/student_data/students.csv") if year=="4" and (major == "Computer Science" or major == "Electrical Engineering") }
    grades = { name for (name, grade) in getData("Necessary_Files/student_data/grades.csv") if myInt(grade) >= 3 } 

    goodnames = names & grades
    for i in goodnames:
        print(i)
