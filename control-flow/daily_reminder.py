# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task’s priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity using match case and if statements
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task."
        if time_bound == 'yes':
            reminder += " Try to complete it soon."
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task."
        if time_bound == 'yes':
            reminder += " Complete it if you have time today."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Print the customized reminder
print(reminder)


           
