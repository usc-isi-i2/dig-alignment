from collections import defaultdict
import re
import hashlib
from urllib import quote

#from util import numericOnly, alphaOnly
#from addresses import standardize_country
# for JSON, there would be 
# six distinguished attributes:
#
# for database, we don't have to worry about this

# no binning

# def nearest5(x):
#   return 5*(int(2.5 + x)/5)

# def nearest2(x):
#   return 2*(int(1 + x)/2)
USPhonePattern = re.compile(r"^\([0-9]{3}\) [0-9]{3}\-[0-9]{4}$")
def clean_phone(x):
    """Return the phone as a 10 digit number,
     or as close to that as we can make it.
     Prefix with country code '+1' at the end.
    """
    if (len(x)>0):
        x = x.strip().lower()
        cc = ''
        if x.find("+") == 0:
            end1 = x.find(" ")
            end2 = x.find("-")
            if end1 == -1: end1 = 10000
            if end2 == -1: end2 = 10000
            if end1 != 10000 or end2 != 10000:
                end = min(end1, end2)
                cc = x[1:end]
                ph = numericOnly(x[end+1:])
            else:
                testCC = detectCountryCode(x)
                if testCC:
                    cc = testCC
                    ccLen = len(cc)
                    ph = x[ccLen+1:]
                    ph = numericOnly(ph)
                else:
                    ph = numericOnly(x)
        else:
            valid = USPhonePattern.match(x)
            if valid:
                ph = valid.group()
                cc = "1"
                ph = numericOnly(ph)
            else:
               ph = numericOnly(x)

    	# If there are 11 numbers
    	if (len(ph)==11 and ph[0]=="1"):
            ph = ph[1:]
            cc = "1"

        if len(cc) > 0:
            ph = "+" + cc + "-" + ph
    	return ph;
    return ''

def phone_uri(x):
    """Return the uri for a phone
    as countrycode-phone
    Use 'x-' as country code if not present in the number
    """
    x = clean_phone(x)
    if len(x) > 0:
        dashIdx = x.find('-');
        if(dashIdx != -1):
            return "phonenumber/" + x[1:]
        return "phonenumber/x-" + x
    return ''

def phonenumber_uri(x):
	return phone_uri(x)

# age   15647
def clean_age(x):
    """Return the clean age
    """
    stripped = x.strip().lower()
    # take only first value of any range
    stripped = stripped.split('-')[0].strip()
    try:
        age = int(stripped)
        if age<1 or age>99:
            return None
    except:
        return None
    return age

def age_uri(x):
	cx = clean_age(x)
	if (cx>0):
		return "person_age/" + str(cx)
	return ''
	
def person_age_uri(x):
    if x:
        return "person_age/%s" % x
    return ''

# email 7105
def clean_email(x):
    """Return a clean email address
    """
    if (len(x)>0 and x.find("@") != -1):
        em = x.strip().lower()
        em = nonWhitespace(em)
        return em
    return ''

def emailaddress_uri(x):
    if x:
        return "emailaddress/%s" % x
    return ''

# gender
def clean_gender(x):
	if (len(x)>0):
	    g = x.strip().lower();
	    if g in ["female", "f"]:
	        return "f"
	    elif g in ["male", "m"]:
	        return "m"
	return ''

def person_gender_uri(cleaned):
    if cleaned:
        return "person_gender/%s" % cleaned
    return ''

# rate
# rate60    12706
# rate30    10640
# rate15    1215
def base_clean_rate(x):
    clean = x.strip().lower()
    if clean[0] == "0":
        return None

    rate = int(float(clean))
    if rate < 20 or rate > 1000:
        return None
    return rate

def clean_rate(x):
    rate = base_clean_rate(x)
    if rate != None:
    	return "%s-per-60min" % rate
    return ''

def clean_rate15(x):
    rate = base_clean_rate(x)
    # if rate != None:
    #     rate = rate * 4
    if rate != None:
    	return "%s-per-15min" % rate
    return ''

def clean_rate30(x):
    rate = base_clean_rate(x)
    # if rate != None:
    #     rate = rate * 2
    if rate != None:
    	return "%s-per-30min" % rate
    return ''

