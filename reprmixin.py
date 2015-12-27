#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Easy repr, namedtuple-like.

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
>>> l.clsmethod()
>>> Titi.static()
>>> repr(l)
"Titi(a=1, b='g')"
"""

def _iter_attributes(obj):
    """Iterate over all attributes on objects.
    """
    cls = obj.__class__
    for name in dir(obj):
        # If __slots__ had elements undefined at __init__, getattr will fail
        if not hasattr(obj, name):
            continue
        # No private stuff, feel free to comment or change this to "__"
        if name.startswith('_'):
            continue
        # No methods, no properties, no class level attributes
        if hasattr(cls, name):
            if getattr(cls, name).__class__.__name__ != 'member_descriptor':
                continue
        yield name, repr(getattr(obj, name))


class ReprMixin(object):
    __slots__ = []

    def __repr__(self):
        return '{0}({1})'.format(
            self.__class__.__name__,
            ', '.join('{0}={1}'.format(*t) for t in _iter_attributes(self)))

