"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("G Wagon", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo_car = Car("Limo", 100)
    limo_car.add_fuel(20)
    print(f"{limo_car.name} has fuel: {limo_car.fuel}")
    limo_car.drive(115)
    print(limo_car)

    charlend_car = Car("Supra", 130)
    charlend_car.add_fuel(50)
    print(f"{charlend_car.name} has fuel: {charlend_car.fuel}")
    charlend_car.drive(175)
    print(charlend_car)

main()