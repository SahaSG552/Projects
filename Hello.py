from dataclasses import dataclass
from collections import namedtuple


@dataclass
class Position:
    name: str
    x: float
    y: float


city = Position("Norge", 25.3, 46.5)

print(city)
print(city.name)
print(city.x)
print(city.y)

NamedTuplePosition = namedtuple("NamedTuplePosition", ["name", "x", "y"])
city1 = NamedTuplePosition("Norge", 25.3, 46.5)
print(city1)
print(city1.name)
print(city1.x)
print(city1.y)
