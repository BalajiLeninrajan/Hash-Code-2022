class Contributor:
    def __init__(self, name, skills, is_working) -> None:
        self.name : str = name
        self.skills : list[Skill] = skills
        self.is_working: bool = is_working

class Project:
    def __init__(self, name, skills, days, score, best_before, in_progress) -> None:
        self.name : str = name
        self.skills : list[Skill] = skills
        self.days : int = days
        self.score : int = score
        self.best_before : int = best_before
        self.in_progress : bool = in_progress
    
    def do_work(self):
        """
        Decrement days left till project completion
        """
        if self.days > 0:
            self.days -= 1

class Skill:
    def __init__(self, name, level) -> None:
        self.name : str = name
        self.level : int = level

class Work:
    def __init__(self, project, contributors, skill) -> None:
        self.project : Project = project
        self.contributors : list[Contributor] = contributors
        self.contributors_skills : list[Skill] = skill