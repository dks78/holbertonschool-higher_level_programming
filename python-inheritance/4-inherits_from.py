#!/usr/bin/python3
def inherits_from(obj, a_class):
        if isinstance(obj,object) and issubclass(type(obj), a_class) and type(obj) != a_class:
            return True
        else:
            return False
