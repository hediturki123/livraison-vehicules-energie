'''
Basics examples of exceptions

@author: Vassilissa Lehoux
'''


def raising_exception(param1):
    """
    Function that raises an exception
    """
    if param1 < 0:
        raise ValueError("Invalid input", param1) 
    print("OK")


def catching_exceptions(val):
    """
    When exceptions are raised, you need to catch them or
    they will stop the execution of your program.
    To do that, write the code that can raise and exception in a "try" block.
    Then catch (one or several) exceptions with "except".
    """
    try:
        return 30 / val
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except TypeError:
        print("You should divide by a number")


if __name__ == '__main__':
    
    catching_exceptions(0)
    catching_exceptions(" a string")
    
    
    print("Raising an uncatched exception")
    raising_exception(-1)
