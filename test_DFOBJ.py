from unittest import TestCase
from testing import DFOBJ
import pandas

class TestDFOBJ(TestCase):



    def test_create_date(self):
        newfr = DFOBJ()
        newfr.create_df()
        frame = newfr.make_df()
        date = frame.date
        for elem in date:
            print(elem.split("-"))
            split = elem.split("-")
            year = int(split[0])
            day = int(split[1])
            assert( year < 2017 and year > 2006)
            assert(day < 14 and day >=1 )


    def test_create_df(self):
        newfr = DFOBJ()
        assert(len(newfr.indices) == 0)
        assert(len(newfr.dates) == 0)
        assert(len(newfr.types) == 0)
        assert(newfr.frame == {})
        newfr.create_df()
        for elem in newfr.types:
            assert(elem == 'exempt' or elem == 'non-exempt')
        assert(len(newfr.dates) == len(newfr.indices))
        assert(len(newfr.types) == len(newfr.dates))

    def test_make_df(self):
        newfr = DFOBJ()
        newfr.create_df()
        frame = newfr.make_df()
        assert(isinstance(frame,pandas.core.frame.DataFrame))