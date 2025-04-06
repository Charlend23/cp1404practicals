from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """a body of code that will handle all of the program"""
    total_bill = 0
    current_taxi = None # set to none to make sure that the program doesnt crash if the user didnt choose the taxi yet
    taxi_list = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets Drive!")
    user_input = input("q)uit, c)hoose, d)rive\n>>> ").lower()
    while user_input != "q": #this loop will keep repeating unless the user enter "q" to quit the program
        if user_input == "c": #this part will show the list of taxis available and the specs
            counter = 0
            print("Taxi available:")
            for taxi in taxi_list:
                print(f"{counter} - {taxi}")
                counter += 1
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice >= len(taxi_list) or taxi_choice < 0:
                print("Invalid taxi choice")
            else:
                current_taxi = taxi_list[taxi_choice]
        elif user_input == "d": # this part will ask the user how far they will go with the taxi
            if current_taxi is None: # to make sure that the program dont crash when they driving before choosing the taxi
                print("You need to choose a taxi before you can drive")
            else:
                distance_input = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance_input)
                total_amount = current_taxi.get_fare()
                total_bill += total_amount
                print(f"Your {current_taxi.name} trip cost you ${total_amount:.2f}")
        else: # if the user enter any word outside the word option, this will ensure that the program does not crash
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        user_input = input("q)uit, c)hoose, d)rive\n>>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    counter = 0
    print("Taxi are now:")
    for taxi in taxi_list:
        print(f"{counter} - {taxi}")
        counter += 1

main()