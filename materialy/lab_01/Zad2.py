class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"'{self.name}' must be of type {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        obj.__dict__[self.name] = value

class Person:
    age = Typed(int)
    name = Typed(str)

p = Person()

p.name = "Alice"
print(f"p.name = {p.name!r}  (str → OK)")

p.age = 30
print(f"p.age  = {p.age!r}  (int → OK)")

try:
    p.age = "trzydzieści"
except TypeError as e:
    print(f"p.age = 'trzydzieści'  → TypeError: {e}")

try:
    p.name = 123
except TypeError as e:
    print(f"p.name = 123           → TypeError: {e}")

print(p.__dict__)
