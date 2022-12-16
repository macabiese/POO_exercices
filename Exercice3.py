from math import *

class Cercle():
    def __init__(self):
        self.rayon = int(9)
        self.circonference = 2 * pi * self.rayon
        self.aire = pi * self.rayon ** 2

    def set_aire(self, aire):
        self.aire = aire

    def set_circonference(self, circonference):
        self.circonference = circonference

    def infos(self):
        print("Aire:", self.aire, "Circonference:", self.circonference)

Cercle().infos()