#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Attempt to divide
    except ZeroDivisionError:
        result = None  # If division by zero occurs, set result to None
    finally:
        print("Inside result: {}".format(result))  # Print the result inside the finally block
        return result  # Return the result (or None if error)