def rate_uri(cleaned):
    if cleaned:
        return "rate/%s" % cleaned

def rate_price(cleaned):
    if cleaned:
        idx = cleaned.find("-")
        if idx != -1:
            return int(cleaned[0:idx])
    return ''

def rate_duration(cleaned):
    if cleaned:
        idx = cleaned.find("per-")
        if idx != -1:
            str = cleaned[idx+4:]
            dur = str[0: len(str)-3]
            return dur
    return ''

def rate_unit(cleaned):
    if cleaned:
        idx = cleaned.find("min")
        if idx != -1:
            return "MIN"
        idx = cleaned.find("sec")
        if idx != -1:
            return "SEC"
        idx = cleaned.find("hr")
        if idx != -1:
            return "HUR"
    return ''

# ethnicity 38587
def clean_ethnicity(x):
    stripped = x.strip().lower().replace(" ","")
    return stripped

def person_ethnicity_uri(cleaned):
    if cleaned:
        return "person_ethnicity/%s" % cleaned


def clean_height(x):
    stripped = x.strip().lower()
    # take only first measurement of any range
    stripped = stripped.split('-')[0].strip()
    try:
        # First, 5'6" or 6' or 6'7
        dimensions = stripped.split("'")
        if len(dimensions) >= 2:
            feet = int(dimensions[0])
            try:
                inches = int(dimensions[1].strip('"'))
            except:
                # empty inches
                inches = 0
            # return nearest5(int(2.54 * (12 * feet) + inches))
            # no binning
            return int(2.54 * (12 * feet) + inches)
        else:
            # no inches, so try centimeters
            # Second, 137
            # return nearest5(int(stripped))
            # no binning
            return int(stripped)
    except:
        return None
    return None

def person_height_uri(cleaned):
    if cleaned:
        return "person_height/%s" % cleaned

