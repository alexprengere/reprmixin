#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Easy repr, namedtuple-like.

>>> class CustomDescriptor(object):
...     def __get__(self, obj, _):
...         return obj.a
...     def __set__(self, obj, value):
...         obj.a = value

>>> class Titi(ReprMixin):
...     __slots__ = ['a', 'b', 'c']
...     clsvars = 'test'
...     def __init__(self, a, b):
...         self.a = a
...         self.b = b
...     def method(self):
...         return self.a
...     @property
...     def prop(self):
...         return self.b
...     @prop.setter
...     def prop(self, b):
...         self.b = b
...     custom_desc = CustomDescriptor()
...     @classmethod
...     def clsmethod(cls):
...         pass
...     @staticmethod
...     def static():
...         pass

>>> l = Titi(a=1, b='2')
>>> l.a
1
>>> l.b
'2'
>>> l.method()
1
>>> l.prop
'2'
>>> l.prop = 'g'
>>> l.prop
'g'
>>> l.custom_desc
1
>>> l.custom_desc = 2
>>> l.clsmethod()
>>> Titi.static()
>>> repr(l)
"Titi(a=2, b='g')"
"""

import inspect


def _find_attrs(obj):
    """Iterate over all attributes of objects."""
    visited = set()

    if hasattr(obj, '__dict__'):
        for attr in sorted(obj.__dict__):
            if attr not in visited:
                yield attr
                visited.add(attr)

    for cls in reversed(inspect.getmro(obj.__class__)):
        if hasattr(cls, '__slots__'):
            for attr in cls.__slots__:
                if hasattr(obj, attr):
                    if attr not in visited:
                        yield attr
                        visited.add(attr)


class ReprMixin(object):
    __slots__ = []

    def __repr__(self):
        return '{0}({1})'.format(
            self.__class__.__name__,
            ', '.join('{0}={1}'.format(attr, repr(getattr(self, attr)))
                      for attr in _find_attrs(self)
                      if not attr.startswith('_') and getattr(self, attr)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
