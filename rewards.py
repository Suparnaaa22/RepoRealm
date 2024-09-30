class Rewards:
    def __init__(self):
        self.milestones = {5: "Bronze Star", 10: "Silver Star", 20: "Gold Star"}

    def check_rewards(self, habit):
        for milestone, reward in self.milestones.items():
            if habit.progress >= milestone:
                print(f"Congratulations! You've earned a {reward} for '{habit.name}'.")

