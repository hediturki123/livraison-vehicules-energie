'''
Basics examples of data structures

@author: Vassilissa Lehoux
'''


def tuple_ex1():
    """
    Creating t-uple
    """
    print("tuple_ex1", ("part1", 2, ["part3"]))


def tuple_ex2():
    """
    Accessing values of a t-uple
    """
    my_tuple = ("part1", 2, ["part3"])
    print("tuple_ex2", (my_tuple[0]))


def tuple_ex3():
    """
    Number of elements
    """
    my_tuple = ("part1", 2, ["part3"])
    print("tuple_ex2", len(my_tuple))


def list_ex1():
    """
    Creating and empty list and filling it
    """
    my_list = []
    my_list.append(1)
    my_list.extend([2, 3])
    print("list_ex1", my_list)


def list_ex2():
    """
    Creating a list of identical numbers
    """
    my_list = [0] * 5
    print("list_ex2", my_list)


def list_ex3():
    """
    Creating a list from an iterable (list comprehension)
    """
    my_list = [2 * val for val in range(5)]
    print("list_ex3", my_list)


def list_ex4():
    """
    Selecting parts of a list
    """
    my_list = [ind for ind in range(10)]
    print("list_ex4", my_list[3])
    print("list_ex4", my_list[2:])
    print("list_ex4", my_list[:4])
    print("list_ex4", my_list[5:-2])

def list_ex5():
    """
    Lists of lists
    """
    print("list_ex5", [[3 * ind1 + ind2 for ind2 in range(3)] for ind1 in range(5)])
    

def dict_ex1():
    """
    Creating an empty dictionary and filling it
    """
    my_dict = {}
    my_dict["key1"] = "val1"
    my_dict["key2"] = 2
    my_dict.update({"key3": 3, "key4": "val4"})
    print("dict_ex1", my_dict)


def dict_ex2():
    """
    Creating a dictionary from an iterable
    """
    my_dict = {ind: val for (ind, val) in enumerate(["val%i"%ind2 for ind2 in range(5)])}
    print("dict_ex2", my_dict)


def dict_ex3():
    """
    Keys and values
    """
    my_dict = {ind: val for (ind, val) in enumerate(["val%i"%ind2 for ind2 in range(10)])}
    print("dict_ex2", "keys", my_dict.keys(), "values", my_dict.values())



def string_ex1():
    """
    Concatenating strings 
    """
    print("string_ex1", "first " + "string")


def string_ex2():
    """
    Joining strings, here strings are separated with the ',' char
    """
    print("string_ex2", ",".join(["val%i" % ind for ind in range(6)]))


def string_ex3():
    """
    Splitting a string into a list
    """
    a_string = ":".join(["val%i" % ind for ind in range(6)])
    print("string_ex3", a_string.split(':'))


def generator_ex():
    """
    Each time next() is called on the generator object,
    it resumes execution after the last yield statement
    (or at the beginning if it is the first call)
    and returns data on "yield" statement
    """
    for a_char in "my string":
        yield a_char


if __name__ == '__main__':
    tuple_ex1()
    tuple_ex2()
    tuple_ex3()
    list_ex1()
    list_ex2()
    list_ex3()
    list_ex4()
    list_ex5()
    dict_ex1()
    dict_ex2()
    dict_ex3()
    string_ex1()
    string_ex2()
    string_ex3()
    print("generator example")
    for a_char in generator_ex():
        print(a_char)
