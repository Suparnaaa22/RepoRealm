class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.progress = 0

    def mark_done(self):
        self.progress += 1
