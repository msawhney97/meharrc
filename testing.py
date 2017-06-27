import pytest
import random
import requests
import random

import pandas as pd

class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def assignWidLen(self):
        self.length = random.randint(10,15)
        self.width = random.randint(15,20)

    def area(self):
        print(self.width, self.length)
        return self.width * self.length
from test_foo import Foo
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ['Comparing Foo instances:',
                '   vals: %s != %s' % (left.val, right.val)]

class DFOBJ:

    def __init__(self):
        self.indices = []
        self.dates = []
        self.types = []
        self.frame = {}

    def create_date(self):
        year = str(random.choice([2007, 2008, 2009, 2010, 2012, 2014, 2016]))
        month = str(random.randrange(1, 13))
        date = year + '-' + month
        return date

    def create_df(self):
        for index in range(1,10):
            self.indices.append(index)
            self.dates.append(self.create_date())
            val = random.randint(0,1)
            if val == 0:
                self.types.append('exempt')
            else:
                self.types.append('non-exempt')

    def make_df(self):
        dict = {
            'type': pd.Series(self.types, index=self.indices),
            'date': pd.Series(self.dates, index=self.indices)
        }

        self.frame = pd.DataFrame(dict)
        return self.frame
    # def col_elements(self):
    #     for elem in self.frame.date:
    #         print (elem)
    #     print(self.frame.date)
        # for dates,types in self.frame.iteritems():
        #     print(dates, 'dates', types, 'types')


# newfr = DFOBJ()
# newfr.create_df()
# newfr.make_df()
# print(newfr.col_elements())

class TONUMERIC:
    def series1(self, series):
        return pd.Series(to_numeric(series))



class PLAYWITHERRORS:
    def val_err_raises(self ,num):
        if num < 10 :
            raise ValueError("Number less than 10")
        else:
            pass
    def except_probs(self, num):
        if num < 10:
            raise Exception("Hello exception")




