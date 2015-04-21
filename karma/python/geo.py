
def gn_place_uri(geonamesid,fcode,country,admin1,admin2,admin3,admin4):
    "Return URI of place from a geonames id"
    if fcode=="PCLI":
        return "geonames/place/Country/"+country
    elif fcode=="ADM1":
        return "geonames/place/State1stDiv/"+country+"_"+admin1
    elif fcode=="ADM2":
        return "geonames/place/CountyProvince2ndDiv/"+country+"_"+admin1+"_"+admin2
    elif fcode=="ADM3":
        return "geonames/place/Community3rdDiv/"+country+"_"+admin1+"_"+admin2+"_"+admin3
    elif fcode=="ADM4":
        return "geonames/place/SubCommunity4thDiv/"+country+"_"+admin1+"_"+admin2+"_"+admin3+"_"+admin4    
    return "geonames/place/"+geonamesid

def gn_place_spacetimevolume_uri(class_uri):
	"Return URI of SpaceTimeVolume for a class with Spacetimevolume"
 	return class_uri+"/SpaceTimeVolume"

def gn_place_identifier_uri(geonamesid):
    "Return URI of place from a geonames id"
    return "geonames/place/"+geonamesid+"/identifier"

def gn_name_uri(geonamesid,name):
    "Return URI of name for a place with geonames id"
    return "geonames/place/"+geonamesid+"/Name/"+name 

def gn_nametype(type):
    "Return Nametype of name"
    return "http://dig.isi.edu/gazetteer/data/SKOS/NameTypes/"+type

def gn_select_not_populated_or_administrative(fclass):
    "Return Nametype of name"
    return fclass!="P" and fclass!="A"


def gn_nametype_conditional(type,condition):
    "Return Nametype of name if condition is 1, used for alternamtenames which have flags for historic, colloquial,..."
    if condition == 1:
    	return "http://dig.isi.edu/gazetteer/data/SKOS/NameTypes/"+type
    return ''

def gn_countrycodeconcept_uri(country):
    "Return country code concept_uri of country taken from SKOS vocabulary http://eulersharp.sourceforge.net/2003/03swap/countries"
    return "http://eulersharp.sourceforge.net/2003/03swap/countries#"+country

def gn_languagecodeconcept_uri(language):
    "Return language code concept_uri of language taken from SKOS vocabulary http://eulersharp.sourceforge.net/2003/03swap/languages"
    if len(language) == 2:
    	return "http://eulersharp.sourceforge.net/2003/03swap/languages#"+language
    return ''

def gn_pointgeometry_uri(place_uri):
    "Return URI of PointGeometry for a place"
    return place_uri+"/PointGeometry"

def gn_country_uri(country):
    "Return URI for Place of class country"
    return "geonames/place/Country/"+country

def gn_geojson(lat,long):
    "Return geojson point representation"
    return """{"type": "Point","coordinates": ["""+lat+","+long+"]}"

def gn_State1stDiv_uri(country,admin1):
    "Return URI for Place of class State1stDiv"
    if admin1 == None or admin1 =='00':
		return ''
    return "geonames/place/State1stDiv/"+country+"_"+admin1

def gn_CountyProvince2ndDiv_uri(country,admin1,admin2):
    "Return URI for Place of class CountyProvince2ndDiv"
    if admin2 == '' or admin2 =='00':
		return ''
    return "geonames/place/CountyProvince2ndDiv/"+country+"_"+admin1+"_"+admin2


def gn_Community3rdDiv_uri(country,admin1,admin2,admin3):
    "Return URI for Place of class CountyProvince2ndDiv"
    if admin3 == '' or admin3 =='00':
        return ''
    return "geonames/place/CountyProvince2ndDiv/"+country+"_"+admin1+"_"+admin2+"_"+admin3

def gn_SubCommunity4thDiv_uri(country,admin1,admin2,admin3,admin4):
    "Return URI for Place of class CountyProvince2ndDiv"
    if admin4 == '' or admin4 =='00':
        return ''
    return "geonames/place/SubCommunity4thDiv/"+country+"_"+admin1+"_"+admin2+"_"+admin3+"_"+admin4

def fcode_to_class(fclass,fcode):
	"Compute the name of the class in the ontology from a geonames fcode"
	c = fclass_dictionary[fclass]
	if fclass=="P":
		return dgeo+c
	c = fcode_dictionary[fcode]
	if c == None:
		return ''
	return dgeo+c


# 
dgeo = "http://dig.isi.edu/ontology/dgeo/"
fcode_dictionary = {}
fcode_dictionary['PCLI'] = "Country"
fcode_dictionary['ADM1'] = "State1stDiv"
fcode_dictionary['ADM2'] = "CountyProvince2ndDiv"
fcode_dictionary['ADM3'] = "Community3rdDiv"
fcode_dictionary['ADM4'] = "SubCommunity4thDiv"

fclass_dictionary = {}
fclass_dictionary['P'] = "PopulatedPlace"
fclass_dictionary['A'] = "AdministrativeArea"