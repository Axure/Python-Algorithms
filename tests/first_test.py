from pymath.types import ExtendedReals
from pymath.types.ExtendedReals import *
import unittest


class FirstTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    a = Interval(3, 'p_i')
    b = Interval(3, 5)
    c = Interval('n_i', 'p_i')
    d = Interval('n_i', 6)

    print(a)
    print(b)
    print(c)
    print(d)

    print(a.lower == 3)
    print(a.lower == 4)
    print(a.upper == 'p_i')

    unittest.main()
