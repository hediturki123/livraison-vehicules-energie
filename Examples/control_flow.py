'''
Control flow examples.

@author: Vassilissa Lehoux
'''

def if_statments(x):
    """
    Sequence
    if - elif - elif - ... - elif - else
    can replace "switch" or "case" that you have in other languages  
    """
    if x == 0:  # parentheses are optional
        print("x is null")
    elif x < 0:
        print("x is negative")
    else:
        print("x is positive")


def while_statement():
    """
    Iterates until a condition is met
    """
    b = 10
    a = 0
    while(a < b):
        print(a)
        a += 1
    print(a)

    # getting out of the loop with break
    a = 0
    while(True):
        print(a)
        a += 1
        if a == 10:
            break
    print(a)


def for_statement():
    """
    Iterates over a sequence of elements
    """
    print("for examples")
    # over a list
    print("list")
    my_list = [2.25, 6, "other"]
    for elem in my_list:
        print(elem)

    # over a list with a step index
    print("enumerate")
    for ind, elem in enumerate(my_list):
        print("step", ind, "elem", elem)
    
    # over a dictionary
    print("dictionary")
    my_dict = {"key1": "value1", "key2": "value2"}
    for key, val in my_dict.items():
        print("key", key, "val", val)

    # over a generator
    print("range")
    for ind in range(10):
        print("ind", ind)

    # over a reverse range
    print("reverse range")
    for ind in range(10, -1, -1):
        print("ind", ind)

    # getting out of the loop with break
    for ind in range(10):
        print("ind", ind)
        if ind == 10:
            break


def do_nothing():
    """
    This function does nothing.
    Usually place holder (to implement later) or interface definition
    """
    pass

if __name__ == '__main__':
    if_statments(6)
    do_nothing()
    for_statement()
    while_statement()
