def cleanPrice(price):
	price = price.replace("$","")
	price = price.strip()
	return price

def getCurrency(price):
	if "$" in price:
		return 'USD'

	#add sophistication
	return 'USD'

def getTransactionType(text):

	if text.lower().startswith("for sale"):
		return 'schema:Offer'
	elif text.lower().startswith("want to buy"):
		return 'schema:Demand'

	return ''

def getTransactionActor(transactionType):
	if transactionType == 'schema:Offer':
		return 'schema:seller'
	elif transactionType == 'schema:Demand':
		return 'schema:buyer'

	return ''

