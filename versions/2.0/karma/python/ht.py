

def ht_offer_uri(url):
	"""Return the URI to use for the offer associated with the ad URL."""
	return "offer/"+get_url_hash(url)+"/processed"

def ht_offer_version_uri(url, timestamp):
	"""Return the URI of an offer version associated with a particular ad."""
	return "offer/"+get_url_hash(url)+"/"+timestamp+"/processed"

def ht_offer_place_uri(offer_uri):
	"The URI of a availableAtOrFrom place of an offer"
	return offer_uri+"/availableAtOrFrom"
