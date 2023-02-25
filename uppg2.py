#!/usr/bin/python3
"""TDDE44 laboration 5."""
from klasser import Vector2D
import random


x = random.uniform(1, 100)
y = random.uniform(1, 100)
v1 = Vector2D(x, y)

x = random.uniform(1, 100)
y = random.uniform(1, 100)
v2 = Vector2D(x, y)

print("\n")
print(" Metod: get_length:", v1)
print("längden på vår vektor är: ", v1.get_length(), "\n")

print("Metod: add:", v2, " och", v1, "addereras :")
print("Nya värdet på vår koordinater är: ",
      v2.add(v1), "\n")  # v2 är self.x och self.y

print("Metod: add_to_new:", v2, "och", v1, "adderas till en ny vektor")
print("Nya vektorn är: ", v2.add_to_new(v1), "\n")  # v2 är self.x och self.y

print("Metod: is_longer_than: ", v2, "och ", v1, "jämföras")
print("Svar: ", v1.is_longer_than(v2), "\n")

print("Metod: create_unit_vector", v1)
print("Enhetsvektorn är: ", v1.create_unit_vector(), "\n")

print("Metod: __str__  ")
print(v2.__str__())
