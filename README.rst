=============================================
python-anyconfig-pyjavaproperties-backend
=============================================

This is a backend module for anyconfig to support Java properties config files
w/ using pyjavaproperties.

* Author: Satoru SATOH <ssato@redhat.com>
* License: MIT

SEE ALSO:

* pyjavaproperties: https://pypi.python.org/pypi/pyjavaproperties
* anyconfig: https://pypi.python.org/pypi/anyconfig

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/SRPMS/<package>-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

Test Status
=============

.. image:: https://api.travis-ci.org/ssato/python-anyconfig-pyjavaproperties-backend.png?branch=master
   :target: https://travis-ci.org/ssato/python-anyconfig-pyjavaproperties-backend
   :alt: Test status

.. vim:sw=2:ts=2:et:
