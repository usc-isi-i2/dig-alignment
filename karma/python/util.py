def documentUrl(x):
	"Return the original document URL from the URL in the document version"
	i = x.find('churl')
	return 'http://'+x[x.find('/',i+6)+1:]