#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            try:
                if int(my_list[i]):
                    print("{:d}".format(my_list[i]), end='')
                n += 1
            except ValueError:
                continue
            except TypeError:
                continue
            except IndexError:
                continue
        print()
        except IndexError:
            return list index out of range
    return n
