def montana_getEnhancedLocation(location):
    """Add Montana to the location if not there already."""
    loc = location.strip()

    if loc == '':
        return ''

    if "montana" in loc.lower():
        return loc
    else:
        return loc + ", Montana"


def montana_cleanPrice(price):
    price = price.replace("$","")
    price = price.strip()
    return price

def montana_getCurrency(price):
    """Return the appropriate currency for a price."""
    if price == '':
        return ''

    if "$" in price:
        return 'USD'

    #add sophistication
    return 'USD'
