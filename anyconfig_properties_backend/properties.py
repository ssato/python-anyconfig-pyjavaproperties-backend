#
# Copyright (C) 2012 - 2017 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
"""
Java properties file support.

.. note::
   Now anyconfig has a native Java properties backend and there is no need to
   install this package. This package will be kept as an reference but
   obsoleted and not updated anymore.

- Format to support: Java Properties file, e.g.
  http://docs.oracle.com/javase/1.5.0/docs/api/java/util/Properties.html
- Requirements: pyjavaproperties,
  https://pypi.python.org/pypi/pyjavaproperties
- Limitations: None obvious
- Special options: None obvious
"""
from __future__ import absolute_import

import pyjavaproperties
import anyconfig.backend.base
import anyconfig.compat


class Parser(anyconfig.backend.base.StreamParser):
    """
    Parser for Java properties files (sample).
    """
    _type = "properties"
    _extensions = ["properties"]

    # ..todo:: Extend pyjavaproperties to implement 'loads' API like json.
    def load_from_string(self, content, container, **kwargs):
        """
        Load config from given string `content`.

        :param content: Config content string
        :param container: callble to make a container object later
        :param kwargs: optional keyword parameters to be sanitized :: dict

        :return: Dict-like object holding config parameters
        """
        raise NotImplementedError()

    def load_from_stream(self, stream, container, **kwargs):
        """
        Load config from given file like object `stream`.

        :param stream: A file or file like object of Java properties files
        :param container: callble to make a container object later
        :param kwargs: optional keyword parameters (ignored actually)

        :return: self.container object holding config parameters
        """
        props = pyjavaproperties.Properties()
        props.load(stream)

        return container(props.getPropertyDict())

    def dump_to_stream(self, cnf, stream, **kwargs):
        """
        Dump config `cnf` to a file or file-like object `stream`.

        :param cnf: Java properties config data to dump :: self.container
        :param stream: Java properties file or file like object
        :param kwargs: backend-specific optional keyword parameters :: dict
        """
        props = pyjavaproperties.Properties()
        for key, val in anyconfig.compat.iteritems(cnf):
            props.setProperty(key, val)

        props.store(stream)

# vim:sw=4:ts=4:et:
