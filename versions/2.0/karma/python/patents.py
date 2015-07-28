

def pt_creator_uri(first_name, last_name, city, state, country):
	"""URI of a person using the personal information provided."""
	str = alphaNumeric(first_name.strip(), '') + '_' + alphaNumeric(last_name.strip(), '') + '_' + alphaNumeric(city.strip(), '')+ '_' + alphaNumeric(state.strip(), '') + '_' + alphaNumeric(country.strip(), '')
	return 'person/' + str.lower()


def pt_organization_uri(name):
	"""URI of an orgnaizatioon based on the name.

	This is a simple implementation that could be made much more robust"""

	return 'organization/' + alphaNumeric(name.strip().lower(), '')


def pt_agent_country(country):
	"""Clean the country"""
	c = country.strip()
	
	if c.lower() == 'unknown':
		return ''

	return c


def orgname_clean(orgname):
	"""Clean the organization name removing junk

	This is a very preliminary implementation."""

	x = orgname.strip()
	x = re.sub('\&\#x\d\d\;', '', x)
	return x


def pt_patent_uri(patent_no):
	"""The URI for a patent based on its number"""
	return 'patent/' + alphaNumeric(patent_no, '').upper()