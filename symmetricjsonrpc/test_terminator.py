import unittest

import json
import wrappers

class TestTerminator(unittest.TestCase):
    def test_one(self):
        # Make a terminated StringIO thingy.
        #
        # Does it put the terminator on when I flush, and not before.
        pass


if __name__ == '__main__':
    unittest.main()
