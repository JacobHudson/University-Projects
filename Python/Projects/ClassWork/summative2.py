def add_workout_from_user(workout):
    workouts.append(get_input())
    
def add_workout_from_file(filepath):
    try:
        data_r = open(filepath, "r")
        for line in data_r:
            workouts.append(line.strip().lower().split(","))
        data_r.close()
    except FileNotFoundError as fnfe:
        print(f"File not Fount: {fnfe.filename} does not exist!")

def valid_workout_type(workout_type):
    if valid_workouts.count(workout_type.lower()):
        return True
    return False

def get_input():
    date = input("Enter date: ")

    valid = False
    while not valid:
        workout_type = input("Enter workout type: ")
        valid = valid_workout_type(workout_type)
        if not valid:
            print("Workout type is not valid!")

    valid = False
    while not valid:
        duration = input("Enter duration: ")
        valid = duration.isdigit()
        if not valid:
            print("Duration is not valid!")

    return [date, workout_type, int(duration)]

def get_workout_type():
    valid = False
    while not valid:
        workout_type = input("Enter workout type: ")
        valid = valid_workout_type(workout_type)
        if not valid:
            print("Workout type is not valid!")
    
    return workout_type

def get_events(workout_type):
    events = []
    for workout in workouts:
        if workout[1].lower() == workout_type.lower():
            events.append([workout[0], workout[2]])

    return events
    
def print_events(events):
    for event in events:
        print(f"Date: {event[0]}, Duration: {event[1]}")

def calculate_avg_duration_for_each_workout():
    avg = []
    for workout_type in valid_workouts:
        total = 0
        count = 0
        for workout in workouts:
            if workout[1].lower() == workout_type:
                count += 1
                total += int(workout[2])
        avg.append(total/count)
    return avg

def avg_of_each_workout():
    s = ""
    avgs = calculate_avg_duration_for_each_workout()
    for i in range(len(valid_workouts)):
        s += (f"{valid_workouts[i]}: {avgs[i]} \n")
    return s

def create_summary():
    summary_w = open("Data/Summary.txt", "w")
    summary_w.write(avg_of_each_workout())

workouts = []
valid_workouts = ["strength training", "running (indoor)", "running (outdoor)",
                  "swimming (pool)", "swimming (outdoor)", "gym", "zumba", "spin class"]

filepath = "Data/workouts group 2.csv"
add_workout_from_file(filepath)

create_summary()
# while True:
#     print_events(get_events(get_workout_type()))