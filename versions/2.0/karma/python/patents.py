

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
    if patent_no:
        return 'patent/' + alphaNumeric(patent_no, '').upper()
    return ''

def clean_patent_number(patent_no):
    patent_no = patent_no.replace(",", "")
    if patent_no.startswith("D"):
        patent_no = patent_no[1:]
    if patent_no.isdigit():
        parent_no = patent_no.rjust(7, "0")
        if parent_no != '0000000':
            return 'D' + parent_no
    return ''

def pt_legal_action_uri(url):
    return "legalAction/" + hashlib.sha1(url.encode('utf-8')).hexdigest().upper()

def pt_get_court_state(court):
    if court:
        idx = court.find("D. ")
        if idx != -1:
            return court[idx+3:]
    return ''