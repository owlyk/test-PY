class Shop:
    def __init__(self, priceInDollars, priceInWraps):
        self.priceInDollars = priceInDollars
        self.priceInWraps = priceInWraps

    def __repr__(self):
        return f"Shop sells chocolates for ${self.priceInDollars} or {self.priceInWraps} wrap(s) a piece."
