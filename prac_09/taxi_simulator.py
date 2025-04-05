from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    total_bill = 0
    current_taxi = None
    taxi_list = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets Drive!")
    user_input = input("q)uit, c)hoose, d)rive\n>>> ").lower()
    while user_input != "q":
        if user_input == "c":
            counter = 0
            print("Taxi available:")
            for taxi in taxi_list:
                print(f"{counter} - {taxi}")
                counter += 1
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(taxi_list):
                print("Invalid taxi choice")
            else:
                current_taxi = taxi_list[taxi_choice]
            print(f"Bill to date: ${total_bill:.2f}")
        elif user_input == "d":
            print("d")
        else:
            "Invalid option"
    print()

main()