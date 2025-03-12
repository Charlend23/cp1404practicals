from guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    input_guitar = input("Name: ").title()
    while input_guitar != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(input_guitar,guitar_year,guitar_cost))
        print(f"{input_guitar} ({guitar_year}) : ${guitar_cost} added.\n")
        input_guitar = input("Name: ").title()
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print(f"\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()