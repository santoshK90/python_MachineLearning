'''
https://www.analyticsvidhya.com/blog/2024/01/exception-handling-in-python/

https://www.linkedin.com/pulse/custom-exceptions-learn-how-create-your-handle-errors-h-s-karthik/


Basic exceptions in python :


SyntaxError:
Raised when there is a syntax error in the code, indicating a mistake in the program’s structure.

# Example SyntaxError
print("Hello World"  # Missing closing parenthesis


---------------------------------------------------

IndentationError:
Raised when there is an issue with the indentation of the code. Python relies on proper indentation to define blocks of code.

# Example IndentationError
if True:
print("Indented incorrectly")  # Missing indentation

---------------------------------------------------


TypeError:
Raised when an operation or function is applied to an object of an inappropriate type.

# Example TypeError
num = "5"
result = num + 2  # Trying to concatenate a string with an integer

----------------------------------------------------

ValueError:
Raised when a built-in operation or function receives an argument with the correct type but an inappropriate value.

# Example ValueError
num = int("abc")  # Attempting to convert a non-numeric string to an integer

-----------------------------------------------------

NameError:
Raised when an identifier (variable or function name) is not found in the local or global namespace.

# Example NameError
print(undefined_variable)  # Variable is not defined

------------------------------------------------------

IndexError:
Raised when trying to access an index that is outside the bounds of a sequence (e.g., list, tuple, string).

# Example IndexError
my_list = [1, 2, 3]
print(my_list[5])  # Accessing an index that doesn't exist

-------------------------------------------------------

KeyError:
Raised when trying to access a dictionary key that does not exist.

# Example KeyError
my_dict = {"name": "John", "age": 25}
print(my_dict["gender"])  # Accessing a key that is not in the dictionary

--------------------------------------------------------

FileNotFoundError:
Raised when attempting to open a file that does not exist.

# Example FileNotFoundError
with open("nonexistent_file.txt", "r") as file:
    content = file.read()  # Trying to read from a nonexistent file

---------------------------------------------------------
'''

# a ZeroDivisionError is caught, preventing the program from crashing.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Error: {e}")




# Handling Multiple Exceptions
# Python allows handling multiple exceptions in a single try-except block.
try:
    # Code that may raise different exceptions
    result = int("text")
except (ValueError, TypeError) as e:
    # Handle both Value and Type errors
    print(f"Error: {e}")


# Finally Block
# The finally block is executed whether an exception occurs or not. It is commonly used for cleanup operations.
try:
    # Code that may raise an exception
    result = open("file.txt", "r").read()
except FileNotFoundError as e:
    # Handle file not found error
    print(f"Error: {e}")
finally:
    # Cleanup operations, e.g., closing files or releasing resources
    print("Execution complete.")



''' custom exception

Why Custom Exceptions?
Custom exceptions are an essential tool in your programming arsenal because they allow you to:
Provide Context: Custom exceptions can convey specific information about the error, making it easier to debug and troubleshoot issues.
Centralize Error Handling Logic: By defining your custom exceptions, you can centralize the error-handling logic, making your codebase more maintainable and consistent.
Enhance Readability: Well-named custom exceptions improve code readability by clearly indicating the type of error being raised.
Let's dive into creating custom exceptions with practical examples.

'''

class CustomError(Exception): 
    def __init__(self, message): 
        super().__init__(message)


def divide(a, b): 
    if b == 0: 
        raise CustomError("Division by zero is not allowed.") 
    return a / b 

try: 
    result = divide(10, 0) 
except CustomError as e: 
    print(f"Error: {e}")


try: 
    result = divide(10, 0) 
except CustomError as e: 
    print(f"Error: {e}") 
except Exception as e: 
    print(f"An unexpected error occurred: {e}")






## File Handling with Custom Exceptions
class FileProcessingError(Exception):
    def __init__(self, filename, message):
        self.filename = filename
        self.message = message
        super().__init__(f"Error processing file '{filename}': {message}")

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            # Process the file data here
            pass
    except FileNotFoundError:
        raise FileProcessingError(filename, "File not found.")
    except PermissionError:
        raise FileProcessingError(filename, "Permission denied.")
    except Exception as e:
        raise FileProcessingError(filename, f"An unexpected error occurred: {str(e)}")

try:
    process_file("nonexistent.txt")
except FileProcessingError as e:
    print(f"File processing error: {e}")



##Custom Business Logic Exception
class InsufficientBalanceError(Exception):
    def __init__(self, account_id, required_amount, balance):
        self.account_id = account_id
        self.required_amount = required_amount
        self.balance = balance
        super().__init__(f"Insufficient balance in account {account_id}. Required: ${required_amount}, Available: ${balance}")

class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.account_id, amount, self.balance)
        else:
            self.balance -= amount

try:
    account = BankAccount("12345", 1000)
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print(f"Error: {e}")
