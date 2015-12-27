#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Easy repr, namedtuple-like.

>>> class Titi(ReprMixin):
...     clsvars = 'test'
...     def __init__(self, a, b):
...         self.a = a
...         self.b = b
...     def method(self):
...         return self.a
...     @property
...     def prop(self):
...         return self.b

>>> l = Titi(1, '2')
>>> l.a
1
>>> l.b
'2'
>>> l.method()
1
>>> l.prop
'2'
>>> repr(l)
"Titi(a=1, b='2')"
"""

def _iter_attributes(obj):
    """Iterate over all attributes on objects.
    """
    cls = obj.__class__
    for attr in dir(obj):
        # No private stuff
        if attr.startswith('_'):
            continue
        # No methods, no properties, no class level attributes
        if hasattr(cls, attr):
            if getattr(cls, attr).__class__.__name__ != 'member_descriptor':
                continue
        yield attr, repr(getattr(obj, attr))


class ReprMixin(object):
    __slots__ = []

    def __repr__(self):
        return '{0}({1})'.format(
            self.__class__.__name__,
            ', '.join('{0}={1}'.format(*t) for t in _iter_attributes(self)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

