#!/usr/bin/env python3
"""Laboration 5 -- TDDE44.

Exempel på slumpmässig layout-funktion. Layout-funktionen skickas som
argument när en instans av lab5.LayoutTester skapas.
"""

# Läs denna fil för att se hur gränssnittet skapats.
import lab5
import random


def random_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares slumpmässigt.

    Argument:
    squares      -- Lista som innehåller tkinter.Label-objekt
    frame_height -- Höjden (int) på den Frame som fyrkanterna ligger i
    frame_width  -- Bredden (int) på den Frame som fyrkanterna ligger i
    """
    # Slumpa ut positioner för alla fyrkanter utan att de hamnar utanför frame.
    for square in squares:
        square_size = square.winfo_width()
        xpos = random.randint(10, frame_width - square_size)
        ypos = random.randint(10, frame_height - square_size)
        square.place(x=xpos, y=ypos)


def row_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares i ordning."""
    plats_x = 0
    plats_y = 0
    xpos = 0
    ypos = 0

    # Hittar rätt x respektiv y koordinat.
    for square in squares:
        square_size = square.winfo_width()
        xpos = plats_x
        ypos = plats_y

        # Hoppar ned en rad efter frame har tagit slut i x-riktning.
        if plats_x + square_size > frame_width:
            plats_y = plats_y + 2 * square.winfo_height()
            plats_x = 0
            xpos = 0
            ypos = plats_y
            # Stoppar programmet innan kvadraterna hamnar utanför i y-riktning.
            if ypos + square_size > frame_height:
                break
        square.place(x=xpos, y=ypos)
        plats_x = plats_x + 2 * square.winfo_width()


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(row_layout)
