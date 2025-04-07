#!/usr/bin/env python3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to perform the calculation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main script execution
if __name__ == "__main__":
    logging.info("Welcome to the Calculator App!")
    
    while True:
        try:
            # Get user input for the calculation
            logging.info("Please enter the first number:")
            num1 = float(input("Enter the first number: "))

            logging.info("Please enter the operation (+, -, *, /):")
            operation = input("Enter operation (+, -, *, /): ").strip()

            logging.info("Please enter the second number:")
            num2 = float(input("Enter the second number: "))

            # Perform the calculation based on the user input
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                result = "Invalid operation!"

            # Print the result
            logging.info(f"The result of {num1} {operation} {num2} is: {result}")
            print(f"The result of {num1} {operation} {num2} is: {result}")
        
        except ValueError:
            logging.error("Invalid input! Please enter numeric values.")
            print("Invalid input! Please enter numeric values.")
        
        # Ask if the user wants to perform another calculation
        logging.info("Do you want to perform another calculation? (yes/no)")
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        
        if again != "yes":
            logging.info("Exiting the calculator app. Goodbye!")
            print("Goodbye!")
            break
