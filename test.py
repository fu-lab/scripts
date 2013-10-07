# -*- coding=UTF-8 -*-

from __future__ import unicode_literals

import unittest

import os

import StringIO

# import filecmp

from goldendict_reader import GoldenDictReader
from sort import GoldenDictSorter
from tilde import GoldenDictTildeProcessor
from refxxx import GoldenDictRefXXXProcessor
# last line of imports


class GoldenDictScriptsTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = lambda x: os.path.join(
            os.path.dirname(__file__), 'files', x)

    def test_dict_reader_works_well(self):
        stdout = StringIO.StringIO()
        stderr = StringIO.StringIO()
        filename = self.filename('original_utf8.dsl')
        original_file = open(filename)
        original = [line for line in original_file]
        original_file.close()
        GoldenDictReader()(
            ['sort.py', filename],
            stdout=stdout,
            stderr=stderr
        )
        self.maxDiff = None
        stdout.seek(0)
        self.assertEqual(original, stdout.readlines())

    def test_dict_sorter_works_well(self):
        stdout = StringIO.StringIO()
        stderr = StringIO.StringIO()
        original_file = open(self.filename('original_utf8.dsl'))
        original = [line for line in original_file]
        original_file.close()
        GoldenDictSorter()(
            ['sort.py', self.filename('unsorted_utf8.dsl')],
            stdout=stdout,
            stderr=stderr
        )
        self.maxDiff = None
        stdout.seek(0)
        '''
        for x in stdout.readlines():
            print x
        stdout.seek(0)
        '''
        self.assertEqual(original, stdout.readlines())

    def test_tilde_processor_works_well(self):
        stdout = StringIO.StringIO()
        stderr = StringIO.StringIO()
        original_file = open(self.filename('tilde_processed_utf8.dsl'))
        original = [line for line in original_file]
        original_file.close()
        GoldenDictTildeProcessor()(
            ['sort.py', self.filename('original_utf8.dsl')],
            stdout=stdout,
            stderr=stderr
        )
        self.maxDiff = None
        stdout.seek(0)
        '''
        for x in stdout.readlines():
            print x
        stdout.seek(0)
        '''
        self.assertEqual(original, stdout.readlines())

    def _test_class_works_well(self, klass, original_filename,
                               processed_filename):
        stdout = StringIO.StringIO()
        stderr = StringIO.StringIO()
        original_file = open(self.filename(processed_filename))
        original = [line for line in original_file]
        original_file.close()
        klass()(
            ['sort.py', self.filename(original_filename)],
            stdout=stdout,
            stderr=stderr
        )
        self.maxDiff = None
        stdout.seek(0)
        '''
        for x in stdout.readlines():
            print x
        stdout.seek(0)
        '''
        self.assertEqual(original, stdout.readlines())

    def do_test_refxxx_works_well(self, s):
        self._test_class_works_well(GoldenDictRefXXXProcessor,
                                    'refxxx_original%s.txt' % s,
                                    'refxxx_processed%s.txt' % s)

    def test_refxxx_works_well(self):
        self.do_test_refxxx_works_well('')

    def test_refxxx_works_well1(self):
        self.do_test_refxxx_works_well('1')

    def tearDown(self):
        pass
        '''
        filename = self.filename('result_utf8.dsl')
        if os.path.exists(filename):
            os.unlink(filename)
        '''

if __name__ == '__main__':
    unittest.main()
