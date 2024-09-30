import csv
from .habit import Habit

class HabitManager:
    def __init__(self, filename='data/habits.csv'):
        self.filename = filename
        self.habits = self.load_habits()

    def add_habit(self, name, frequency):
        habit = Habit(name, frequency)
        self.habits.append(habit)
        self.save_to_csv(habit)

    def save_to_csv(self, habit):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([habit.name, habit.frequency, habit.progress])

    def load_habits(self):
        habits = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    habit = Habit(row[0], row[1])
                    habit.progress = int(row[2])
                    habits.append(habit)
        except FileNotFoundError:
            pass
        return habits

    def get_habits(self):
        return self.habits
