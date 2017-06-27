from unittest import TestCase
from testing import  Rectangle

class TestRectangle(TestCase):
    def test_area(self):
        r = Rectangle()
        r.assignWidLen()
        print(r.length, r.width)
        assert (r.width <= 20)
        assert (r.width >= 15)
        assert (r.length <= 15)
        assert (r.length >= 10)
        assert (r.area() <= 300 and r.area() >=150)



