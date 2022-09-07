# args - arguments
# kwargs - keyword arguments

def _add(*args, **kwargs):

    _sum = 0
    n = len(args)
    if 'add' in kwargs:
        n = kwargs['add']

    for elem in args[:n]:
        _sum += elem

    if 'mul' in kwargs:
        _sum *= kwargs["mul"]

    return _sum


a = 2
b = 3

c = _add(a, b, 100, 55, 89, 1, 0.4, add=2, mul=5)
print(c)
