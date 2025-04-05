class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_format = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_format})"

    def add(self, new_musicians):
        self.musicians.append(new_musicians)

    def play(self):
        return "\n".join([musicians.play() for musicians in self.musicians])