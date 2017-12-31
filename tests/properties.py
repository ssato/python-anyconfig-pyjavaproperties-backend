#
# Copyright (C) 2012 - 2015 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring
from __future__ import absolute_import
import anyconfig_properties_backend as TT

import os
import tempfile
import unittest


CONF_0 = """
a = 0
b = bbb

sect0.c = x;y;z
"""

TEST_LOADS = False
TEST_STRICT = False


class Test(unittest.TestCase):

    def setUp(self):
        (_, conf) = tempfile.mkstemp(prefix="ac-test-")
        open(conf, 'w').write(CONF_0)
        self.config_path = conf
        self.psr = TT.Parser()

    def tearDown(self):
        os.remove(self.config_path)

    def test_10_loads(self):
        """TODO: implement Parser.loads"""
        if not TEST_LOADS:
            return

        conf = self.psr.loads(CONF_0)
        self.assertEquals(conf['b'], "bbb", conf)

        if TEST_STRICT:
            self.assertEquals(conf['a'], 0, str(conf))
            self.assertEquals(conf["sect0"]['c'], ['x', 'y', 'z'])

    def test_20_load(self):
        conf = self.psr.load(self.config_path)

        self.assertEquals(conf['b'], "bbb", conf)

        if TEST_STRICT:
            self.assertEquals(conf['a'], 0, str(conf))
            self.assertEquals(conf["sect0"]['c'], ['x', 'y', 'z'])

# vim:sw=4:ts=4:et:
