class Entrepreneur:
    def __init__(self, **kwargs):
        self.habits = {
            "learning": False,
            # Have you engaged in daily learning?
            "tasks": False,
            # Are your top 3 tasks for the day completed?
            "network": False,
            # Did you connect with someone in your network today?
            "mindful": True,
            # Are you practising mindfulness or meditation?
            "exercise": True,
            # Did you engage in physical activity?
            "finance": False,
            # Was there a review of business finances today?
            "feedback": True,
            # Did you seek feedback on something?
            "focus": True,
            # Were there periods of focused, undistracted work?
            "skills": True,
            # Was time spent on skill development?
            "gratitude": True
            # Did you reflect on things they're grateful for?
        }

        # Allow users to customize habits during initialization
        for habit, value in kwargs.items():
            if habit in self.habits:
                self.habits[habit] = value

    def __getitem__(self, habit):
        return self.habits.get(habit, False)
    
    def __setitem__(self, habit, value):
        if habit in self.habits:
            self.habits[habit] = value

    def day_summary(self):
        return sum(self.habits.values())
    
    def toggle_habit(self, habit):
        self[habit] = not self[habit]


# Example usage:
Boss = Entrepreneur(learning=True, tasks=True, mindful=False)
Boss.toggle_habit("learning")
Boss.toggle_habit("mindful")
Boss["tasks"] = True

focus_level = "focus" if Boss["focus"] else "not focusing"
print(f"Boss is {focus_level} on his tasks")



