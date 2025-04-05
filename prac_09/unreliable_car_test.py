from unreliable_car import UnreliableCar

my_car = UnreliableCar("Spyder", 150, 30.5)
for test in range(100):
    print(my_car.drive(50))

