

def us_getTextHash(manufacturer,model):
	"""The URI for an Offer in usbid"""
	text=manufacturer+model
	if text:
		return "offer/" + hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
	return ''


def as_getTextHash(manufacturer,model):
	"""The URI for an Offer in abacus select"""
	text=manufacturer+model
	if text:
		return "offer/" + hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
	return ''


def el_clean_model(model):
	"""Clean a model number from all junk that may be left over from extraction"""
	return asciiChars(model.strip())


def el_product_uri(model):
	"""The URI of a product based on the model.
	Assumes for now that model is an identifier so that if two parts have the 
	same model they are the same part."""
	return "product/" + el_clean_model(model).lower()


def el_clean_manufacturer(manufacturer):
	"""Try to create a cannonical name for a manufacturer."""
	return asciiChars(manufacturer.strip())


def el_manufacturer_uri(manufacturer):
	"""The URI for a manufacturer, with the hope that we can reduce across sources."""
	return "organization/" + alphaNumeric(el_clean_manufacturer(manufacturer).lower(),'')