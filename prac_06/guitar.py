"""
Guitar
Estimate = 50 Minutes
Actual = 55 Minutes
"""
CURRENT_YEAR = 2022
MIN_VINTAGE_YEAR = 50

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= MIN_VINTAGE_YEAR