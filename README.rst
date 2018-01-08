=============================================
python-anyconfig-pyjavaproperties-backend
=============================================

.. image:: https://img.shields.io/travis/ssato/python-anyconfig-pyjavaproperties-backend.svg
   :target: https://travis-ci.org/ssato/python-anyconfig-pyjavaproperties-backend
   :alt: Test status

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-pyjavaproperties-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-pyjavaproperties-backend
   :alt: Coverage Status

.. image:: https://landscape.io/github/ssato/python-anyconfig-pyjavaproperties-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-pyjavaproperties-backend/master
   :alt: Code Health

This is a backend module for python-anyconfig to support Java properties config
files w/ using pyjavaproperties.

.. note::

   Please note that the latest version of python-anyconfig can load and dump
   Java propertiers files w/o this package now and you don't need to install
   this package usually. This package is just kept as an example how to write
   backend module for python-anyconfig.

* Author: Satoru SATOH <ssato@redhat.com>
* License: MIT

SEE ALSO:

* pyjavaproperties: https://pypi.python.org/pypi/pyjavaproperties
* python-anyconfig: https://pypi.python.org/pypi/anyconfig

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/SRPMS/<package>-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
