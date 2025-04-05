from taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness