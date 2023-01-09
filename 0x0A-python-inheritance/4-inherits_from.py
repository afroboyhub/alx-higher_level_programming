#!/usr/bin/python3

def inherits_from(obj, a_class):
    """inherits_from: returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj: object
        a_class: class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False