from datetime import datetime

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
    patent_id = alphaNumeric(patent_no, '').upper()

    if len(patent_id) == 8 and patent_id[0] == '0':
        patent_id = patent_id[1:]

    if patent_id:
        return 'patent/' + patent_id
    return ''

def clean_patent_number(patent_no):
    patent_no = patent_no.replace(",", "")
    if patent_no.startswith("D"):
        patent_no = patent_no[1:]
    if patent_no.isdigit():
        patent_no = patent_no.rjust(7, "0")
        if patent_no != '0000000':
            return 'D' + patent_no
    return ''

def pt_legal_action_uri(url):
    return "legalAction/" + hashlib.sha1(url.encode('utf-8')).hexdigest().upper()

def pt_get_court_state(court):
    if court:
        idx = court.find("D. ")
        if idx != -1:
            return court[idx+3:]
    return ''

def pt_format_date(input_date,in_format):
    format1 = "yyyymmdd"
    input_date = input_date.encode('UTF-8')
    if(in_format.replace(" ","").lower() == format1):
        out_date = datetime.strptime(input_date, "%Y%m%d")
        out_date.strftime('(%Y-%m-%d)')
        return str(out_date.date())
    format2 = "day,mmdd,yyyy"
    if(in_format.replace(" ","").lower() == format2):
        out_date = datetime.strptime(input_date, "%A, %B %d, %Y")
        out_date.strftime('(%Y-%m-%d)')
        return str(out_date.date())
    return ''

def attorney_uri(org_uri, person_name):
    """The URI for an attorney at a law firm"""
    return org_uri + uri_from_fields('/person/', person_name)

def party_from_title(title, index):
    """Helper function: Extract the plaintiff/defendant from the title of a court case"""
    parties = title.split(' v. ')
    
    if len(parties) == 2:
       return parties[index].strip()

    if len(parties) == 1:
        parties = title.split(' v ')  # No dot
        if len(parties) == 2:
            return parties[index].strip()

    return ''

def plaintiff_from_title(title):
    """Extract the plaintiff from the title of a court case"""
    return party_from_title(title, 0)

def defendant_from_title(title):
    """Extract the defendant from the title of a court case"""
    return party_from_title(title, 1)

def clean_legal_action_cause(cause):
    """Normalize the statement of the cause for a legal action."""
    return cause.strip()
