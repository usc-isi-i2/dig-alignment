#!/usr/bin/python

import sys
from urlparse import urlparse
from pymodutil import echo

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

metadata_by_source = {
    "backpage": {"columns": "url",
                 "keytype": "sitekey"},
    "craigslist": {"columns": "url",
                   "keytype": "sitekey"},
    "classivox": {"columns": "url",
                  "keytype": "sitekey"},
    "myproviderguide": {"columns": "url",
                        "keytype": "sitekey"},
    "naughtyreviews": {"columns": "url",
                       "keytype": "citytuple"},
    "redbook": {"columns": None,
                "keytype": None},
    "cityvibe": {"columns": "url",
                 "keytype": "sitekey"},
    "massagetroll": {"columns": "url",
                     "keytype": "sitekey"},
    "redbook_forum": {"columns": None,
                      "keytype": None},
    "cityxguide": {"columns": None,
                   "keytype": None},
    "cityxguideforum": {"columns": None,
                        "keytype": None},
    "rubads": {"columns": None,
               "keytype": None},
    "anunico": {"columns": None,
                "keytype": None},
    "sipsap": {"columns": None,
               "keytype": None},
    "escortsincollege": {"columns": "title",
                         "keytype": "city,state"},
    "escortphonelist": {"columns": "title",
                        "keytype": "city,state"},
    "eroticmugshots": {"columns": "url",
                       "keytype": "sitekey"},
    "escortadsxxx": {"columns": "city,state",
                     "keytype": "city,state"},
    "escortsinca": {"columns": "city,state",
                    "keytype": "city,state"},
    "escortsintheus": {"columns": "city,state",
                       "keytype": "city,state"},
    "liveescortreviews": {"columns": "url",
                          "keytype": "sitekey"},
    "myproviderguideforum": {"columns": None,
                             "keytype": None},
    "usasexguide": {"columns": None,
                    "keytype": None},
    "eroticreview": {"columns": None,
                     "keytype": None},
    "adultsearch": {"columns": None,
                    "keytype": None},
    "happymassage": {"columns": None,
                     "keytype": None},
    "utopiaguide": {"columns": None,
                    "keytype": None},
    "missingkids": {"columns": None,
                    "keytype": None},
    "alibaba": {"columns": None,
                "keytype": None},
    "justlanded": {"columns": None,
                   "keytype": None},
    "gmdu": {"columns": None,
             "keytype": None},
    "tradekey": {"columns": None,
                 "keytype": None},
    "manpowervacancy": {"columns": None,
                        "keytype": None},
    "gulfjobsbank": {"columns": None,
                     "keytype": None},
    "ec21": {"columns": None,
             "keytype": None}
    }

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

def mkSrcMktUri(sourcename, keydata, base='http://dig.isi.edu'):
    if isinstance(keydata, (list, tuple)):
        keydata = "/".join(keydata)
    print keydata
    return "%s/sourcemarket/%s/%s" % (base, sourcename, keydata)

### 1. BACKPAGE

def backpage_url_to_sitekey(url):
    """http://longisland.backpage.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def dtMktBackpage(url, title, city, state):
    return marketid_to_market_tuple("url",backpage_sitekey_to_marketid[backpage_url_to_sitekey(url)])

def dtMktBackpage(url, title, city, state):
    return mkSrcMktUri("backpage", backpage_url_to_sitekey(url))

### 2. CRAIGSLIST

def craigslist_url_to_sitekey(url):
    """http://longisland.craigslist.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def dtMktCraigslist(url, title, city, state):
    return marketid_to_market_tuple("url", craigslist_sitekey_to_marketid[craigslist_url_to_sitekey(url)])

def dtMktCraigslist(url, title, city, state):
    return mkSrcMktUri("craigslist", craigslist_url_to_sitekey(url))

### 3. CLASSIVOX

