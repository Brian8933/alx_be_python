def main():
    task = input("Task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Please address it soon.")

        case "medium":
            if time_bound == "yes":
                print(f"\nNote: '{task}' is a medium priority task with a deadline. Try to complete it today.")
            else:
                print(f"\nNote: '{task}' is a medium priority task. Schedule time for it this week.")

        case "low":
            if time_bound == "yes":
                print(f"\nNote: '{task}' is a low priority task but has a deadline. Complete it when necessary.")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("\nInvalid priority level entered. Please use high, medium or low.")


if __name__ == "__main__":
    main()
