def buyChocolates(dollars):
    wraps = 0
    chocolates = 0

    dollarsPerChoc = 1
    wrapsPerChoc = 3

    chocolatesForDollars = dollars // dollarsPerChoc
    dollars = dollars % dollarsPerChoc
    wraps += chocolatesForDollars
    chocolates += chocolatesForDollars

    while wraps >= wrapsPerChoc:
        chocolatesForWraps = wraps // wrapsPerChoc
        wraps = wraps % wrapsPerChoc
        wraps += chocolatesForWraps
        chocolates += chocolatesForWraps

    return chocolates


print(buyChocolates(15))
