from typing import NamedTuple


def check_type_wrong():
    Point = NamedTuple('Point', ('x', 'y'))
    p = Point(1, 2)

    if type(p) == tuple: # this will be false because it doesn't check for inheritance
        print('is tuple')
    else:
        print('not tuple')

def check_type_correct():
    Point = NamedTuple('Point', ('x', 'y'))
    p = Point(1, 2)

    if isinstance(p, tuple): # this will be true
        print('is tuple')
    else:
        print('not tuple')
