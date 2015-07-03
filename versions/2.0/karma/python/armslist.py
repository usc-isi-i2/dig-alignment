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


def al_clean_image_url(imgurl):
	#http://cdn2.armslist.com/sites/armslist/uploads/posts/2015/07/02/4479405_01_winchester_mod_94_big_bore_xtr_640.jpg
	if re.search(r'http[s]?://cdn.*armslist.com.*',imgurl):
		return imgurl

	return ''

def cbt_clean_image_url(imgurl):
	#http://cdn2.armslist.com/sites/armslist/uploads/posts/2015/07/02/4479405_01_winchester_mod_94_big_bore_xtr_640.jpg
	if re.search(r'http[s]?://.*carolinabargaintrader.net.*',imgurl):
		return imgurl

	return ''

def tge_clean_image_url(imgurl):
	#http://cdn2.armslist.com/sites/armslist/uploads/posts/2015/07/02/4479405_01_winchester_mod_94_big_bore_xtr_640.jpg
	if re.search(r'http[s]?://.*tennesseegunexchange.com/wp-content/uploads.*',imgurl):
		return imgurl

	return ''

