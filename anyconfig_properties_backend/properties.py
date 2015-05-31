#
# Copyright (C) 2012 - 2015 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
"""
anyconfig backend to load/dump Java .properties files.
"""
from __future__ import absolute_import

import pyjavaproperties
import anyconfig.backend.base
import anyconfig.compat


def dump_impl(data, config_fp):
    """TODO: How to encode nested dicts?
    """
    prop = pyjavaproperties.Properties()
    for key, val in anyconfig.compat.iteritems(data):
        prop.setProperty(key, val)

    prop.store(config_fp)


class Parser(anyconfig.backend.base.Parser):
    """
    Parser for Java properties files.

    - Backend: pyjavaproperties (https://pypi.python.org/pypi/pyjavaproperties)
    - Limitations:

      - API 'loads' is not implemented yet.
      - pyjavaproperties does not support python 3

    - Special options: None obvious
    """

    _type = "properties"
    _extensions = ["properties"]

    # FIXME:
    # @classmethod
    # def loads(cls, config_content, *args, **kwargs):
    #     config_fp = anyconfig.compat.StringIO(config_content)
    #     return load_impl(config_fp, cls.container())

    @classmethod
    def load_impl(cls, config_fp, **kwargs):
        """
        :param config_fp:  Config file object
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: dict object holding config parameters
        """
        prop = pyjavaproperties.Properties()
        prop.load(config_fp)

        return prop.getPropertyDict()

    @classmethod
    def dumps_impl(cls, data, **kwargs):
        """
        :param data: Data to dump :: dict
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: string represents the configuration
        """
        config_fp = anyconfig.compat.StringIO()
        dump_impl(data, config_fp)

        return config_fp.getvalue()

    @classmethod
    def dump_impl(cls, data, config_path, **kwargs):
        """
        :param data: Data to dump :: dict
        :param config_path: Dump destination file path
        :param kwargs: backend-specific optional keyword parameters :: dict
        """
        dump_impl(data, open(config_path, 'w'))

# vim:sw=4:ts=4:et:
