from random import *

class Hero():
    def __init__(self, nom):
        self.pdv = randint(1, 10) + randint(1, 10)
        self.force_att = randint(1, 6)
        self.force_def = randint(1, 6)
        self.nom = nom

    def attaque(self):
        self.degats_att = randint(1, 6) + self.force_att

    def defense(self):
        self.degats_def = self.degats_att - self.force_def

    def est_vivant(self):
        if self.pdv < 0:
            return False

