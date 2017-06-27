from unittest import TestCase
from testing import PLAYWITHERRORS
from pandas.util import testing as tm


import mymod



class TestTONUMERIC(TestCase):
    def test_try_numeric(self):
        new = TONUMERIC()
        s = pd.Series(['1', '-3.14', '7'])
        new.try_numeric(s)

        expected = pd.Series([1, -3.14, 7])
        tm.assert_series_equal(res, expected)

        s = pd.Series(['1', '-3.14', 7])
        res = to_numeric(s)
        tm.assert_series_equal(res, expected)


    def try_errors(self):
        s = pd.Series([1, -3.14, 'apple'])

        msg = 'Unable to parse string "apple" at position 2'
        with tm.assert_raises_regex(ValueError, msg):
            to_numeric(s, errors='raise')

        res = to_numeric(s, errors='ignore')
        expected = pd.Series([1, -3.14, 'apple'])

        tm.assert_series_equal(res, expected)

    def test_val_err(self):
        msg = 'Number less than 10'
        with tm.assert_raises_regex(ValueError, msg):
            PLAYWITHERRORS.val_err_raises(8, errors='raise')

    def test_except(self):
        self.assertRaises("Hello exception", mymod.PLAYWITHERRORS.except_probs(2))