def classivox_url_to_sitekey(url):
    """http://longisland.classivox.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = netloc.split('.')[0]
    return sitekey

def dtMktClassivox(url, title, city, state):
    return marketid_to_market_tuple("url", classivox_sitekey_to_marketid[classivox_url_to_sitekey(url)])

def dtMktClassivox(url, title, city, state):
    return mkSrcMktUri("classivox", classivox_url_to_sitekey(url))

### 4. MYPROVIDERGUIDE

def myproviderguide_url_to_sitekey(url):
    """http://longisland.myproviderguide.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    dirs = path.split('/')
    return dirs[2]

def dtMktMyproviderguide(url, title, city, state):
    return marketid_to_market_tuple("url", myproviderguide_sitekey_to_marketid[myproviderguide_url_to_sitekey(url)])

def dtMktMyproviderguide(url, title, city, state):
    return mkSrcMktUri("myproviderguide", myproviderguide_url_to_sitekey(url))

### 5. NAUGHTYREVIEWS

def process(url):
    bits = url.split('/')
    print bits
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


naughtyreviews_multiword_cities = set([ # 2-WORD city names
                                       ("las", "vegas",),
                                       ("los", "angeles",),
                                       ("new", "york",),
                                       ("san", "diego",),
                                       ("palm", "beach",),
                                       ("new", "orleans",),
                                       ("st", "louis",),
                                       ("kansas", "city",),
                                       ("washington", "dc",),
                                       ("san", "jose",),
                                       ("san", "francisco",),
                                       ("panama", "city",),
                                       ("orange", "county",),
                                       ("san", "antonio",),
                                       ("fort", "lauderdale",),
                                       ("oklahoma", "city",),
                                       ("central", "jersey",),
                                       ("grand", "rapids",),
                                       ("myrtle", "beach",),
                                       ("lake", "city",),
                                       ("des", "moines",),
                                       ("daytona", "beach",),
                                       ("baton", "rouge",),
                                       ("south", "bend",),
                                       ("green", "bay",),
                                       ("kuala", "lumpur",),
                                       ("fort", "myers",),
                                       ("colorado", "springs",),
                                       ("long", "island",),
                                       ("san", "juan",),
                                       ("niagara", "falls",),
                                       ("virginia", "beach",),
                                       ("sioux", "falls",),
                                       ("saint", "petersburg",),
                                       ("red", "deer",),
                                       ("st", "cloud",),
                                       ("sao", "paulo",),
                                       ("charlotte", "amalie",),
                                       ("little", "rock",),
                                       ("ft", "mcmurray",),
                                       ("new", "haven",),
                                       ("buenos", "aires",),
                                       ("mexico", "city",),
                                       ("atlantic", "city",),
                                       ("cape", "town",),
                                       ("fort", "wayne",),
                                       ("el", "paso",),
                                       ("hilton", "head",),
                                       ("inland", "empire",),
                                       ("key", "west",),
                                       ("lake", "charles",),
                                       ("jersey", "city",),
                                       ("hong", "kong",),
                                       ("fort", "collins",),
                                       ("santa", "barbara",),
                                       ("corpus", "christi",),
                                       ("la", "crosse",),
                                       ("boca", "raton",),
                                       ("northern", "virginia",),
                                       ("rapid", "city",),
                                       ("ann", "arbor",),
                                       ("palm", "springs",),
                                       ("taipei", "city",),
                                       ("cedar", "rapids",),
                                       ("tel", "aviv",),
                                       ("sioux", "city",),
                                       ("great", "falls",),
                                       ("long", "beach",),
                                       ("terre", "haute",),
                                       ("ventura", "county",),
                                       ("fort", "smith",),
                                       ("traverse", "city",),
                                       ("st", "john",),
                                       ("bowling", "green",),
                                       ("santa", "fe",),
                                       ("junction", "city",),
                                       # 3-WORD city names
                                       ("san", "fernando", "valley",),
                                       ("salt", "lake", "city",),
                                       ("salvador", "de", "bahia",),
                                       ("rio", "de", "janeiro",),
                                       ("west", "palm", "beach",),
                                       ("st", "john", "s",),
                                       ("ho", "chi", "minh",),
                                       ("san", "gabriel", "valley",),
                                       ("rio", "grande", "valley",),
                                       ])

