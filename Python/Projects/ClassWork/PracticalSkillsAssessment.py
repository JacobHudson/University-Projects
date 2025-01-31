def AddReg():
    r = input("Enter Registration to Add: ")
    car_regs.append(r)

def PrintAllRegs():
    if len(car_regs) == 0:
        print("No Cars are Currently in the List!")
    for i in range(len(car_regs)):
        print(f"Index {i}: {car_regs[i]}")

def PrintRegByIndex(i):
    if len(car_regs) > i and i >= 0:
        print(f"Index {i}: {car_regs[i]}")
    else:
        print(f"Invalid Input! Must be between 0 and {len(car_regs)-1}")

def BulkUploadCSV(path):
    try:
        csv = open(path, "r")
        regs = (csv.read().split(","))
        for i in range(len(regs)):
            car_regs.append(regs[i].strip())
        csv.close
    except FileNotFoundError as e:
        print(f"File at path [{path}] could not be found!")

def ExportToTXT(name):
    txt = ""
    for i in range(len(car_regs)):
        txt += f"Index {i}: {car_regs[i]}\n"
    out = open(name, "w")
    out.write(txt)
    out.close

def PrintOptions():
    print("Please select a option (1-6): ")
    print("     1 to add a car to the list")
    print("     2 to prints all cars to the screen")
    print("     3 to print a single car to the screen using the item index")
    print("     4 to add a batch of cars to the list")
    print("     5 to download the contents of the list to a file")
    print("     6 to quit the program")

def GetInput():
    i = input("Enter the number (1-6) of your desired action: ")
    if i == "1":
        AddReg()
    elif i == "2":
        PrintAllRegs()
    elif i == "3":
        i = input("Enter Index to Search: ")
        try:
            i = int(i) 
            PrintRegByIndex(i)
        except Exception as e:
            print("Invalid Input! must be a Number")
    elif i == "4":
        p = input("Enter CSV file path and extention: ")
        BulkUploadCSV(p)
    elif i == "5":
        n = input("Enter name of output file: ")
        ExportToTXT(n)
    elif i == "6":
        return True
    else:
        print("A valid option wasnt selected!")

    print("-----------------------------------")
    return False

car_regs = []
quit = False

while not quit:
    PrintOptions()
    quit = GetInput()
