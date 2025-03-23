"""
Project Management
Estimate : 60 Minutes
"""

from project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    menu()
    user_input = input("Enter Choice: ").lower()
    while user_input != "q":
        if user_input == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif user_input == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif user_input == "d":
            display_projects(projects)
        elif user_input == "f":
            print()
        elif user_input == "n":
            print()
        elif user_input == "u":
            print()
        else:
            print("Invalid choice.")
        menu()
        user_input = input("Enter Choice: ").lower()
    save_user_input = input("Do you want to save your projects before quitting? (y/n): ").lower()
    if save_user_input.lower() == 'y':
        print()
    print("Thank you")

def menu():
        return print("Menu:\n"
          "Load projects (l)\n"
          "Save projects (s)\n"
          "Display projects (d)\n"
          "Filter projects by date (f)\n"
          "Add new project (n)\n"
          "Update project (u)\n"
          "Quit (q)")

def load_projects(file):
    projects = []
    with open(file, "r") as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects

def save_projects(file, projects):
    with open(file, "w") as in_file:
        in_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            in_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    print("\nIncomplete Projects:")
    incomplete.sort()
    complete.sort()
    for project in incomplete:
        print(project)
    print("\nCompleted Projects:")
    for project in complete:
        print(project)

main()