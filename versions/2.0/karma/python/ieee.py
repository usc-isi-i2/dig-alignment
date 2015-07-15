import re

def abstract_uri(abstract_id):
	""" generates abstract uri with id"""
	return "article/"+abstract_id

def article_uri_from_citation_url(citation_url):
	"""extract the article id from the citation_url"""
	list=re.findall('\d+',citation_url)
	for str in list:
		if(len(str)>5):
			return "article/"+str
