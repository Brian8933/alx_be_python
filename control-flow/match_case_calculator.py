# match_case_calculator.py
# Simple calculator using match-case statements
 

def main():
    # Step 1: Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    #Step 2: perform calculatiom using match-case
    match operation:
        case "+":
            result = num1 + num2
            print (f"The result is {result}")
        case "-":
            resutl = num1 - num2
            print(f"The results is {result}")  
        case "*":
            result = num1 * num2
            print(f"The result is{result}") 
        case "/":
            if num2 == 0:
                print("cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is{result}")
        case _:
            print("Invalid operation. Please choose +, -, *, /")  

if __name__ == "__main__":
    main()                      
                