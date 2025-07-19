# daily_reminder.py
def main():
    # 1. Get user input (must match EXACTLY these prompts)
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # 2. Match case must be exactly like this
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Note: '{task}' is a medium priority task with a deadline. Try to complete it today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Schedule time for it this week.")
        
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task but has a deadline. Complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")

if __name__ == "__main__":
    main()