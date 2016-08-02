# from string_manipulation import SM

class SearchEval(object):

    def __init__(self):
        self.name = "SearchEval"

    @staticmethod
    def price_nice(amount, units, period):
        """Return a cannocical representation of a price"""
        value = SM.numeric_only(amount)
        try:
            x = float(value)
            if x < 10:
                return ''
            if x > 10000:
                return ''
            if x > 2010 and x < 2017:
                return ''
        except:
            pass
        period = period.strip()
        if period != '':
        	return str(value)+"/"+period
        else:
            return str(value)
