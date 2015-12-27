# reprmixin

Automatic `repr` on your Python objects, with the classic namedtuple-like display.

Note that class attributes, class methods, static methods, instance methods and properties will not appear in the `repr`, only instance attributes. This also works whether `slots` are defined or not.

```python
>>> from reprmixin import ReprMixin
>>>
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

>>> l = Titi(1, '2')
>>> repr(l)
"Titi(a=1, b='2')"

```

