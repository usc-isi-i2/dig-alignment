def getEnhancedLocation(location):
    if "montana" in location.lower():
        return "montana"
    else:
        return location


def clean_phone(x):
    """Return the phone as a 10 digit number,
     or as close to that as we can make it.
     Prefix with country code '+1' at the end.
    """
    if (len(x)>0):
        x = x.strip().lower()
        cc = ''
        if x.find("+") == 0:
            end1 = x.find(" ")
            end2 = x.find("-")
            if end1 == -1: end1 = 10000
            if end2 == -1: end2 = 10000
            if end1 != 10000 or end2 != 10000:
                end = min(end1, end2)
                cc = x[1:end]
                ph = numericOnly(x[end+1:])
            else:
                testCC = detectCountryCode(x)
                if testCC:
                    cc = testCC
                    ccLen = len(cc)
                    ph = x[ccLen+1:]
                    ph = numericOnly(ph)
                else:
                    ph = numericOnly(x)
        else:
            valid = USPhonePattern.match(x)
            if valid:
                ph = valid.group()
                cc = "1"
                ph = numericOnly(ph)
            else:
               ph = numericOnly(x)

    	# If there are 11 numbers
    	if (len(ph)==11 and ph[0]=="1"):
            ph = ph[1:]
            cc = "1"

        if len(cc) > 0:
            ph = "+" + cc + "-" + ph
    	return ph;
    return ''

def cleanPrice(price):
    price = price.replace("$","")
    price = price.strip()
    return price

def getCurrency(price):
    """Return the appropriate currency for a price."""
    if price == '':
        return ''

    if "$" in price:
        return 'USD'

    #add sophistication
    return 'USD'
