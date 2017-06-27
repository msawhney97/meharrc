import pytest

import numpy as np

print("import")

from pandas.core.dtypes.cast import (
    maybe_convert_string_to_object,
    infer_dtype_from_scalar
)

print("yo")

class TestThings(object):
    def test_convert_string_to_array(self):
        res = maybe_convert_string_to_object('Mehar')
        tm.assert_numpy_array_equal(res, np.array(['Mehar'], dtype=object))

    def test_bool_infer(self):
        for val in [True, False]:
            dt,vl = infer_dtype_from_scalar(val)
            assert (dt == np.bool_)


tests = TestThings()
tests.test_convert_string_to_array()
tests.test_bool_infer()
print("exited")


