# daily_reminder.py

# Step 1: Collect user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process using if-elif-else
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unknown priority level"

# Step 3: Add time sensitivity to the message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Step 4: Output the result
print("\nReminder:", reminder)
