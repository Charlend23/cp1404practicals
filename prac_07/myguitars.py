from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, year, cost))
    guitars.sort()
    for guitar in guitars:
        print(f"{guitar.name} is made in {guitar.year} and it cost ${guitar.cost}")
    guitar_name = input("Enter Guitar Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Enter Guitar Name: ")
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()