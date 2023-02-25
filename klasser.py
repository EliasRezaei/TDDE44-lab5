#!/usr/bin/python3
"""TDDE44 laboration 5."""
import math


class Pet(object):
    """En klass för att beskriva husdjur."""

    def __init__(self, name):
        """Definera instansvariabler."""
        self.name = name
        self.kind = ""
        self.toys = []

    def add_toys(self, toy):
        """Lägger till leksak om det inte finns med."""
        if toy not in self.toys:
            self.toys.append(toy)

    def __str__(self):
        """Lägger till kommmentare till instanserna."""
        resp1 = "{} är en {} som har inga leksaker"
        resp2 = "{} är en {} som har föjande leksaker: {} "
        if self.toys == []:
            return resp1.format(self.name, self.kind)
        else:
            return resp2.format(self.name, self.kind, ", ".join(self.toys))


class Vector2D(object):
    """En klass som skapar 2D vecter."""

    def __init__(self, xin, yin):
        """Definera instansvariaber .x och .y."""
        self.x = xin
        self.y = yin

    def get_length(self):
        """Längden på vectorn."""
        return(math.sqrt((math.pow(self.x, 2))+(math.pow(self.y, 2))))

    def add(self, vect):
        """Summary.

        Addera komponenterna (x och y) från vectorn
        vect till instansens egna vectkomponenter
        """
        self.x += vect.x
        self.y += vect.y
        return self.x, self.y

    def add_to_new(self, vect):
        """Summary.

        Nya instanse av Vector2D som är representation av den
        vector som fås då vect adderas, retuneras
        """
        nyvect = Vector2D(self.x + vect.x, self.y + vect.y)
        return nyvect

    def is_longer_than(self, vect):  # v1 from uppg2 stoppas in i vect
        """get_length undersökas och retunera True eller False."""
        return vect.get_length() < self.get_length()

    def create_unit_vector(self):
        """Skapar enhetsvectn."""
        enhet = Vector2D((self.x/self.get_length()),
                         (self.y/self.get_length()))
        x = 0
        return enhet

    def __str__(self):
        """Strängrepresentation av vect2D-instansen."""
        Txt = "vect med följande koordinater {}, {}"
        return Txt.format(self.x, self.y)
