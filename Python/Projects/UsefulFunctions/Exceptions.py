def printName():
    r_names = open(f"Data/{input("Enter File Name: ")}.txt", "r")
    ln_number = int(input("Enter a line number to read: "))
    names = []
    for line in r_names:
        names.append(line)
    r_names.close
    print(names[ln_number - 1], end="")

error_raised = True
while error_raised:
    try:
        printName()
    except FileNotFoundError as file_not_found_e:
        print(f"File {file_not_found_e.filename} could not be found!")
    except PermissionError as permission_e:
        print(f"Permission is not granted to open {permission_e.filename}")
    except ValueError as value_e:
        print(f"line number must be a number")
    except IndexError as index_e:
        print(f"{index_e}")
    else:
        print("No excesption was raised")
        error_raised = False
    finally:
        print("Finished Executing")

print("Done")