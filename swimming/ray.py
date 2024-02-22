# import the python datetime module to help us create a timestamp
from datetime import date

class Ray:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True