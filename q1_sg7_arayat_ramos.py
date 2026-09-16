class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, material, capacity):
        super().__init__(material)
        self.capacity = capacity


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Glass", 100),
            Beaker("Glass", 100),
            Beaker("Glass", 100),
            Beaker("Glass", 100),
            Beaker("Glass", 100)
        ]
