from dataclasses import dataclass, make_dataclass

Position = make_dataclass('Position', ['name', 'lon', 'lat'])

toshkent = Position('Toshkent', 66.9167, 24.7167)
samarqand = Position('Samarqand', 67.9167, 27.9167)
print(toshkent)
print(samarqand)
print(toshkent == samarqand)
# @dataclass
# class Position:
#     name: str
#     lon: float
#     lat: float

