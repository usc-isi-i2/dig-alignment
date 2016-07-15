# from string_manipulation import SM

class SearchEval(object):

    def __init__(self):
        self.name = "SearchEval"

    @staticmethod
    def price_nice(amount, units, period):
        """Return a cannocical representation of a price"""
        value = SM.numeric_only(amount)
        period = period.strip()
        if period != '':
        	return str(value)+"/"+period
        else:
            return str(value)
