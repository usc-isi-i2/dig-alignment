from collections import defaultdict
import re
import hashlib

#from util import numericOnly, alphaOnly

# for JSON, there would be 
# six distinguished attributes:
#
# for database, we don't have to worry about this

# no binning

# def nearest5(x):
#   return 5*(int(2.5 + x)/5)

# def nearest2(x):
#   return 2*(int(1 + x)/2)

# phone
# phone2    810

def clean_phone(x):
    """Return the phone as a 10 digit number,
     or as close to that as we can make it.
     Prefix with country code '+1' at the end.
    """
    ph = numericOnly(x.strip().lower())
    # If there are 11 numbers 
    if (len(ph)==11 and ph[0]=="1"):
        ph = ph[1:]
    return '+1-' + ph;

def phone_uri(x):
    """Return the puri for a phone
    as countrycode-phone
    Do not return uri if countrycode is not present
    """
    x = x.strip().lower()
    ph = numericOnly(x)
    final = ''
	
    # If there are 11 numbers 
    if (len(ph)==11 and ph[0]=="1"):
        ph = ph[1:];
        final = 'phonenumber/1-' + ph;
    else:
    	dashIdx = x.find('-');
    	if(dashIdx != -1):
    		cc = numericOnly(x[0:dashIdx].strip());
    		ph = numericOnly(x[dashIdx+1].strip());
    		if(len(cc) > 0 and len(ph) > 0):
    			final = 'phonenumber/' + cc + '-' + ph
    return final

# age   15647
def clean_age(x):
    """Return the clean age
    """
    return x.strip().lower();

def feature_age(x):
    cleaned = clean_age(x)
    if cleaned:
        return "Age/%s" % cleaned

# email 7105
def clean_email(x):
    """Return a clean email address
    """
    if (x.find("@") != -1):
        em = x.strip().lower();
        return em;

def feature_email(x):
    cleaned = clean_email(x)
    if cleaned:
        return "EmailAddress/%s" % cleaned

# gender
def clean_gender(x):
    g = x.strip().lower();
    if g in ["female", "f"]:
        return "f"
    elif g in ["male", "m"]:
        return "m"
    else:
        return None

def feature_gender(x):
    cleaned = clean_gender(x)
    if cleaned:
        return "gender/%s" % cleaned

# rate
# rate60    12706
# rate30    10640
# rate15    1215
def clean_rate(x):
    r = x.strip().lower()
    if r[0] == "0":
        return None
    rate = int(float(r))
    if rate < 20 or rate > 1000:
        return None
    # return nearest5(rate)
    # no binning
    return rate

def clean_rate15(x):
    rate = clean_rate(x)
    if rate != None:
        rate = rate * 4
    return rate

def clean_rate30(x):
    rate = clean_rate(x)
    if rate != None:
        rate = rate * 2
    return rate

ethnicity_samples = ["black", "african-american", "latina", "ASIAN", "Martian"]
def feature_rate(x):
    cleaned = clean_rate(x)
    if cleaned:
        return "rate/%s" % cleaned
def test_ethnicity():
    for b in ethnicity_samples:
        f = feature_ethnicity(b)
        print "%r => %r" % (b, f)

# ethnicity 38587
def clean_ethnicity(x):
    stripped = x.strip().lower().replace(" ","")
    return stripped

def feature_ethnicity(x):
    cleaned = clean_ethnicity(x)
    if cleaned:
        return "Ethnicity/%s" % cleaned

# height    29135

height_samples = ["168", "5'6\"", "6'", "5'7\" - 5'9\""]
def test_height():
    for b in height_samples:
        f = feature_height(b)
        print "%r => %r" % (b, f)


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

def feature_height(x):
    cleaned = clean_height(x)
    if cleaned:
        return "height/%s" % cleaned

