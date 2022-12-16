class StringFoo():
    def __init__(self):
        self.mot = str("g string")

    def set_string(self, string):
        self.mot = string

    def print_string(self):
        print(self.mot.upper())

StringFoo().print_string()