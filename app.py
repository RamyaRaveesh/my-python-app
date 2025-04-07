#!/usr/bin/env python3
import time

# Function to add two numbers
def add(a, b):
    return a + b

# Main script execution
if __name__ == "__main__":
    print("Welcome Ramya!")
    print("Sum of 1 and 2 is:")
    print(add(1, 2))

    # Keep the process running indefinitely
    while True:
        print("Running...")  # This could be a status log or heart-beat message
        time.sleep(60)  # Sleep for 60 seconds before the next iteration