def findSitekey(terms):
    if tuple(terms[-3:]) in naughtyreviews_multiword_cities:
        return tuple(terms[-3:])
    if tuple(terms[-2:]) in naughtyreviews_multiword_cities:
        return tuple(terms[-2:])
    return tuple(terms[-1:])

# def findSitekey(terms):
#     sk3 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-3:]))
#     if sk3:
#         return terms[-3:]
#     sk2 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-2:]))
#     if sk2:
#         return terms[-2:]
#     sk1 = naughtyreviews_sitekey_to_marketid.get(tuple(terms[-1:]))
#     if sk1:
#         return terms[-1:]
#     return None

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
        cands = findSitekey(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on escort %r: [%s]" % (line, e)
        return 0
    return cands

def processAgency(line):
    cands = 0
    try:
        terms = line.split('-')[1:]
        (suffix, terms) = trimNumericSuffix(terms)
        cands = findSitekey(terms[-3:])
    except Exception as e:
        print >> sys.stderr, "Give up on agency %r: [%s]" % (line, e)
        return 0
    return cands

def processMassage(line):
    terms = line.split('-')[1:]
    return findSitekey(terms[-3:])

def naughtyreviews_url_to_marketid(url):
    """http://longisland.naughtyreviews.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    try:
        return process(url)
    except Exception as e:
        print >> sys.stderr, e
        return None

def naughtyreviews_url_to_sitekey(url):
    """http://longisland.naughtyreviews.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    try:
        return process(url)
    except Exception as e:
        print >> sys.stderr, e
        return None

# def dtMktNaughtyreviews(url, title, city, state):
#     marketid = "/".join(naughtyreviews_url_to_marketid(url))
#     if marketid:
#         return mkSrcMktUri("naughtyreviews", 
#     else:
#         return None

def dtMktNaughtyreviews(url, title, city, state):
    return mkSrcMktUri("naughtyreviews", naughtyreviews_url_to_sitekey(url))

### 6. REDBOOK (not implemented)

def dtMktRedbook(url, title, city, state):
    pass

### 7. CITYVIBE

def cityvibe_url_to_sitekey(url):
    """http://www.cityvibe.com/losangeles/PremiumEscorts/ariel-wla-gfe-incalloutcall/396104"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = path.split('/')[1]
    return sitekey

def dtMktCityvibe(url, title, city, state):
    return marketid_to_market_tuple("url", cityvibe_sitekey_to_marketid[cityvibe_url_to_sitekey(url)])

def dtMktCityvibe(url, title, city, state):
    return mkSrcMktUri("cityvibe", cityvibe_url_to_sitekey(url))

### 9. REDBOOK_FORUM (not implemented)

def dtMktRedbook_forum(url, title, city, state):
    pass

### 10. CITYXGUIDE (not implemented)

def dtMktCityxguide(url, title, city, state):
    pass

### 11. CITYXGUIDE_FORUM (not implemented)

def dtMktCityxguideforum(url, title, city, state):
    pass

### 12. RUBADS (not implemented)

def dtMktRubads(url, title, city, state):
    pass

### 13. ANUNICO (not implemented)

def dtMktAnunico(url, title, city, state):
    pass

### 14. SIPSAP (not implemented)

def dtMktSipsap(url, title, city, state):
    pass

### 15. ESCORTSINCOLLEGE

def escortsincollege_title_to_sitekey(title):
    """202-277-7628 - Escort ad in Atlanta, Georgia | Visiting Visiting Visiting"""
    start = 28
    end = title.index('|')
    sitekey = title[start:end].strip()
    return sitekey

def dtMktEscortsincollege(url, title, city, state):
    return marketid_to_market_tuple("title", escortsincollege_sitekey_to_marketid[escortsincollege_title_to_sitekey(title)])

def dtMktEscortsincollege(url, title, city, state):
    return mkSrcMktUri("escortsincollege", escortsincollege_url_to_sitekey(url))

### 16. ESCORTPHONELIST

def escortphonelist_title_to_sitekey(title):
    """"602-330-8931 - Escort ad in Phoenix, Arizona | Sexy Latina With Huge Ll Natural Ddd's $100 !!"""
    start = 28
    end = title.index('|')
    sitekey = title[start:end].strip()
    return sitekey

def dtMktEscortphonelist(url, title, city, state):
    return marketid_to_market_tuple("title", escortphonelist_sitekey_to_marketid[escortphonelist_title_to_sitekey(title)])

def dtMktEscortphonelist(url, title, city, state):
    return mkSrcMktUri("escortphonelist", escortphonelist_url_to_sitekey(url))

### 17. EROTICMUGSHOTS
### 8. MASSAGETROLL

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

def dtMktEroticmugshots(url, title, city, state):
    return marketid_to_market_tuple("url", eroticmugshots_massagetroll_sitekey_to_marketid[eroticmugshots_url_to_sitekey(url)])

def dtMktEroticmugshots(url, title, city, state):
    return mkSrcMktUri("eroticmugshots",eroticmugshots_url_to_sitekey(url))

def dtMktMassagetroll(url, title, city, state):
    return marketid_to_market_tuple("url", eroticmugshots_massagetroll_sitekey_to_marketid[massagetroll_url_to_sitekey(url)])

def dtMktMassagetroll(url, title, city, state):
    return mkSrcMktUri("massagetroll" ,massagetroll_url_to_sitekey(url))

### 18. ESCORTADSXXX
### 19. ESCORTSINCA
### 20. ESCORTSINTHEUS

def escorts181920_citystate_to_marketid(city, state):
    """http://longisland.escorts181920.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377"""
    return escorts181920_sitekey_to_marketid.get((city, state), None)

def escorts181920_citystate_to_sitekey(city, state):
    return (clean(city), clean(state))
def escortadsxxx_citystate_to_sitekey(city, state):
    return escorts181920_citystate_to_sitekey(city, state)
def escortsinca_citystate_to_sitekey(city, state):
    return escorts181920_citystate_to_sitekey(city, state)
def escortsintheus_citystate_to_sitekey(city, state):
    return escorts181920_citystate_to_sitekey(city, state)

def dtMktEscortadsxxx(url, title, city, state):
    return mkSrcMktUri("escortadsxxx", escortadsxxx_citystate_to_sitekey(city, state))

def dtMktEscortsinca(url, title, city, state):
    return mkSrcMktUri("escortsinca", escortsinca_citystate_to_sitekey(city, state))

def dtMktEscortsintheus(url, title, city, state):
    return mkSrcMktUri("escortsintheus", escortsintheus_citystate_to_sitekey(city, state))

### 21. LIVEESCORTREVIEWS

def liveescortreviews_url_to_sitekey(url):
    """http://liveescortreviews.com/ad/daytona/702-637-9016/5/3463"""
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    sitekey = path.split('/')[2]
    return sitekey

def dtMktLiveescortreviews(url, title, city, state):
    return marketid_to_market_tuple("url", liveescortreviews_sitekey_to_marketid[liveescortreviews_url_to_sitekey(url)])

def dtMktLiveescortreviews(url, title, city, state):
    return mkSrcMktUri("url","liveescortreviews",liveescortreviews_url_to_sitekey(url))

### 22. MYPROVIDERGUIDE FORUM (not implemented)

def dtMktMyproviderguideforum(url, title, city, state):
    pass

### 23. USASEXGUIDE (not implemented)

def dtMktUsasexguide(url, title, city, state):
    pass

### 24. EROTICREVIEW (not implemented)

def dtMktEroticreview(url, title, city, state):
    pass

### 25. ADULTSEARCH (not implemented)

def dtMktAdultsearch(url, title, city, state):
    pass

### 26. HAPPYMASSAGE (not implemented)

def dtMktHappymassage(url, title, city, state):
    pass

### 27. UTOPIAGUIDE (not implemented)

def dtMktUtopiaguide(url, title, city, state):
    pass

### 28. MISSINGKIDS (not implemented)

def dtMktMissingkids(url, title, city, state):
    pass

### 29. ALIBABA (not implemented)

def dtMktAlibaba(url, title, city, state):
    pass

### 30. JUSTLANDED (not implemented)

def dtMktJustlanded(url, title, city, state):
    pass

### 31. GMDU (not implemented)

def dtMktGmdu(url, title, city, state):
    pass

### 32. TRADEKEY (not implemented)

def dtMktTradekey(url, title, city, state):
    pass

### 33. MANPOWERVACANCY (not implemented)

def dtMktManpowervacancy(url, title, city, state):
    pass

### 34. GULFJOBSBANK (not implemented)

def dtMktGulfjobsbank(url, title, city, state):
    pass

### 35. EC21 (not implemented)

def dtMktEc21(url, title, city, state):
    pass

# handlers_by_source = {
#                       "backpage": dtMktBackpage,
#                       "craigslist": dtMktCraigslist,
#                       "classivox": dtMktClassivox,
#                       "myproviderguide": dtMktMyproviderguide,
#                       "naughtyreviews": dtMktNaughtyreviews,
#                       "redbook": dtMktRedbook,
#                       "cityvibe": dtMktCityvibe,
#                       "massagetroll": dtMktMassagetroll,
#                       "redbook_forum": dtMktRedbook_forum,
#                       "cityxguide": dtMktCityxguide,
#                       "cityxguideforum": dtMktCityxguideforum,
#                       "rubads": dtMktRubads,
#                       "anunico": dtMktAnunico,
#                       "sipsap": dtMktSipsap,
#                       "escortsincollege": dtMktEscortsincollege,
#                       "escortphonelist": dtMktEscortphonelist,
#                       "eroticmugshots": dtMktEroticmugshots,
#                       "escortadsxxx": dtMktEscortadsxxx,
#                       "escortsinca": dtMktEscortsinca,
#                       "escortsintheus": dtMktEscortsintheus,
#                       "liveescortreviews": dtMktLiveescortreviews,
#                       "myproviderguideforum": dtMktMyproviderguideforum,
#                       "usasexguide": dtMktUsasexguide,
#                       "eroticreview": dtMktEroticreview,
#                       "adultsearch": dtMktAdultsearch,
#                       "happymassage": dtMktHappymassage,
#                       "utopiaguide": dtMktUtopiaguide,
#                       "missingkids": dtMktMissingkids,
#                       "alibaba": dtMktAlibaba,
#                       "justlanded": dtMktJustlanded,
#                       "gmdu": dtMktGmdu,
#                       "tradekey": dtMktTradekey,
#                       "manpowervacancy": dtMktManpowervacancy,
#                       "gulfjobsbank": dtMktGulfjobsbank,
#                       "ec21": dtMktEc21}

# def dtMkt(source, url, title, city, state, idx=0):
#     try:
#         source = int(source)
#     except:
#         pass
#     try:
#         handler = handlers_by_source[sources_by_id.get(source, source)]
#         l = handler(url, title, city, state)
#         return l
#     except:
#         pass
#     return None

handlers_by_source = {
                      "backpage": dtMktBackpage,
                      "craigslist": dtMktCraigslist,
                      "classivox": dtMktClassivox,
                      "myproviderguide": dtMktMyproviderguide,
                      "naughtyreviews": dtMktNaughtyreviews,
                      "redbook": dtMktRedbook,
                      "cityvibe": dtMktCityvibe,
                      "massagetroll": dtMktMassagetroll,
                      "redbook_forum": dtMktRedbook_forum,
                      "cityxguide": dtMktCityxguide,
                      "cityxguideforum": dtMktCityxguideforum,
                      "rubads": dtMktRubads,
                      "anunico": dtMktAnunico,
                      "sipsap": dtMktSipsap,
                      "escortsincollege": dtMktEscortsincollege,
                      "escortphonelist": dtMktEscortphonelist,
                      "eroticmugshots": dtMktEroticmugshots,
                      "escortadsxxx": dtMktEscortadsxxx,
                      "escortsinca": dtMktEscortsinca,
                      "escortsintheus": dtMktEscortsintheus,
                      "liveescortreviews": dtMktLiveescortreviews,
                      "myproviderguideforum": dtMktMyproviderguideforum,
                      "usasexguide": dtMktUsasexguide,
                      "eroticreview": dtMktEroticreview,
                      "adultsearch": dtMktAdultsearch,
                      "happymassage": dtMktHappymassage,
                      "utopiaguide": dtMktUtopiaguide,
                      "missingkids": dtMktMissingkids,
                      "alibaba": dtMktAlibaba,
                      "justlanded": dtMktJustlanded,
                      "gmdu": dtMktGmdu,
                      "tradekey": dtMktTradekey,
                      "manpowervacancy": dtMktManpowervacancy,
                      "gulfjobsbank": dtMktGulfjobsbank,
                      "ec21": dtMktEc21}

def dtMkt(source, url, title, city, state, idx=0):
    try:
        source = int(source)
    except:
        pass
    try:
        handler = handlers_by_source[sources_by_id.get(source, source)]
        l = handler(url, title, city, state)
        return l
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

def dtMktBoilerplate(url, title, city, state):
    return marketid_to_market_tupleboilerplate_sitekey_to_marketid[boilerplate_url_to_sitekey(url)])
