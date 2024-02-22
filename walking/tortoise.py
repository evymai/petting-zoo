# import the python datetime module to help us create a timestamp
from datetime import date

class Tortoise:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True