from simple_term_menu import TerminalMenu
from time import time
from files import *
from models import *


def main():
    # Set run limit
    max_days = 100

    # Tracks work status
    working: list[Work] = []
    work_done: list[Work] = []

    # Gets & stores input data
    contributors: list[Contributor]
    projects: list[Project]
    input_files = [
        "a_an_example",
        "b_better_start_small",
        "c_collaboration",
        "d_dense_schedule",
        "e_exceptional_skills",
        "f_find_great_mentors"
    ]
    file_index = TerminalMenu(input_files).show()
    contributors, projects = read(input_files[file_index])

    # Starts timer
    init_time = time()

    # Sort projects based on score
    sort_projects(projects)

    # Execute everyday
    for day in range(max_days):
        # Do work and check completion
        for work in working:
            work.project.do_work()
            if work.project.days == 0:
                work_done.append(work)
                for contributor in work.contributors:
                    contributor.is_working = False
                projects.remove(work.project)
                working.remove(work)

        # Assigns contributors to each project
        for project in projects:
            if not project.in_progress:
                possible_project = assign(project, contributors)
                if possible_project:
                    working.append(possible_project)

    # Writes output to ./output/filename
    # NOTE: does not create output folder if doesn't already exist
    write(input_files[file_index], work_done)

    # Returns start time to calculate time elapsed
    return init_time


def sort_projects(projects: list[Project]):
    """
    Sorts projects and updates scores
    """
    for i in range(len(projects)):
        # Simple bubble sort
        for j in range(len(projects) - i - 1):
            if projects[j].score - projects[i].best_before < projects[j + 1].score - projects[j + 1].best_before:
                projects[j], projects[j + 1] = projects[j + 1], projects[j]


def assign(project: Project, contributors: list[Contributor]):
    """
    Creates a temporary task and populates the skills required
    If all the skills are able to be fulfilled the task is returned
    Else returns false
    """

    # Creates temporary tasks
    possible_project: Work = Work(project, [], [])

    # Populates skills in task
    for project_skill in project.skills:
        # Interates trough contributors and appends when conditions are met
        # TODO: Sort contributors on highest skill total or similar metric
        for contributor in contributors:
            if (
                contributor not in possible_project.contributors
                and contributor.is_working == False
            ):
                for contributor_skill in contributor.skills:
                    if (
                       contributor_skill.name == project_skill.name
                       and contributor_skill.level >= project_skill.level
                       ):
                        possible_project.contributors.append(contributor)
                        possible_project.contributors_skills.append(
                            contributor_skill)

                        # Checks if all skills are satified and level ups contributor skills
                        if len(project.skills) == len(possible_project.contributors_skills):
                            project.in_progress = True
                            for i in range(len(possible_project.contributors)):
                                possible_project.contributors[i].is_working = True
                                if possible_project.contributors_skills[i].level <= project_skill.level:
                                    possible_project.contributors_skills[i].level += 1
                            return possible_project


if __name__ == "__main__":
    # Runs program and calculates time elapsed
    init_time = main()
    print("--- Time taken: {} seconds ---".format(time() - init_time))