# hair  22078
def clean_hair(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_hair(x):
    cleaned = clean_hair(x)
    if cleaned:
        return "hair/%s" % cleaned

# build 21842
def clean_build(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_build(x):
    cleaned = clean_build(x)
    if cleaned:
        return "build/%s" % cleaned

# cup   19179
def clean_cup(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_cup(x):
    cleaned = clean_cup(x)
    if cleaned:
        return "cup/%s" % cleaned

# bust  18394
# bust  34-35
# bust  D
# bust  34&quot;
# bust  over
# bust  Perrrfct

bust_samples = ["34-35", "D", "34&quot;", '34"', "over", "Perrrfct", "34.5"]
def test_bust():
    for b in bust_samples:
        f = feature_bust(b)
        print "%r => %r" % (b, f)

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

def feature_bust(x):
    "Bust measured in inches"
    cleaned = clean_bust(x)
    if cleaned:
        return "bust/%s" % cleaned

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

def commaList(l):
    return ",".join(l)

def feature_piercings(x):
    cleaned = clean_piercings(x)
    if cleaned:
        return ",".join(["piercings/%s" % c for c in cleaned])

# creditcards   18272
def clean_creditcards(x):
    stripped = x.strip().lower()
    return stripped

def feature_creditcards(x):
    cleaned = clean_creditcards(x)
    if cleaned:
        return "creditcards/%s" % cleaned

# hairlength    18030
def clean_hairlength(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_hairlength(x):
    cleaned = clean_hairlength(x)
    if cleaned:
        return "hairlength/%s" % cleaned

# hairtype  17945
def clean_hairtype(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_hairtype(x):
    cleaned = clean_hairtype(x)
    if cleaned:
        return "hairtype/%s" % cleaned

# eyes  16723
def clean_eyes(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_eyes(x):
    cleaned = clean_eyes(x)
    if cleaned:
        return "eyes/%s" % cleaned

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

def feature_weight(x):
    """in kg
unmarked weight < 90 is interpreted as kg, >=90 as lb"""
    kg = clean_weight(x)
    if kg and kg >= 40 and kg <= 200:
        return "weight/" + str(kg)
    else:
        return None

# name  10042
def clean_name(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_name(x):
    cleaned = clean_name(x)
    if cleaned:
        return "PersonName/%s" % cleaned

# tattoos   8614
def clean_tattoos(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_tattoos(x):
    cleaned = clean_tattoos(x)
    if cleaned:
        return "tattoos/%s" % cleaned

# grooming  5709
def clean_grooming(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_grooming(x):
    cleaned = clean_grooming(x)
    if cleaned:
        return "grooming/%s" % cleaned

# implants  5469
def clean_implants(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_implants(x):
    cleaned = clean_implants(x)
    if cleaned:
        return "implants/%s" % cleaned

# username  5209
def clean_username(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_username(x):
    cleaned = clean_username(x)
    if cleaned:
        return "username/%s" % cleaned

# travel    4727
def clean_travel(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_travel(x):
    cleaned = clean_travel(x)
    if cleaned:
        return "travel/%s" % cleaned

# zip   2734
def clean_zip(x):
    stripped = x.strip().lower()
    return numericOnly(stripped)

def feature_zip(x):
    cleaned = clean_zip(x)
    if cleaned:
        return "zip/%s" % cleaned

# waist 2468
waist_samples = ["24 inches", "28\"", "70cm", "70 cm", "26.5", "svelte", "24-25"]
def test_waist():
    for b in waist_samples:
        f = feature_waist(b)
        print "%r => %r" % (b, f)


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


def feature_waist(x):
    """in cm
unmarked waist < 60 is interpreted as in, >=60 as cm"""
    cm = clean_waist(x)
    if cm and cm >= 40 and cm <= 200:
        return "waist/" + str(cm)
    else:
        return None

# hips  2400
def clean_hips(x):
    stripped = x.strip().lower()
    return numericOnly(stripped)

def feature_hips(x):
    cleaned = clean_hips(x)
    if cleaned:
        return "hips/%s" % cleaned

# alias 2049
def clean_alias(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_alias(x):
    cleaned = clean_alias(x)
    if cleaned:
        return "alias/%s" % cleaned

# availability  2049
availability_samples = ["Incall", "Outcall", "Incall Outcall"] 
def test_availability():
    for b in availability_samples:
        f = feature_availability(b)
        print "%r => %r" % (b, f)
def clean_availability(x):
    stripped = x.strip().lower()
    return alphaOnly(stripped)

def feature_availability(x):
    cleaned = clean_availability(x)
    if cleaned:
        return "availability/%s" % cleaned

# for stanford only
location_samples = ["Iowa", "New York", "arlington"]
def test_location():
    for b in location_samples:
        f = feature_location(b)
        print "%r => %r" % (b, f)
def clean_location(x):
    stripped = x.strip().lower()
    stripped = stripped.replace(" ","_")
    return alphaOnly(stripped)

def feature_location(x):
    cleaned = clean_location(x)
    if cleaned:
        return "location/%s" % cleaned


def get_url_hash(string):
    return hashlib.sha1(string).hexdigest().upper()

def getCacheBaseUrl():
    return "http://memex.zapto.org/data/"

def feature_address(city, state, country):
	return clean_address(city, state, country, ", ")

def clean_address(city, state, country, sep):
	city = clean_location(city)
	usep = ""
	addr = ""
	if city:
		addr = city
		usep = sep
	state = clean_location(state)
	if state:
		addr = addr + usep + state
		usep = sep
	country = clean_location(country)
	if country:
		addr = addr + usep + country
	return addr

def address_uri(city, state, country):
	addr = clean_address(city, state, country, "-")
	if len(addr) > 0:
		return "address/" + addr
	return ''

mapFunctions = defaultdict(lambda x: None)

mapFunctions['phone'] = clean_phone
mapFunctions['age'] = clean_age
mapFunctions['email'] = clean_email
mapFunctions['gender'] = clean_gender
mapFunctions['rate'] = clean_rate
mapFunctions['rate30'] = clean_rate30
mapFunctions['rate60'] = clean_rate
mapFunctions['ethnicity'] = clean_ethnicity
mapFunctions['height'] = clean_height
mapFunctions['hair'] = clean_hair
mapFunctions['build'] = clean_build
mapFunctions['cup'] = clean_cup
mapFunctions['bust'] = clean_bust
mapFunctions['piercings'] = lambda x: commaList(clean_piercings(x))
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
attribute_to_feature['zip'] = "zipcode"
attribute_to_feature['waist'] = "person_waistsize"
attribute_to_feature['hips'] = "person_hipstype"
attribute_to_feature['alias'] = "persion_alias"
attribute_to_feature['availability'] = "person_incalloutcall"
attribute_to_feature['location'] = "person_location"
attribute_to_feature['rate15'] = "rateperhour"
attribute_to_feature['rate30'] = "rateperhour"
attribute_to_feature['rate60'] = "rateperhour"


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
            return mod_time
        return ''
    except Exception, e:
        return ''
