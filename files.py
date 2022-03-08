from models import *

def read(filename : str):
    """
    Reads data from file and return contributors and projects
    """

    contributors : list[Contributor] = []
    projects : list[Project] = []

    f = open("./input/" + filename + ".in.txt", "r")
    # Number of contributors and projects
    C, P = [int(x) for x in f.readline().split(" ")]
    # Gets contributor skills
    for i in range(C):
        name, N = f.readline().split(" ")
        skills: list[Skill] = []
        for skill in range(int(N)):
            skill_name, level = f.readline().split(" ")
            skills.append(Skill(
                skill_name,
                int(level)
            ))
        contributors.append(Contributor(
            name,
            skills,
            False
        ))
    # Gets project skills
    for i in range(P):
        name, D, S, B, R = f.readline().split(" ")
        skills : list[Skill] = []
        for skill in range(int(R)):
            skill_name, level = f.readline().split(" ")
            skills.append(Skill(
                skill_name,
                int(level)
            ))
        projects.append(Project(
            name,
            skills,
            int(D),
            int(S),
            int(B),
            False
        ))
    f.close()
    return contributors, projects

def write(filename: str, work_done: list[Work]):
    """
    Writes data to filename-out.txt
    """
    f = open("./output/" + filename + ".out.txt", "w")
    f.write(str(len(work_done)) + "\n")
    for work in work_done:
        f.write(work.project.name + "\n")
        for contributor in work.contributors:
            f.write(contributor.name + " ")
        f.write("\n")
    print("--- Output file at " + f.name + " ---")
    f.close()