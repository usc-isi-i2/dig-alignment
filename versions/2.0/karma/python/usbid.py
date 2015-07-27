
# returns sha1 of manufacturer and model
def us_getTextHash(manufacturer,model):
    text=manufacturer+model
    if text:
        return hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
    return ''
