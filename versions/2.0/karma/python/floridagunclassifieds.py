import re

def cleanPrice(price):
	price = price.replace("$","")
	price = price.strip()
	return price

def getCurrency(price):
	if "$" in price:
		return 'USD'

	#add sophistication
	return 'USD'

def getEnhancedLocation(location):
	if "florida" in location.lower():
		return "florida"
	else:
		return location