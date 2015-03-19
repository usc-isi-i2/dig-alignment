#!/usr/bin/python

import sys
from urlparse import urlparse

sources_by_id = {
                 1: "backpage",
                 2: "craigslist",
                 3: "classivox",
                 4: "myproviderguide",
                 5: "naughtyreviews",
                 6: "redbook",
                 7: "cityvibe",
                 8: "massagetroll",
                 9: "redbook_forum",
                 10: "cityxguide",
                 11: "cityxguideforum",
                 12: "rubads",
                 13: "anunico",
                 14: "sipsap",
                 15: "escortsincollege",
                 16: "escortphonelist",
                 17: "eroticmugshots",
                 18: "escortadsxxx",
                 19: "escortsinca",
                 20: "escortsintheus",
                 21: "liveescortreviews",
                 22: "myproviderguideforum",
                 23: "usasexguide",
                 24: "eroticreview",
                 25: "adultsearch",
                 26: "happymassage",
                 27: "utopiaguide",
                 28: "missingkids",
                 29: "alibaba",
                 30: "justlanded",
                 31: "gmdu",
                 32: "tradekey",
                 33: "manpowervacancy",
                 34: "gulfjobsbank",
                 35: "ec21"}


def clean(x):
    return str(x).replace(' ', '')

def marketid_to_market_tuple(source_columns, marketid):
    minfo = market_id_to_market_info.get(marketid, None)
    if not minfo:
        print >> sys.stderr, "Need to define a tuple for FAA/ICAO %s" % marketid
        return None
    else:
        locality = minfo[2]
        adm1 = minfo[1]
        country = minfo[0]
        return [source_columns] + minfo

### BACKPAGE



def backpage_url_to_sitekey(url):
    """http://longisland.backpage.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def determineMarketBackpage(url, title, city, state):
    return marketid_to_market_tuple("url",backpage_sitekey_to_marketid[backpage_url_to_sitekey(url)])

### CRAIGSLIST



def craigslist_url_to_sitekey(url):
    """http://longisland.craigslist.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def determineMarketCraigslist(url, title, city, state):
    return marketid_to_market_tuple("url", craigslist_sitekey_to_marketid[craigslist_url_to_sitekey(url)])

### CLASSIVOX



def classivox_url_to_sitekey(url):
    """http://longisland.classivox.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def determineMarketClassivox(url, title, city, state):
    return marketid_to_market_tuple("url", classivox_sitekey_to_marketid[classivox_url_to_sitekey(url)])

### MYPROVIDERGUIDE


def myproviderguide_url_to_sitekey(url):
    """http://longisland.myproviderguide.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    dirs = path.split('/')
    return dirs[2]

def determineMarketMyproviderguide(url, title, city, state):
    return marketid_to_market_tuple("url", myproviderguide_sitekey_to_marketid[myproviderguide_url_to_sitekey(url)])

### NAUGHTYREVIEWS


def process(url):
    bits = url.split('/')
    service = bits[3]
    if service in ["escorts", "companions"]:
        line = bits[-1]
        return processEscort(line)
    elif service in ["escort-agencies"]:
        line = bits[-1]
        return processAgency(line)
    elif service in ["na"]:
        print "N",
        line = bits[-1]
        return processEscort(line)
    elif service in ["massage-parlors"]:
        line = bits[-1]
        return processMassage(line)
    else:
        print "Didn't recognize service type %s" % service
        return 0

def lookupSitekey(terms):
    sk3 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-3:]))
    if sk3:
        return sk3
    sk2 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-2:]))
    if sk2:
        return sk2
    sk1 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-1:]))
    if sk1:
        return sk1
    return None

def isGenderMarker(t):
    return t in ["female", "woman", "male", "shemale", "tstvtg", "man", "couple", "female1"]

def isRaceEthnicMarker(t):
    return t in ["white", "black", "asian", "latin", "latino", "latina", "hispanic", "indian", "other", "european", "oriental", "russian", "mixed",""]

def isCompoundRaceEthnicMarker(t):
    return t in [["middle","eastern"]]

def trimNumericSuffix(terms):
    suffix = None
    try:
        i = int(terms[-1])
        suffix = terms[-1]
        terms.pop()
    except ValueError as e:
        pass
    return (suffix, terms)

def trimGenderMarker(terms):
    marker = None
    try:
        if isGenderMarker(terms[-1]):
            marker = terms[-1]
            terms.pop()
    except ValueError as e:
        pass
    return (marker, terms)
    