'''

"""intended use:

create python transform 'marketinfo':

return dtMkt(getValue('sources_id'), getValue('url'), getValue('title'), getValue('city'), getValue('state'))

"""

TESTCASES= [
["backpage", "http://longisland.backpage.com/FemaleEscorts/s-mny-oo-chics-but-oo-nn-lik-oo-me-19/40317377", None, None, None],
["backpage", "http://bronx.backpage.com/FemaleEscorts/i-love-doing-this-lets-explore-unrushed-fun-try-somrthing-new-19-year-old-sexy-latin-19/42033905", None, None, None],
["backpage", "http://buffalo.backpage.com/FemaleEscorts/rockstar-chick-available-now-22/10960004", None, None, None],
["backpage", "http://manhattan.backpage.com/FemaleEscorts/sexi-hot-phat-booty-i-am-so-hot-babe-lets-get-our-freak-on-babe-beautiful-michel-29/43436197", None, None, None],
["backpage", "http://binghamton.backpage.com/FemaleEscorts/new-38dd-caribbeanbeauty-hot-like-fire-lve-2party-lets-get-kinky-24/1286614", None, None, None],

["craigslist", "http://bham.craigslist.org/cas/4209753359.html", None, None, None],
["craigslist", "http://juneau.craigslist.org/cas/4171573516.html", None, None, None],
["craigslist", "http://littlerock.craigslist.org/cas/4206819843.html", None, None, None],
["craigslist", "http://cosprings.craigslist.org/cas/4169982413.html", None, None, None],
["craigslist", "http://desmoines.craigslist.org/cas/4212904849.html", None, None, None],

["classivox","http://lexington.classivox.com/t/sex-guide/859-553-3365-just-a-reminder-mia-is-now-taking-appointments-now-38/358536/", None, None, None],
["classivox","http://pittsburgh.classivox.com/t/female-escorts/-hey-we-have-specials-today-or-massages-4126-07-1975/370287/", None, None, None],
["classivox","http://toronto.classivox.com/t/female-escorts/-bella-welcome-to-the-ultimate-experience-im/370954/", None, None, None],
["classivox","http://washington-dc.classivox.com/t/female-escorts/-hey-guys-im-back-intown-im-london-a-beautiful/372711/", None, None, None],
["classivox","http://augusta.classivox.com/t/female-escorts/706-538-7452-hi-guys-my-name-is-nikki-i-am-new-to/376531/", None, None, None],

["myproviderguide","http://www.myproviderguide.com/escorts/birmingham/free-posts/w4m/5538151_miss-mya.html",None, None, None],
["myproviderguide","http://www.myproviderguide.com/escorts/sierra-vista/free-posts/w4m/5165518_sexy-big-busted-redhead-girl.html",None, None, None],
["myproviderguide","http://www.myproviderguide.com/escorts/chico/free-posts/w4m/5430901_up-for-a-mutually-beneficial-a.html",None, None, None],
["myproviderguide","http://www.myproviderguide.com/escorts/san-fernando-valley/free-posts/w4m/2898312_your-new-atf-omg-ava-monroe.html",None, None, None],
["myproviderguide","http://www.myproviderguide.com/escorts/valdosta/free-posts/w4m/5436370_sweet-sexy-stunning-let-s-play.html",None, None, None],

["naughtyreviews","http://www.naughtyreviews.com/escorts/chloe-birmingham-white-female-1", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/dana-davis-palmdale-black-female", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/caroline-costello-richmond-white-female", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/ohare-goddess-chicago-white-female", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/playful-penn-erie-white-female", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/vanessa-houston-latin-shemale", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/brianna-birmingham-white-female-0", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/vanessa-houston-latin-shemale", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/companions/juliette-jakarta-asian-shemale", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/companions/chanel-dayton-mixed-female", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escort-agencies/my-exotic-escape-cleveland", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escort-agencies/bogus-agency-new-orleans-0", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/massage-parlors/renton-spadivine-temple-seattle", None, None, None],
["naughtyreviews","http://www.naughtyreviews.com/escorts/lebanese-middle-eastern-beauty-san-diego-middle-eastern-female", None, None, None],

["eroticmugshots","http://eroticmugshots.com/birmingham-escorts/256-642-1389/?pid=9734745", None, None, None],
["eroticmugshots","http://eroticmugshots.com/birmingham-escorts/205-266-0048/?pid=9580660", None, None, None],
["eroticmugshots","http://eroticmugshots.com/macon-escorts/404-308-6499/?pid=22002677", None, None, None],
["eroticmugshots","http://eroticmugshots.com/ftlauderdale-escorts/765-520-6437/?pid=8232257", None, None, None],
["eroticmugshots","http://eroticmugshots.com/houston-escorts/719-492-9016/?pid=6887627", None, None, None],

["liveescortreviews", "http://liveescortreviews.com/ad/huntsville/256-585-7212/14/2351", None, None, None],
["liveescortreviews", "http://liveescortreviews.com/ad/phoenix/602-432-9586/14/86334", None, None, None],
["liveescortreviews", "http://liveescortreviews.com/ad/phoenix/602-487-2432/49/72000", None, None, None],
["liveescortreviews", "http://liveescortreviews.com/ad/denver/720-621-0548/36/71638", None, None, None],
["liveescortreviews", "http://liveescortreviews.com/ad/denver/720-625-0460/49/70273", None, None, None],
["liveescortreviews", "http://liveescortreviews.com/ad/daytona/702-637-9016/5/3463", None, None, None],

["escortsincollege", None, "602-321-2061 - Escort ad in Flagstaff, Arizona | Any One For A Full Cup Of Juice", None, None],
["escortsincollege", None, "707-241-3258 - Escort ad in Flagstaff, Arizona | $ Pecails Specails Specail Two Girls Specails", None, None],
["escortsincollege", None, "623-432-9116 - Escort ad in Phoenix, Arizona | New Chic On Backpage Wait Til You Get A Load Of Her", None, None],
["escortsincollege", None, "619-717-9773 - Escort ad in Flagstaff, Arizona | Busty & Petite Exotic Or Erotic", None, None],
["escortsincollege", None, "202-277-7628 - Escort ad in Atlanta, Georgia | Visiting Visiting Visiting", None, None],

["escortphonelist", None, "480-652-1939 - Escort ad in Flagstaff, Arizona | I'm The Best That (u) N E V E R Had!! Blonde Thick Thighs Big B00ty W Curves C Ll Now!", None, None],
["escortphonelist", None, "480-316-0406 - Escort ad in Flagstaff, Arizona | #1 Premiere Escort Agency Is Now Hiring! Southern Comfort", None, None],
["escortphonelist", None, "619-581-3269 - Escort ad in Phoenix, Arizona | Double Trouble Sexy Mixed Barbie && Curvy Latin Freaks Incall Available Now", None, None],
["escortphonelist", None, "602-845-9280 - Escort ad in Phoenix, Arizona | Stop!!!! New Exotic Babe 100 Real Pics ) 80$pecials Ready For You Tonight! !! Incall Outcall", None, None],
["escortphonelist", None, "602-330-8931 - Escort ad in Phoenix, Arizona | Sexy Latina With Huge Ll Natural Ddd's $100 !!", None, None],

["escortadsxxx", None, None, "Birmingham", "Alabama"],
["escortadsxxx", None, None, "Atlanta", "Georgia"],
["escortadsxxx", None, None, "Savannah", "Georgia"],
["escortadsxxx", None, None, "Orlando", "Florida"],
["escortadsxxx", None, None, "Virginia Beach", "Virginia"],

["escortsinca", None, None, "Edmonton", "Alberta"],
["escortsinca", None, None, "Lethbridge", "Alberta"],
["escortsinca", None, None, "Regina", "Saskatchewan"],
["escortsinca", None, None, "Fort Mcmurray", "Alberta"],
["escortsinca", None, None, "Toronto", "Ontario"],

["escortsintheus", None, None, "Birmingham", "Alabama"],
["escortsintheus", None, None, "Baltimore", "Maryland"],
["escortsintheus", None, None, "Reno", "Nevada"],
["escortsintheus", None, None, "Montgomery", "Alabama"],
["escortsintheus", None, None, None, None],

["massagetroll", "http://massagetroll.com/auburn-massages/256-608-1040/?pid=7164973", None, None, None],
["massagetroll", "http://massagetroll.com/flagstaff-massages/480-267-5248/?pid=20876871", None, None, None],
["massagetroll", "http://massagetroll.com/sanfrancisco-massages/408-641-1859/?pid=16299331", None, None, None],
["massagetroll", "http://massagetroll.com/ventura-massages/678-949-6764/?pid=39604831", None, None, None],
["massagetroll", "http://massagetroll.com/fortmyers-massages/786-488-6466/?pid=12048202", None, None, None],

["eroticmugshots", "http://eroticmugshots.com/birmingham-escorts/256-642-1389/?pid=9734745", None, None, None],
["eroticmugshots", "http://eroticmugshots.com/birmingham-escorts/205-266-0048/?pid=9580660", None, None, None],
["eroticmugshots", "http://eroticmugshots.com/macon-escorts/404-308-6499/?pid=22002677", None, None, None],
["eroticmugshots", "http://eroticmugshots.com/ftlauderdale-escorts/765-520-6437/?pid=8232257", None, None, None],
["eroticmugshots", "http://eroticmugshots.com/houston-escorts/719-492-9016/?pid=6887627", None, None, None],

["cityvibe", "http://www.cityvibe.com/birmingham/Escorts/really-petite-very-exotic-insanely-erotic-absolutley-satisfying-100-real-23/1574731", None, None, None],
["cityvibe", "http://www.cityvibe.com/losangeles/PremiumEscorts/ariel-wla-gfe-incalloutcall/396104", None, None, None],
["cityvibe", "http://www.cityvibe.com/sanfrancisco/Escorts/mizisland-visiting-the-east-bay-and-sf-area/1568611", None, None, None],
["cityvibe", "http://www.cityvibe.com/northbayca/Escorts/sexy-sassy-february-bikini-model/1552503", None, None, None],
["cityvibe", "http://www.cityvibe.com/chicago/Escorts/direct-to-you-the-perfect-treat/1569024", None, None, None]
]

# TESTCASES = [TESTCASES[0]]
# TESTCASES = [["naughtyreviews","http://www.naughtyreviews.com/escorts/brianna-birmingham-white-female-0", None, None, None],
#              ["escortadsxxx", None, None, "Virginia Beach", "Virginia"]
#              ]
             
def main():
    for row in TESTCASES:
        print row,
        mkt = dtMkt(*row)
        print mkt

# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(main())
