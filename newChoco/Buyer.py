class Buyer:
    def __init__(self, initialDollars, initialWraps=0, initialChocolates=0):
        self.dollars = initialDollars
        self.wraps = initialWraps + initialChocolates
        self.chocolates = initialChocolates

    def takeDollars(self, val):
        self.dollars -= val

    def takeWraps(self, val):
        self.wraps -= val

    def giveChocolate(self):
        self.chocolates += 1
        self.wraps += 1

    def __repr__(self):
        return f"Buyer currently has ${self.dollars}, {self.wraps} wrap(s) and {self.chocolates} chocolate(s)."

    def __add__(self, anotherBuyer):
        return Buyer(
            self.dollars + anotherBuyer.dollars,
            self.wraps + anotherBuyer.wraps,
            self.chocolates + anotherBuyer.chocolates,
        )

