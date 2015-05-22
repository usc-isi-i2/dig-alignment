# Three models
# JSON data providing Thread
# JSON data providing Post
# XML data providing Post

try:
    from urlparse import urlunparse, urljoin
except:
    pass

### JSON-specific

def j28ThreadUri(threadUrl):
    if threadUrl:
        return "thread/" + get_url_hash(threadUrl)
    else:
        return ""

def j28PostUri(postUrl):
    """Canonicalize postURL to drop query and fragment"""
    if postUrl:
        (scheme, netloc, path, params, query, fragment) = urlparse(postUrl)
        # something like p=123#p456
        # means post p456 in context of (original? parent?) p123
        # but for us p=123#p456 and p=789#p456 are equivalent (and equivalent to p=456 with no fragment)
        # So this doesn't work
        # return "post/" + get_url_hash(urlunparse( (scheme, netloc, path, params, query, "") ))
        # So I will hash the entire URL and hope it joins nicely on the XML source
        return "post/" + get_url_hash(urlunparse( (scheme, netloc, path, params, query, fragment) ))
    else:
        return ""

def j28ImageUri(url):
    if url:
        return "image/" + get_url_hash(url)
    else:
        return ""

def j28FeatureProperty():
    """the name of the property"""
    pass

def j28SourceName(originalfile):
    return ".".join(originalfile.split('.')[0:-1])

J28SITEROOTS = {"airgunadvice.net": "http://www.airgunadvice.net",
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

HG2SITEROOTS = {"smf_abraxasgacelesox.onion": "http://abraxasgacelesox.onion",
                "phpbb_z34uj4opd3tejafn.onion": "http://z34uj4opd3tejafn.onion"}

## To avoid changing model, just append those new entries to original

J28SITEROOTS.update(HG2SITEROOTS)

def j28SiteRoot(sourceName):
    return J28SITEROOTS.get(sourceName, "")

# future
# def hg2SiteRoot(sourceName):
#     return HG2SITEROOTS.get(sourceName, "")

def j28ThreadLinkAbsolute(siteRoot, threadLink):
    return urljoin(siteRoot, threadLink)

def j28FcUri(uri):
    return atf_fc_uri(uri)

##################################################################

# XML-specific

def filterPostUri(name, content):
    if name=='url':
        return j28PostUri(content)
    else:
        return ''

J28XMLFEATURENAMES =  {"action": "transactionTypesMentioned",
                       "email_domain": "emailDomainsMentioned",
                       "firearm_type": "weaponsMentioned",
                       # is actually the source name, not forum within a source
                       # already handled as Thread.website
                       "forum_name": None,
                       "from_user": "fromUser",
                       "to_user": "toUsers",
                       # memex ontology
                       "keyword": "keywords",
                       "phone": "phonenumber",
                       # already handled elsewhere as Post.hasBodyPart
                       "post_content": None,
                       # this is the location mentioned in the text
                       "post_location": "placePostalAddress",
                       # modeled as Thread.hasTitlePart
                       "thread_name": None,
                       # ignore, seems an artifact of forum processing
                       "id": None,
                       # used to generate URI only
                       "url": None,
                       # this is the location of the post author
                       # already handled elsewhere as Post.placePostalAddress
                       "user_location": None,
                       # ignore, redundant with 
                       "year": None}

def j28xmlFeatureName(name):
    try:
        fn = J28XMLFEATURENAMES.get(name, "")
        return fn or ""
    except Exception as e:
        return ""

def j28xmlFeatureNameUri(fn):
    if fn:
        return "http://memexproxy.com/ontology/" + fn
    else:
        return ""

def j28xmlFeatureCollectionUri(uri):
    if uri:
        return atf_fc_uri(uri)
    else:
        return ""                               


def j28xmlFeatureCollectionLinkName(name):
    fn = j28xmlFeatureName(name)
    if fn:
        return "http://memexproxy.com/ontology/" + fn + "_feature"
    else:
        return ""

def j28xmlFeatureCollectionLinkNameUri(fn):
    if fn:
        return "http://memexproxy.com/ontology/" + fn
    else:
        return ""
