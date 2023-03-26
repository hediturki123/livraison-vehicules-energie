'''
Some basic examples of function definition and parameter settings

@author: Vassilissa Lehoux
'''

def optional_args(end_val, beg_val=0, prefix=""):
    """
    Function with 3 arguments.
    First one is mandatory, the others are optional.
    If not provided, default value is used.
    If you respect the parameter order, you can call the function without the parameter's name.
    If not, you need to pass key=val arguments (see example below)
    """
    for ind in range(beg_val, end_val):
        print(prefix, ind)


def with_return():
    return 4


def shared_default_arg(val, default_list=[]):
    """
    Warning: default parameter is shared between the calls
    """
    default_list.append(val)
    return default_list


def lambda_functions():
    """
    Creating small anonymous functions can be done 
    using lambdas.
    They can be passed as parameters.
    """
    points_2d = [(2.0, 0.0), (0.0, 1.5), (3.4, 1.0), (-1.0, 4.0)]
    points_2d.sort(key=lambda point: point[0])  # sort the points by the first coordinate
    print(points_2d)

    def translate(val):
        return lambda point: (point[0] + val, point[1])

    trans3 = translate(3)
    print("Translate the x coordinate of the points of 3 on the right", [trans3(point) for point in points_2d])

    trans5 = lambda point: (point[0] + 5, point[1])
    print("Translate the x coordinate of the points of 3 on the right", [trans5(point) for point in points_2d])


if __name__ == '__main__':

    print("only one of the optional args")
    optional_args(10, prefix="prefix")

    print("first optional arg")
    optional_args(10, 3)

    print("function with return", with_return())

    print("Shared value between the calls")
    print(shared_default_arg(1))
    print(shared_default_arg(20))
    print(shared_default_arg(42))

    lambda_functions()
