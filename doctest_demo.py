# def add(a, b):
#     """
#     >>> add(2, 3)
#     6
#     >>> add(100,200)
#     20000
#     """
#     return a * b


# python -m doctest -v doctest_demo.py

def double(values):
    """ double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    >>> double([])
    []
    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' ant 'NoneType'
    """
    return [2 * element for element in values]