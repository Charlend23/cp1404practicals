from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(my_taxi)
my_taxi.drive(18)
taxi_fares = my_taxi.get_fare()
print(taxi_fares)

assert taxi_fares == 48.78, "Wrong Fare"