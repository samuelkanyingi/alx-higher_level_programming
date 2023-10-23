#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as e:
        err = "Exception: {}".format(e)
        print(err, file=sys.stderr)
        return None
