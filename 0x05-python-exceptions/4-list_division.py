#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_length = max(len(my_list_1), len(my_list_2))
    n_list = []
    for i in range(list_length):
        try:
            z = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            z = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            z = 0
        except IndexError:
            print("out of range")
            z = 0
        finally:
            n_list.append(z)
    return n_list
