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
    menu()
    user_input = input("Enter Choice: ").lower()
    while user_input != "q":
        if user_input == "l":
            print()
        elif user_input == "s":
            print()
        elif user_input == "d":
            print()
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

main()