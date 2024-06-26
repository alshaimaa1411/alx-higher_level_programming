#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as x:
        import sys
        print("Exception: {}".format(x), file=sys.stderr)
        return None
