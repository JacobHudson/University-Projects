file_name = "Data/grades.csv"
results_file_name = "Data/Results.txt"

names = []
marks = []
percents = []
grades = []

max_score = 75

def WriteToFile():
    o_file = open(results_file_name, 'w')
    for i in range(len(names)):
        o_file.write(f"{names[i]}, {percents[i]}% \n")

    highest_i = marks.index(max(marks))
    o_file.write(f"\nHighest Mark: {names[highest_i]} \n Mark: {marks[highest_i]} Percent: {percents[highest_i]}%")

    lowest_i = marks.index(min(marks))
    o_file.write(f"\nLowest Mark: {names[lowest_i]} \n Mark: {marks[lowest_i]} Percent: {percents[lowest_i]}%\n")

    o_file.write(f"\nRange of Marks:{str(marks[lowest_i]).strip()} - {marks[highest_i]}")
    o_file.write(f"\nRange of Percent:{str(percents[lowest_i]).strip()}% - {percents[highest_i]}%\n")

    t = 0
    for m in marks:
        t += int(m)
    
    o_file.write(f"\nAverage Mark: {t/len(marks)}\n")

    o_file.write(f"\n'A' count: {grades.count('A')}")
    o_file.write(f"\n'B' count: {grades.count('B')}")
    o_file.write(f"\n'C' count: {grades.count('C')}")
    o_file.write(f"\n'D' count: {grades.count('D')}")
    o_file.write(f"\n'E' count: {grades.count('E')}")
    o_file.write(f"\nFail ('F') count: {grades.count('F')}")

    o_file.close

def PrintToConsole():
    r_file = open(results_file_name, 'r')
    for line in r_file:
        print(line.strip())
    r_file.close

def CalculateData():
    i_file = open(file_name, "r")
    for line in i_file:
        names.append(line.split(",")[0].strip())
        marks.append(line.split(",")[1].strip())

        percents.append(round(((int(line.split(",")[1])/max_score) * 100), 2))
    i_file.close

    for m in marks:
        g = ''
        m = int(m)
        if m >= 0.8 * max_score:
            g = 'A'
        elif m >= 0.7 * max_score:
            g = 'B'
        elif m >= 0.6 * max_score:
            g = 'C'
        elif m >= 0.5 * max_score:
            g = 'D'
        elif m >= 0.4 * max_score:
            g = 'E'
        else:
            g = 'F'

        grades.append(g)

def PrintDataByName(n):
    while names.count(n) == 0:
        print("NAME NOT FOUND OR INVALID VALUE ENTERED")
        n = input("Enter the name of a student to get their raw mark, percentage, and letter grade")

    i = names.index(n)
    print(f"Name: {names[i]}\n Raw Mark: {marks[i]}\n Percentage: {percents[i]}\n Grade: {grades[i]}")

CalculateData()
WriteToFile()
PrintToConsole()

while True:
    n = input("Enter the name of a student to get their raw mark, percentage, and letter grade")
    PrintDataByName(n)