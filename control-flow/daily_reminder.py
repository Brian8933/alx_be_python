# daily_reminder.py

# Step 1: Collect user input
print("Task:")
task = input()

print("Priority (high/medium/low):")
priority = input().lower()

print("Time Bound (yes/no):")
time_bound = input().lower()

# Step 2: Process using match-case and if-statement
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Step 3: Add time sensitivity to the message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Step 4: Output the result
print("Reminder:", reminder)

