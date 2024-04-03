#!/usr/bin/python3
def safe_print_integer(value):
    if value:
        try:
            if value * 1:
                print("{:d}".format(value))
                return True
        except ValueError:
            return False
        except TypeError:
            return False
    else:
        return False
