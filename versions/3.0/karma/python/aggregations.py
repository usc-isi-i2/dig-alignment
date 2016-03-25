class concat:
    def __init__(self, column_name, separator):
        self.result = ""
        self.separator = separator
        self.isFirst = True
        self.columnName = column_name

    def transform(self):
        return getValue(self.columnName)

    def accumulate(self, val):
        if self.isFirst:
            self.result += val
            self.isFirst = False
        else:
            self.result += self.separator + val

    def getResult(self):
        return self.result


class average:
    def __init__(self, column_name):
        self.result = ""
        self.columnName = column_name
        self.count = 0
        self.sum = 0

    def transform(self):
        value = getValue(self.columnName)
        try:
            return float(value)
        except ValueError:
            return 0

    def accumulate(self, val):
        self.count += 1
        self.sum += val

    def getResult(self):
        return str(self.sum / self.count)


class min:

    def __init__(self, column_name):
        self.result = ""
        self.columnName = column_name
        self.min = 0
        self.unset = True

    def transform(self):
        value = getValue(self.columnName)
        try:
            return float(value)
        except ValueError:
            return 0

    def accumulate(self, val):
        if self.unset:
            self.unset = False
            self.min = val
        elif self.min > val:
            self.min = val

    def getResult(self):
        return "NaN" if self.unset else str(self.min)


class max:

    def __init__(self, column_name):
        self.result = ""
        self.columnName = column_name
        self.max = 0
        self.unset = True

    def transform(self):
        value = getValue(self.columnName)
        try:
            return float(value)
        except ValueError:
            return 0

    def accumulate(self, val):
        if self.unset:
            self.unset = False
            self.max = val
        elif self.max < val:
            self.max = val

    def getResult(self):
        return "NaN" if self.unset else str(self.max)