"""
test_ch1.py

Auther: thgch
Created on 2020/05/17

"""

import unittest
import numpy as np
import ch1 as testee


class TestCh1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # From here, test for each function #
    def test_class(self):
        m = testee.Man("David")
        m.hello()
        m.goodbye()

    def test_numpy(self):
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([2.0, 4.0, 6.0])
        np.testing.assert_allclose(x + y, [3.0, 6.0, 9.0], rtol=1.0e-8)


if __name__ == '__main__':
    unittest.main(verbosity=2)