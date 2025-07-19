# This script provides customized reminders for a task based on priority and time sensitivity

def main():
    # Step 1: Get user input
    task = input("Enter your task: ")
    Priority = input(" Priority (high/medium/low): ").lower()
    time_bound = input("Is it time bound? (yes/no): ").lower()

    # Step 2: Process the task using match-case for priority
    match Priority: 
        case "high": 
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires a immediate attentiontodaty!")
            else:
                print(f"\nReminder: '{task}' is a priority task. Please address it soon.")

        case "medium":
            if time_bound == "yes":
                print(f"\nNote: '{task}' is a medium priority task with a dealine. Try to complete it today.")
            else:
                print(f"\nNote '{task}' is a medium priority task. Schedule time for it this week")

        case "low":
            if time_bound == "yes":
                print(f"\nNote: '{task}' is a low priority task but has a deadline. Complete it when necessary.")
            else:
                print(f"\nNote: '{task}' is a low priority. task is consider. Consider completing it when you free time.")

        case _:
            print("\nInvalid priority level entered. Please use high, medium or low.")

if __name__ == "__main__":
    main()                                  
