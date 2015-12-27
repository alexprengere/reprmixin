# reprmixin

Automatic `repr` on your Python objects, with the classic namedtuple-like display.

Note that class attributes, class methods, static methods, instance methods and properties will not appear in the `repr`, only instance attributes.

```python
>>> from reprmixin import ReprMixin
>>>
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

```

