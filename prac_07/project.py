class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, Started at: {self.date}, Priority at: {self.priority}, at the cost of: ${self.cost} and The completion rate is: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion >= 100