#
# Copyright (C) 2012 - 2017 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name
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

TEST_STRICT = False


class TestBase(unittest.TestCase):

    def setUp(self):
        self.psr = TT.Parser()


class TestBaseWithIO(TestBase):

    def setUp(self):
        super(TestBaseWithIO, self).setUp()

        (_, conf) = tempfile.mkstemp(prefix="ac-test-")
        open(conf, 'w').write(CONF_0)
        self.config_path = conf

    def tearDown(self):
        os.remove(self.config_path)


class Test_10_loads(TestBase):

    def test_10_loads(self):
        try:
            conf = self.psr.loads(CONF_0)
            self.assertEquals(conf['b'], "bbb", conf)

            if TEST_STRICT:
                self.assertEquals(conf['a'], 0, str(conf))
                self.assertEquals(conf["sect0"]['c'], ['x', 'y', 'z'])
        except NotImplementedError:
            pass


class Test_20_load(TestBaseWithIO):

    def test_20_load(self):
        conf = self.psr.load(self.config_path)

        self.assertEquals(conf['b'], "bbb", conf)

        if TEST_STRICT:
            self.assertEquals(conf['a'], 0, str(conf))
            self.assertEquals(conf["sect0"]['c'], ['x', 'y', 'z'])

# vim:sw=4:ts=4:et:
