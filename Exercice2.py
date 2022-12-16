class Rectangle():
    def __init__(self):
        self.longueur = int(input("L"))
        self.largeur = int(input("l"))
        self.aire = self.longueur * self.largeur

    def set_aire(self, aire):
        self.aire = aire

    def print_aire(self):
        print(self.aire)

Rectangle().print_aire()