"""
Guitar
Estimate = 50 Minutes
"""
CURRENT_YEAR = 2025

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, year):
        return CURRENT_YEAR - year
