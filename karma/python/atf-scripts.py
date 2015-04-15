# Scripts for modeling ATF data.

def atf_article_uri(url, post_id):
	return get_url_hash(url)+"/"+post_id


def atf_date_created(date):
	"""Put the date in ISO format"""
	return date


def atf_joined_date(date):
	"""Put the date in ISO format"""
	return date


def signature_clean(text):
	"""Strip HTML"""
	return text


def atf_fc_uri(article_uri):
	"""URI of feature collection"""
	return article_uri+"/featurecollection"
