# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority level"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"\nReminder: {reminder}")
else:
    # Provide different messages based on priority for non-time-bound tasks
    if priority == "high":
        reminder += ". Make sure to complete it soon."
    elif priority == "medium":
        reminder += ". Try to complete it when possible."
    elif priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

    print(f"\nReminder: {reminder}")