# hair  22078
def clean_hair(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_haircolor_uri(cleaned):
    if cleaned:
        return "person_haircolor/%s" % cleaned

# build 21842
def clean_build(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_build_uri(cleaned):
    if cleaned:
        return "person_build/%s" % cleaned

# cup   19179
def clean_cup(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_cupsizeus_uri(cleaned):
    if cleaned:
        return "person_cupsizeus/%s" % cleaned

# bust  18394
# bust  34-35
# bust  D
# bust  34&quot;
# bust  over
# bust  Perrrfct

def clean_bust(x):
    """Bust measured in inches, restricted to [20,50]"""
    def sanityCheck(bust):
        if bust >= 20 and bust <= 50:
            return bust
        else:
            return None

    stripped = x.strip().lower()
    stripped = stripped.replace(" ","")
    first = re.split("-", stripped)[0]
    try:
        return sanityCheck(int(float(first)))
    except:
        pass
    try:
        return sanityCheck(int(numericOnly(first)))
    except:
        pass
    return None

def person_bustbandsize_uri(cleaned):
    "Bust measured in inches"
    if cleaned:
        return "person_bustbandsize/%s" % cleaned

# piercings 18294 
# None Belly Button Face
# xxxxx Other (where xxxx is a legal value)
# Tongue Breasts Belly Button Other
#
# Maybe use "belly button" "below the belt" as tokens, and then
# we should generate a comma-separated list of values and then
# use split values to generate a multi-valued cell so that we
# can generate multiple features per attribute.
def clean_piercings(x):
    stripped = x.strip().lower()
    stripped = re.sub("belly button", "bellybutton", stripped)
    stripped = re.sub("below the belt", "belowthebelt", stripped)
    return stripped.split(' ')

def pipeList(l):
    return "|".join(l)

def person_piercings_uri(cleaned):
    if cleaned:
        return "person_piercings/%s" % cleaned
    return ''

# creditcards   18272
def clean_creditcards(x):
    stripped = x.strip().lower()
    return stripped

def creditcardaccepted_uri(cleaned):
    cleaned = clean_creditcards(cleaned)
    if cleaned:
        return "creditcardaccepted/%s" % cleaned

# hairlength    18030
def clean_hairlength(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_hairlength_uri(cleaned):
    if cleaned:
        return "person_hairlength/%s" % cleaned

# hairtype  17945
def clean_hairtype(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_hairtype_uri(cleaned):
    if cleaned:
        return "person_hairtype/%s" % cleaned

# eyes  16723
def clean_eyes(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_eyecolor_uri(cleaned):
    if cleaned:
        return "person_eyecolor/%s" % cleaned

# weight    13316
def clean_weight(x):
    """In kg.
unmarked weight < 90 is interpreted as kg, >=90 as lb"""
    x = str(x).strip().lower()

    def lb_to_kg(lb):
        return int(float(lb)/2.2)
    def sanityCheck(kg):
        if kg >= 40 and kg <= 200:
            return kg
        else:
            return None

    try:
        cleaned = x

        # # first try for st/stone
        l = re.split("stone", cleaned)
        if len(l) == 1:
            l = re.split("st", cleaned)
        if len(l) > 1:
            stone = float(l[0])
            lb = l[1]
            lb = lb.strip('s')
            lb = lb.strip('lb')
            lb = lb.strip('pound')
            try:
                lb = float(lb)
            except ValueError, e:
                lb = 0
            # return sanityCheck(nearest2(lb_to_kg(int(stone*14+lb))))
            # no binning
            return sanityCheck(lb_to_kg(int(stone*14+lb)))
        lb = cleaned.strip('s')
        # now try for just pounds
        if lb.endswith("lb"):
            # return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('lb'))))))
            # no binning
            return sanityCheck(lb_to_kg(int(float(lb.strip('lb')))))
        if lb.endswith('pound'):
            # return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('pound'))))))
            # no binning
            return sanityCheck(lb_to_kg(int(float(lb.strip('pound')))))
        # now kg
        kg = cleaned.strip('s')
        if kg.endswith("kg"):
            # return sanityCheck(nearest2(int(float(kg.strip('kg')))))
            # no binning
            return sanityCheck(int(float(kg.strip('kg'))))
        if kg.endswith("kilo"):
            # return sanityCheck(nearest2(int(float(kg.strip('kilo')))))
            # no binning
            return sanityCheck(int(float(kg.strip('kilo'))))
        if kg.endswith('kilogram'):
            # return sanityCheck(nearest2(int(float(kg.strip('kilogram')))))
            # no binning
            return sanityCheck(int(float(kg.strip('kilogram'))))
        # now assume number sans unit
        num = int(float(cleaned))
        if num < 90:
            # assume kg
            # return sanityCheck(nearest2(num))
            # no binning
            return sanityCheck(num)
        else:
            # assume lb
            # return sanityCheck(nearest2(lb_to_kg(num)))
            # no binning
            return sanityCheck(lb_to_kg(num))

    except Exception, e:
        return None

def person_weight_uri(cleaned):
    if cleaned:
        return "person_weight/%s" % cleaned

# name  10042
def clean_name(x):
    x = toTitleCaseCleaned(x)
    if isSymbol(x[0:1]):
        return ''
    return x

def person_name_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "person_name/%s" % cleaned
    return ''


def author_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "author/%s" % cleaned
    return ''

# tattoos   8614
def clean_tattoos(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_tattoocount_uri(cleaned):
    if cleaned:
        return "person_tattoocount/%s" % cleaned

# grooming  5709
def clean_grooming(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_grooming_uri(cleaned):
    if cleaned:
        return "person_grooming/%s" % cleaned

# implants  5469
def clean_implants(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_implantspresent_uri(cleaned):
    if cleaned:
        return "person_implantspresent/%s" % cleaned

# username  5209
def clean_username(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_username_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "person_username/%s" % cleaned
    return ''

def person_blackhat_username_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "person_blackhat_username/%s" % cleaned
    return ''

# travel    4727
def clean_travel(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_travel_uri(cleaned):
    if cleaned:
        return "person_travel/%s" % cleaned

# waist 2468
# waist_samples = ["24 inches", "28\"", "70cm", "70 cm", "26.5", "svelte", "24-25"]

def clean_waist(x):
    "copied from bust"
    def inch_to_cm(inch):
        return int(inch*2.54)
    def sanityCheck(cm):
        if cm >= 40 and cm <= 200:
            return cm
        else:
            return None
    try:
        stripped = x.strip().lower()
        stripped = stripped.replace(" ","")
        first = re.split("-", stripped)[0]
        first = first.strip()
    except:
        pass

    try:
        cleaned = first
        inch = cleaned.strip('es')
        inch = inch.strip('s')
        # now try for just inches
        if inch.endswith("inch"):
            # return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('inch'))))))
            # no binning
            return sanityCheck(inch_to_cm(int(float(inch.strip('inch')))))
        if inch.endswith('in'):
            # return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('in'))))))
            # no binning
            return sanityCheck(inch_to_cm(int(float(inch.strip('in')))))
        if inch.endswith('"'):
            # return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('"'))))))
            # no binning
            return sanityCheck(inch_to_cm(int(float(inch.strip('"')))))
        # now cm
        cm = cleaned.strip('s')
        if cm.endswith("cm"):
            # return sanityCheck(nearest2(int(float(cm.strip('cm')))))
            # no binning
            return sanityCheck(int(float(cm.strip('cm'))))
        if cm.endswith('centimeter'):
            # return sanityCheck(nearest2(int(float(cm.strip('centimeter')))))
            # no binning
            return sanityCheck(int(float(cm.strip('centimeter'))))
        # now assume number sans unit
        num = int(float(cleaned))
        if num >= 60:
            # assume cm
            # return sanityCheck(nearest2(num))
            # no binning
            return sanityCheck(num)
        else:
            # assume inch
            # return sanityCheck(nearest2(inch_to_cm(num)))
            # no binning
            return sanityCheck(inch_to_cm(num))

    except Exception, e:
        return None


def person_waistsize_uri(cleaned):
    """in cm
unmarked waist < 60 is interpreted as in, >=60 as cm"""
    if cleaned:
        return "person_waistsize/" + str(cleaned)
    else:
        return None

# hips  2400
def clean_hips(x):
    stripped = x.strip().lower()
    return numericOnly(stripped)

def person_hipstype_uri(cleaned):
    if cleaned:
        return "person_hipstype/%s" % cleaned

# alias 2049
def clean_alias(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_alias_uri(cleaned):
    if cleaned:
        return "person_alias/%s" % cleaned

# availability  2049
#availability_samples = ["Incall", "Outcall", "Incall Outcall"]

def clean_availability(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def person_incalloutcall_uri(cleaned):
    if cleaned:
        return "person_incalloutcall/%s" % cleaned


def get_url_hash(string):
    return hashlib.sha1(string).hexdigest().upper()

def getCacheBaseUrl():
    return "http://memex.zapto.org/data/"

def getHTBaseUrl():
    return "http://dig.isi.edu/ht/data/"

# zip   2734
def clean_zip(x):
    stripped = x.strip().lower()
    return numericOnly(stripped)

def place_zipcode_uri(cleaned):
    if cleaned:
        return "place_zipcode/%s" % cleaned
# for stanford only
#location_samples = ["Iowa", "New York", "arlington"]

def clean_location(x):
    stripped = x.strip().lower()
    stripped = alphaNumeric(stripped).strip()
    return toTitleCaseCleaned(stripped)

def place_location_uri(cleaned):
    if cleaned:
        cleaned = cleaned.replace(" ","_").lower()
        return "place_location/%s" % cleaned

def feature_address(city, state, country):
	return clean_address(city, state, country, ", ")

def clean_city(city):
    return clean_location(city)

def clean_state(state, country):
    state = clean_location(state)
    if country:
        state = standardize_state_name(country, state)
    else:
        state_us = standardize_state_name("US", state)
        if len(state_us) > 0:
            state = state_us

    if len(state) == 2:
        state = state.upper() #upper case state code

    return state

def clean_country(country):
    country = clean_location(country)
    country = standardize_country_name(country)
    return country

def country_code(country):
    country = clean_location(country)
    country = standardize_country_code(country)
    return country

def clean_address(city, state, country, sep):
    city = clean_location(city)
    usep = ""
    addr = ""
    if city:
        addr = city
        usep = sep

    country = clean_location(country)
    country = standardize_country_name(country)

    state = clean_location(state)
    state = standardize_state_name(country, state)
    if state:
        addr = addr + usep + state
        usep = sep

    if country:
        addr = addr + usep + country
    return addr

def address_uri(city, state, country):
    addr = clean_address(city, state, country, "-").strip()
    if len(addr) > 0:
        addr = addr.replace(" ", "_").lower()
        return "address/" + addr
    return ''

def country_uri(country):
    country = clean_location(country)
    country = standardize_country_name(country)
    if country:
        cc = country.replace(" ", "_").lower()
        return "country/" + cc
    return ''

def clean_website(website):
    x = nonWhitespace(website)
    if x:
        return x.lower()
    return ''

def website_uri(website):
	if len(website) > 0:
		uri = quote(website, safe='')
		return "website/" + uri
	return ''

def gender_uri(gender):
	cg = clean_gender(gender)
	if (len(cg)>0):
		return "person_gender/" + cg
	return ''

def emailaddress_uri(email):
	c = clean_email(email)
	if (len(c) > 0):
		qc = quote(c, safe='')
		return "emailaddress/" + qc
	return ''

content_registeries = ["application", "audio", "example", "image",
                        "message", "model", "multipart", "text", "video"]

def clean_content_type(type):
    idx = type.find("/")
    if idx:
        reg = type[0:idx]
        if reg in content_registeries:
            return type
    return ''

def content_type_uri(cleaned):
    if cleaned:
        return "content_type/%s" % cleaned
    return ''

def clean_content_length(clen):
   return numericOnly(clen)

def content_length_uri(cleaned):
    if cleaned:
        return "content_length/%s" % cleaned
    return ''

def publication_year_uri(cleaned):
    if cleaned:
        return "publication_year/%s" % cleaned
    return ''

def clean_organization(org):
    x = toTitleCaseCleaned(org)
    if isSymbol(x[0:1]):
         return ''
    return x

def organization_name_uri(cleaned):
    if cleaned:
        for_uri = cleaned.replace(" ", "_").lower()
        return "organization/name/%s"  % for_uri
    return ''


mapFunctions = defaultdict(lambda x: None)

mapFunctions['phone'] = clean_phone
mapFunctions['age'] = clean_age
mapFunctions['email'] = clean_email
mapFunctions['gender'] = clean_gender
mapFunctions['rate'] = clean_rate
mapFunctions['rate15'] = clean_rate15
mapFunctions['rate30'] = clean_rate30
mapFunctions['rate60'] = clean_rate
mapFunctions['ethnicity'] = clean_ethnicity
mapFunctions['height'] = clean_height
mapFunctions['hair'] = clean_hair
mapFunctions['build'] = clean_build
mapFunctions['cup'] = clean_cup
mapFunctions['bust'] = clean_bust
mapFunctions['piercings'] = lambda x: pipeList(clean_piercings(x))
mapFunctions['creditcards'] = clean_creditcards
mapFunctions['hairlength'] = clean_hairlength
mapFunctions['hairtype'] = clean_hairtype
mapFunctions['eyes'] = clean_eyes
mapFunctions['weight'] = clean_weight
mapFunctions['name'] = clean_name
mapFunctions['tattoos'] = clean_tattoos
mapFunctions['grooming'] = clean_grooming
mapFunctions['implants'] = clean_implants
mapFunctions['username'] = clean_username
mapFunctions['travel'] = clean_travel
mapFunctions['zip'] = clean_zip
mapFunctions['waist'] = clean_waist
mapFunctions['hips'] = clean_hips
mapFunctions['alias'] = clean_alias
mapFunctions['availability'] = clean_availability
mapFunctions['location'] = clean_location

def feature_value(attributeName, value):
    try:
        ret = mapFunctions[attributeName](value)
        if ret == None:
            ret = ''
        return ret
    except Exception, e:
        return ''


uriFunction = defaultdict(lambda x: None)

uriFunction["phonenumber"] = phonenumber_uri
uriFunction["person_age"] = person_age_uri
uriFunction["emailaddress"] = emailaddress_uri
uriFunction["person_gender"] = person_gender_uri
uriFunction["person_ethnicity"] = person_ethnicity_uri
uriFunction["person_height"] = person_height_uri
uriFunction["person_haircolor"] = person_haircolor_uri
uriFunction["person_build"] = person_build_uri
uriFunction["person_cupsizeus"] = person_cupsizeus_uri
uriFunction["person_bustbandsize"] = person_bustbandsize_uri
uriFunction["person_piercings"] = person_piercings_uri
uriFunction["creditcardaccepted"] = creditcardaccepted_uri
uriFunction["person_hairlength"] = person_hairlength_uri
uriFunction["person_hairtype"] = person_hairtype_uri
uriFunction["person_eyecolor"] = person_eyecolor_uri
uriFunction["person_weight"] = person_weight_uri
uriFunction["person_name"] = person_name_uri
uriFunction["person_tattoocount"] = person_tattoocount_uri
uriFunction["person_grooming"] = person_grooming_uri
uriFunction["person_implantspresent"] = person_implantspresent_uri
uriFunction["person_username"] = person_username_uri
uriFunction["person_travel"] = person_travel_uri
uriFunction["place_zipcode"] = place_zipcode_uri
uriFunction["person_waistsize"] = person_waistsize_uri
uriFunction["person_hipstype"] = person_hipstype_uri
uriFunction["person_alias"] = person_alias_uri
uriFunction["person_incalloutcall"] = person_incalloutcall_uri
uriFunction["place_location"] = place_location_uri
uriFunction["rate"] = rate_uri

def feature_uri(cleanAttributeName, cleanValue):
    try:
        ret = uriFunction[cleanAttributeName](cleanValue)
        if ret == None:
            ret = ''
        return ret
    except Exception, e:
        return ''

def feature_value(attributeName, value):
    try:
        ret = mapFunctions[attributeName](value)
        if ret == None:
            ret = ''
        return ret
    except Exception, e:
        return ''

# Pedro
attribute_to_feature = {}
attribute_to_feature['phone'] = "phonenumber"
attribute_to_feature['age'] = "person_age"
attribute_to_feature['email'] = "emailaddress"
attribute_to_feature['gender'] = "person_gender"
attribute_to_feature['ethnicity'] = "person_ethnicity"
attribute_to_feature['height'] = "person_height"
attribute_to_feature['hair'] = "person_haircolor"
attribute_to_feature['build'] = "person_build"
attribute_to_feature['cup'] = "person_cupsizeus"
attribute_to_feature['bust'] = "person_bustbandsize"
attribute_to_feature['piercings'] = "person_piercings"
attribute_to_feature['creditcards'] = "creditcardaccepted"
attribute_to_feature['hairlength'] = "person_hairlength"
attribute_to_feature['hairtype'] = "person_hairtype"
attribute_to_feature['eyes'] = "person_eyecolor"
attribute_to_feature['weight'] = "person_weight"
attribute_to_feature['name'] = "person_name"
attribute_to_feature['tattoos'] = "person_tattoocount"
attribute_to_feature['grooming'] = "person_grooming"
attribute_to_feature['implants'] = "person_implantspresent"
attribute_to_feature['username'] = "person_username"
attribute_to_feature['travel'] = "person_travel"
attribute_to_feature['zip'] = "place_zipcode"
attribute_to_feature['waist'] = "person_waistsize"
attribute_to_feature['hips'] = "person_hipstype"
attribute_to_feature['alias'] = "person_alias"
attribute_to_feature['availability'] = "person_incalloutcall"
attribute_to_feature['location'] = "place_location"
attribute_to_feature['rate15'] = "rate"
attribute_to_feature['rate30'] = "rate"
attribute_to_feature['rate60'] = "rate"


def feature_name(attribute_name):
    """Note: this overrides a specific feature function"""    
    try:
        ret = attribute_to_feature[attribute_name]
        if ret == None:
            ret = ''
        return ret
    except Exception, e:
        return ''

def feature_mod_time(feature_name, feature_value, mod_time):
    try:
        if len(feature_value) > 0:
        	stripped = feature_value.strip()
        	if (len(stripped)>0):
        		return mod_time
        return ''
    except Exception, e:
        return ''
