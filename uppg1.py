#!/usr/bin/python3
"""TDDE44 laboration 5."""
from klasser import Pet

pet1 = Pet("Fido")
pet1.kind = "Katt"
pet1.toys = ["nalle", "tygråtta", "Boll"]
pet1.add_toys("Fjäder")


pet2 = Pet("Pluto")
pet2.kind = "Hund"
pet2.toys = ["Something"]
pet2.add_toys("fjäder")


pet3 = Pet("Fisk")
pet3.kind = ("Fisk")


pet4 = Pet("Gollum")
pet4.kind = "Stoor Habbit"
pet4.toys = ["Ring"]

list = [pet1, pet2, pet3, pet4]
for pet in list:
    print(pet)
