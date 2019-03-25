def buyChocolate(buyer, shop):
    if buyer.dollars >= shop.priceInDollars:
        buyer.takeDollars(shop.priceInDollars)
        buyer.giveChocolate()
        print("Bought a chocolate for wraps.")
    elif buyer.wraps >= shop.priceInWraps:
        buyer.takeWraps(shop.priceInWraps)
        buyer.giveChocolate()
        print("Bought a chocolate for wraps.")
    else:
        print("Buyer has insufficent funds.")
        return False

    return True


def allIn(buyer, shop):
    print(shop)
    print(buyer)

    while buyChocolate(buyer, shop):
        print(buyer)

    print()
    print("Buyer expended all his funds.")
    print(buyer)
