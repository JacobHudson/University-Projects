def main():
    print("Welcome to Your Average Calculator")

    num_nums = get_number_input("x")
    nums_list = []

    for i in range(num_nums):
        nums_list.append(get_number_input(i+1))

    print("The average of the numbers you entered is: " + str(calculate_average(nums_list)))

def get_number_input(input_num):
    valid_entry = False

    if(input_num == "x"):
        entry_string = "Please enter the number of numbers you want to enter: "
    else:
        entry_string = "Please enter number " + str(input_num) + ": "

    while not valid_entry:
        entered_number = input(entry_string)
        if(entered_number.isdigit()):
            number_to_return = int(entered_number)
            valid_entry = True
        else:
            print("That is not a valid entry, please try again!")

    return number_to_return

def calculate_average(list_of_nums):
    number_of_numbers = len(list_of_nums)
    sum_nums = 0

    for i in list_of_nums:
        sum_nums += i

    return sum_nums/number_of_numbers

main()
