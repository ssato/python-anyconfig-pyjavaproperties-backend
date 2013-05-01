#
# Copyright (C) 2012 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
from anyconfig.compat import StringIO, iteritems
from anyconfig.backend.base import ConfigParser

import pyjavaproperties


SUPPORTED = True


def dump_impl(data, config_fp):
    """TODO: How to encode nested dicts?
    """
    p = pyjavaproperties.Properties()
    for k, v in iteritems(data):
        p.setProperty(k, v)

    p.store(config_fp)


class PropertiesParser(ConfigParser):

    _type = "properties"
    _extensions = ["properties"]
    _supported = SUPPORTED

    # FIXME:
    #@classmethod
    #def loads(cls, config_content, *args, **kwargs):
    #    config_fp = StringIO(config_content)
    #    return load_impl(config_fp, cls.container())

    @classmethod
    def load_impl(cls, config_fp, **kwargs):
        """
        :param config_fp:  Config file object
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: dict object holding config parameters
        """
        p = pyjavaproperties.Properties()
        p.load(config_fp)

        return p.getPropertyDict()

    @classmethod
    def dumps_impl(cls, data, **kwargs):
        """
        :param data: Data to dump :: dict
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: string represents the configuration
        """
        config_fp = StringIO()
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