def trimRaceEthnicMarker(terms):
    marker = None
    try:
        if isCompoundRaceEthnicMarker(terms[-2:]):
            marker = "-".join(terms[-2:])
            terms.pop()
            terms.pop()
        elif isRaceEthnicMarker(terms[-1]):
            marker = terms[-1]
            terms.pop()
    except ValueError as e:
        pass
    return (marker, terms)

def processEscort(line):
    cands = 0
    try:
        terms = line.split('-')[1:]
        (suffix, terms) = trimNumericSuffix(terms)
        (gender, terms) = trimGenderMarker(terms)
        (raceEthnic, terms) = trimRaceEthnicMarker(terms)
        cands = lookupSitekey(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on escort %r: [%s]" % (line, e)
        return 0
    return cands

def processAgency(line):
    cands = 0
    try:
        terms = line.split('-')[1:]
        (suffix, terms) = trimNumericSuffix(terms)
        cands = lookupSitekey(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on agency %r: [%s]" % (line, e)
        return 0
    return cands

def processMassage(line):
    terms = line.split('-')[1:]
    return lookupSitekey(terms[-3:])

def naughtyreviews_url_to_marketid(url):
    """http://longisland.naughtyreviews.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    try:
        return process(url)
    except Exception as e:
        print >> sys.stderr, e
        return None

def determineMarketNaughtyreviews(url, title, city, state):
    marketid = naughtyreviews_url_to_marketid(url)
    if marketid:
        return marketid_to_market_tuple("url", marketid)
    else:
        return None

### Redbook

def determineMarketRedbook(url, title, city, state):
    pass

### CITYVIBE



def cityvibe_url_to_sitekey(url):
    """http://www.cityvibe.com/losangeles/PremiumEscorts/ariel-wla-gfe-incalloutcall/396104"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = path.split('/')[1]
    return sitekey

def determineMarketCityvibe(url, title, city, state):
    return marketid_to_market_tuple("url", cityvibe_sitekey_to_marketid[cityvibe_url_to_sitekey(url)])

def determineMarketRedbook_forum(url, title, city, state):
    pass

def determineMarketCityxguide(url, title, city, state):
    pass

def determineMarketCityxguideforum(url, title, city, state):
    pass

def determineMarketRubads(url, title, city, state):
    pass

def determineMarketAnunico(url, title, city, state):
    pass

def determineMarketSipsap(url, title, city, state):
    pass

### ESCORTSINCOLLEGE


def escortsincollege_title_to_sitekey(title):
    """202-277-7628 - Escort ad in Atlanta, Georgia | Visiting Visiting Visiting"""
    start = 28
    end = title.index('|')
    sitekey = title[start:end].strip()
    return sitekey

def determineMarketEscortsincollege(url, title, city, state):
    return marketid_to_market_tuple("title", escortsincollege_sitekey_to_marketid[escortsincollege_title_to_sitekey(title)])

### ESCORTPHONELIST

def escortphonelist_title_to_sitekey(title):
    """"602-330-8931 - Escort ad in Phoenix, Arizona | Sexy Latina With Huge Ll Natural Ddd's $100 !!"""
    start = 28
    end = title.index('|')
    sitekey = title[start:end].strip()
    return sitekey

def determineMarketEscortphonelist(url, title, city, state):
    return marketid_to_market_tuple("title", escortphonelist_sitekey_to_marketid[escortphonelist_title_to_sitekey(title)])

### EROTICMUGSHOTS
### MASSAGETROLL



def eroticmugshots_url_to_sitekey(url):
    """http://eroticmugshots_massagetroll.com/houston-escorts/719-492-9016/?pid=6887627"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    d = path.split('/')[1]
    if d.endswith('-escorts'):
        return d[0:-8]
    else:
        return None

def massagetroll_url_to_sitekey(url):
    """http://eroticmugshots_massagetroll.com/houston-escorts/719-492-9016/?pid=6887627"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    d = path.split('/')[1]
    if d.endswith('-massages'):
        return d[0:-9]
    else:
        return None

def determineMarketEroticmugshots(url, title, city, state):
    return marketid_to_market_tuple("url", eroticmugshots_massagetroll_sitekey_to_marketid[eroticmugshots_url_to_sitekey(url)])

def determineMarketMassagetroll(url, title, city, state):
    return marketid_to_market_tuple("url", eroticmugshots_massagetroll_sitekey_to_marketid[massagetroll_url_to_sitekey(url)])

### ESCORTADSXXX
### ESCORTSINCA
### ESCORTSINTHEUS



def escorts181920_citystate_to_marketid(city, state):
    """http://longisland.escorts181920.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    return escorts181920_sitekey_to_marketid.get((city, state), None)

def determineMarketEscorts181920(url, title, city, state):
    return marketid_to_market_tuple("city,state", escorts181920_citystate_to_marketid(city,state))

def determineMarketEscortadsxxx(url, title, city, state):
    return determineMarketEscorts181920(url, title, city, state)

def determineMarketEscortsinca(url, title, city, state):
    return determineMarketEscorts181920(url, title, city, state)

def determineMarketEscortsintheus(url, title, city, state):
    return determineMarketEscorts181920(url, title, city, state)

### LIVEESCORTREVIEWS



def liveescortreviews_url_to_sitekey(url):
    """http://liveescortreviews.com/ad/daytona/702-637-9016/5/3463"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = path.split('/')[2]
    return sitekey

def determineMarketLiveescortreviews(url, title, city, state):
    return marketid_to_market_tuple("url", liveescortreviews_sitekey_to_marketid[liveescortreviews_url_to_sitekey(url)])

def determineMarketMyproviderguideforum(url, title, city, state):
    pass

def determineMarketUsasexguide(url, title, city, state):
    pass

def determineMarketEroticreview(url, title, city, state):
    pass

def determineMarketAdultsearch(url, title, city, state):
    pass

def determineMarketHappymassage(url, title, city, state):
    pass

def determineMarketUtopiaguide(url, title, city, state):
    pass

def determineMarketMissingkids(url, title, city, state):
    pass

def determineMarketAlibaba(url, title, city, state):
    pass

def determineMarketJustlanded(url, title, city, state):
    pass

def determineMarketGmdu(url, title, city, state):
    pass

def determineMarketTradekey(url, title, city, state):
    pass

def determineMarketManpowervacancy(url, title, city, state):
    pass

def determineMarketGulfjobsbank(url, title, city, state):
    pass

def determineMarketEc21(url, title, city, state):
    pass

handlers_by_source = {
                      "backpage": determineMarketBackpage,
                      "craigslist": determineMarketCraigslist,
                      "classivox": determineMarketClassivox,
                      "myproviderguide": determineMarketMyproviderguide,
                      "naughtyreviews": determineMarketNaughtyreviews,
                      "redbook": determineMarketRedbook,
                      "cityvibe": determineMarketCityvibe,
                      "massagetroll": determineMarketMassagetroll,
                      "redbook_forum": determineMarketRedbook_forum,
                      "cityxguide": determineMarketCityxguide,
                      "cityxguideforum": determineMarketCityxguideforum,
                      "rubads": determineMarketRubads,
                      "anunico": determineMarketAnunico,
                      "sipsap": determineMarketSipsap,
                      "escortsincollege": determineMarketEscortsincollege,
                      "escortphonelist": determineMarketEscortphonelist,
                      "eroticmugshots": determineMarketEroticmugshots,
                      "escortadsxxx": determineMarketEscortadsxxx,
                      "escortsinca": determineMarketEscortsinca,
                      "escortsintheus": determineMarketEscortsintheus,
                      "liveescortreviews": determineMarketLiveescortreviews,
                      "myproviderguideforum": determineMarketMyproviderguideforum,
                      "usasexguide": determineMarketUsasexguide,
                      "eroticreview": determineMarketEroticreview,
                      "adultsearch": determineMarketAdultsearch,
                      "happymassage": determineMarketHappymassage,
                      "utopiaguide": determineMarketUtopiaguide,
                      "missingkids": determineMarketMissingkids,
                      "alibaba": determineMarketAlibaba,
                      "justlanded": determineMarketJustlanded,
                      "gmdu": determineMarketGmdu,
                      "tradekey": determineMarketTradekey,
                      "manpowervacancy": determineMarketManpowervacancy,
                      "gulfjobsbank": determineMarketGulfjobsbank,
                      "ec21": determineMarketEc21}

def determineMarket(source, url, title, city, state, idx=0):
    try:
        source = int(source)
    except:
        pass
    try:
        handler = handlers_by_source[sources_by_id.get(source, source)]
        l = handler(url, title, city, state)
        return str(l) if idx==None else l[idx]
    except:
        pass
    return None

'''
### BOILERPLATE

boilerplate_sitekey_to_marketid = {"zurich": "ZRH"}

def boilerplate_url_to_sitekey(url):
    """http://longisland.boilerplate.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def determineMarketBoilerplate(url, title, city, state):
    return marketid_to_market_tupleboilerplate_sitekey_to_marketid[boilerplate_url_to_sitekey(url)])
'''

"""intended use:

create python transform 'marketinfo':

return determineMarket(getValue('sources_id'), getValue('url'), getValue('title'), getValue('city'), getValue('state'))

"""
