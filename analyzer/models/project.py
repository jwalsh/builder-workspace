class Project:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.description}"
