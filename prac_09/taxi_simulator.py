from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    total_bill = 0
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
        elif user_input == "d":
            print("d")
        else:
            "Invalid option"


main()