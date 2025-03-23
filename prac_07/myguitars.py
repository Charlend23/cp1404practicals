from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, year, cost))
    for guitar in guitars:
        print(f"{guitar.name} is made in {guitar.year} and it cost ${guitar.cost}")

main()