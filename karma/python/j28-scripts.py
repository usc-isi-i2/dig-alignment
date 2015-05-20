# Three models
# JSON data models THREAd to provide
# 

# function to 

try:
    from urlparse import urlunparse, urljoin
except:
    pass


def j28ThreadUri(threadUrl):
    return "thread/" + get_url_hash(threadUrl)

def j28PostUri(postUrl):
    """Canonicalize postURL to drop query and fragment"""
    (scheme, netloc, path, params, query, fragment) = urlparse(postUrl)
    return "post/" + get_url_hash(urlunparse( (scheme, netloc, path, params, "", "") ))

def j28ImageUri(url):
    return "image/" + get_url_hash(url)

def j28FeatureProperty():
    """the name of the property"""
    pass

def j28SourceName(originalfile):
    return ".".join(originalfile.split('.')[0:-1])

SITEROOTS = {"airgunadvice.net": "http://www.airgunadvice.net",
             "americanpreppersnetwork.net": "http://americanpreppersnetwork.net",
             "arguntrader.com": "http://arguntrader.com",
             "claytargetclassifieds.com": "http://www.claytargetclassifieds.com",
             "comebackalive.com": "http://cafe.comebackalive.com",
             "ducksouth.com": "http://www.ducksouth.com/phpbb",
             "gobblernation.com": "http://www.gobblernation.com/phpBB3",
             "henryfirearms.org": "http://http://www.henryfirearms.org/henrybb/",
             "isthmus.com": "http://forum.isthmus.com",
             "kentuckyarmoryclub.com": "http://kentuckyarmoryclub.com",
             "levergunscommunity.com": "http://levergunscommunity.com",
             "marauderairrifle.com": "http://marauderairrifle.com/forum",
             "modernmuzzleloader.com": "http://modernmuzzleloader.com/forum",
             "newmexicoguntrader.net": "http://newmexicoguntrader.net",
             "nodakoutdoors.com": "http://nodakoutdoors.com/forums",
             "nosler.com": "http://forum.nosler.com",
             "ohioccwforums.org": "http://ohioccwforums.org",
             "pistolworld.com": "http://pistolworld.com/bbs",
             "remingtonsociety.com": "http://www.remingtonsociety.com/forums",
             "rossi-rifleman.com": "http://www.rossi-rifleman.com",
             "silencerforum.com": "http://www.silencerforum.com",
             "spokaneguntrader.com": "http://www.spokaneguntrader.com",
             "texaschlforum.com": "http://www.texaschlforum.com",
             "tfaonline.org": "http://www.tfaonline.org/forum",
             "theliberalgunclub.com": "http://www.theliberalgunclub.com/phpBB3",
             "tndeer.com": "http://www.tndeer.com/forums",
             "treasurestatearms.com": "http://www.treasurestatearms.com/phpbb3",
             "utahconcealedcarry.com": "http://www.utahconcealedcarry.com"}

def j28SiteRoot(sourceName):
    return SITEROOTS.get(sourceName, "")

def j28ThreadLinkAbsolute(siteRoot, threadLink):
    return urljoin(siteRoot, threadLink)


def j28FcUri(uri):
    return atf_fc_uri(uri)

