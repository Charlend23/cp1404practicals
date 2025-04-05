from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return (f"{self.name}, fuel={self.fuel}, odo={self._odometer}, "
                f"{self.current_fare_distance}km on current fare, "
                f"{self.price_per_km}/km plus flagfall of {self.flagfall}")

    def get_fare(self):
        return super().get_fare() + self.flagfall