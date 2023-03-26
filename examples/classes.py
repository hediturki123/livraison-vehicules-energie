'''
Classes basic example

@author: Vassilissa Lehoux
'''

class MyClass(object):
    '''
    classdocs
    '''
    class_var = "ex_class_var"  # attribute of the class, shared between instances

    def __init__(self, att1):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.attribute1 = att1  # attribute different for each instance
        self.attribute2 = list()

    def __str__(self):
        """
        custom object string representation
        """
        return "attr1 " + str(self.attribute1) + " attr2 " + str(self.attribute2)

    def a_function(self, new_elem):
        """
        You can define functions for the object (self)
        """
        self.attribute2.append(new_elem)
        
    @classmethod
    def a_class_function(cls):
        """
        method for a class
        """
        return cls.class_var
    
class ChildClass(MyClass):  # Python supports multiple base classes, no described here
    """
    A child class.
    """

    def __init__(self):
        '''
        Defining a constructor that calls the one
        of the parent class
        '''
        super().__init__(10)   # super().method_name can be used with any parent method
        self.attribute3 = "a string"
    
    @classmethod
    def from_list(cls, elem_list):
        """
        Defining an additional constructor as a class method
        """
        inst = cls()
        inst.attribute2 = elem_list
        return inst
    
    def a_function(self, new_elem):
        """
        You can redefined functions of the base class
        (otherwise, you can use them as they are)
        """
        if new_elem is None:
            self.attribute2.append(0)
        else:
            self.attribute2.append(new_elem)

    def __str__(self):
        """
        custom object string representation
        """
        return super().__str__() + " attr3 " + self.attribute3



if __name__ == '__main__':
    # object initialization
    an_instance = MyClass(3)
    a_child_instance = ChildClass()
    an_instance.a_function("str")
    # Setting an attribute
    a_child_instance.attribute1 = 25
    print("instance of parent class", an_instance)
    print("instance of child class", a_child_instance)
    print("class attribute", ChildClass.class_var, an_instance.class_var, a_child_instance.class_var)
    print("is instance of MyClass", a_child_instance, isinstance(a_child_instance, MyClass))
