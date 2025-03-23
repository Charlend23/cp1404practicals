class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name} in {self.date} top {self.priority} ${self.cost} and {self.completion}%"