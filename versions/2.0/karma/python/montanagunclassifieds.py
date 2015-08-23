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
    return price_quantity_us_number(price)

def montana_getCurrency(price):
    return price_currency(price)
