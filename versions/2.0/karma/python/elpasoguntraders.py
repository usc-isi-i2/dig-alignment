

def cleanPrice(price):
    price = price.replace("$","")
    price = price.strip()
    return price

def getCurrency(price):
    if "$" in price:
        return 'USD'

    #add sophistication
    return 'USD'
