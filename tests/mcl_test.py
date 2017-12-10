#!/usr/bin/env python

# python -m unittest -v tests.mcl_test

import unittest
import filecmp

import os

from public.solver import solver

class MCLTest(unittest.TestCase):
    TEST_FILE = 'tests/test.csv'

    def test_MCL(self):
        solver('tests/examples/1.csv', 'output_info.txt', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/1.csv', self.TEST_FILE, shallow=False))

        solver('tests/examples/2.csv', 'output_info.txt', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/2.csv', self.TEST_FILE, shallow=False))

        solver('tests/examples/3.csv', 'output_info.txt', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/3.csv', self.TEST_FILE, shallow=False))

        solver('tests/examples/4.csv', 'output_info.txt', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/4.csv', self.TEST_FILE, shallow=False))

        solver('tests/examples/5.csv', 'output_info.txt', self.TEST_FILE)
        self.assertTrue(filecmp.cmp('tests/outputs/5.csv', self.TEST_FILE, shallow=False))

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE):
            os.remove(self.TEST_FILE)