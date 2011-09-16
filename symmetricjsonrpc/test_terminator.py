import StringIO
import unittest

import json
import wrappers

class TestWriter(unittest.TestCase):
    def setUp(self):
        self.f_ = StringIO.StringIO()
        self.terminator = '#'
        wrappers.add_terminator(self.f_, self.terminator)
        self.writer = json.Writer(self.f_, encoding='UTF-8')

    def test_no_write_until_flush(self):
        # Make a string is bigger than the buffer to test flush logic.
        big_string = 'abcd' * wrappers.WriterWrapper.buff_maxsize
        self.writer.unflushed_write_value(big_string)
        self.assertEqual(self.f_.getvalue(), '')
        self.writer.s.flush()
        self.assertEqual(self.f_.getvalue(),
                         '"%s"%s' % (big_string, self.terminator))

    def test_two_objects(self):
        str1 = 'abcd'
        str2 = 'efgh'
        self.writer.write_value(str1)
        self.writer.write_value(str2)
        self.assertEqual(self.f_.getvalue(),
                         '"%s"%s"%s"%s' % (str1, self.terminator,
                                           str2, self.terminator))


class TestReader(unittest.TestCase):
    def setUp(self):
        self.terminator = '#'

    def test_two_objects(self):
        str1 = 'monty'
        str2 = 'python'
        f_ = StringIO.StringIO('"%s"%s"%s"%s' % (str1, self.terminator,
                                                 str2, self.terminator))

        wrappers.add_terminator(f_, self.terminator)
        reader = json.Reader(f_)
        self.assertEqual(str1, reader.read_value())
        self.assertEqual(str2, reader.read_value())


if __name__ == '__main__':
    unittest.main()
