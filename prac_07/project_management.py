"""
Project Management
Estimate : 60 Minutes
"""

from project import Project

FILENAME = "projects.txt"

def main():
    projects = []
    with open(FILENAME, "r") as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    for project in projects:
        print(f"{project.name} in {project.date} top {project.priority} ${project.cost} and {project.completion}%")

main()