#!/usr/bin/env python

# python -m unittest -v tests.mcl_test

import unittest
import filecmp

import os

from public.solver import solve

class MCLTest(unittest.TestCase):
    TEST_FILE = 'tests/output'

    def test_MCL(self):
        solve('tests/examples/1.csv', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/1', self.TEST_FILE, shallow=False))

        solve('tests/examples/2.csv', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/2', self.TEST_FILE, shallow=False))

        solve('tests/examples/3.csv', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/3', self.TEST_FILE, shallow=False))

        solve('tests/examples/4.csv', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/4', self.TEST_FILE, shallow=False))

        solve('tests/examples/5.csv', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/5', self.TEST_FILE, shallow=False))

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE):
            os.remove(self.TEST_FILE)