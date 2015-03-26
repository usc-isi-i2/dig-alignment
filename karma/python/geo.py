


def country_uri(country_code):
	return "country/" + country_code


def state_uri(country_code, state_code):
	return "state/"+country_code+"/"+state

def geonames_uri(geonames_id, gazetteer_name):
	return "/id/" + gazetteer_name + "/" + geonames_id
