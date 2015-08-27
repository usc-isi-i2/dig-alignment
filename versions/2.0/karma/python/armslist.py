import re

def cleanPrice(price):
	price = price.replace("$","")
	price = removeAlpha(price)
	price = price.strip()
	return price

def getCurrency(price):
	if "$" in price:
		return 'USD'
	if "BTC" in price or "btc" in price:
		return "BTC"
	if price.strip() == '':
		return ''

	#add sophistication
	return 'USD'

def getTransactionType(text):

	if text.lower().startswith("for sale"):
		return 'http://schema.org/Offer'
	elif text.lower().startswith("want to buy"):
		return 'http://schema.org/Demand'

	return ''

def getTransactionActor(transactionType):
	if transactionType == 'http://schema.org/Offer':
		return 'http://schema.org/seller'
	elif transactionType == 'http://schema.org/Demand':
		return 'http://schema.org/buyer'

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

def vw_clean_image_url(imgurl):
	#/images/VW%20Firears/Refurbished/Mosin%20%23151%201.JPG
	#http://velocityworks.net/images/VW%20Firears/Refurbished/Mosin%20%23151%203.JPG
	if re.search(r'^/images/(?!social_bookmarks).*$',imgurl):
		return 'http://velocityworks.net' + imgurl

	return ''

def price_uri(price):
	return "price/" + price.replace(",","")

def weapons_title_uri(title):
	return "title/" + title.replace(",","_").replace(" ", "_").replace("-","_").replace(".","_")
