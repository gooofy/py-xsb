#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name         ='py-xsb-prolog',
      version      ='0.1.2',
      description  ='Python interface for XSB Prolog',
      url          ='https://github.com/gooofy/py-xsb-prolog',
      classifiers  = [
                      'Topic :: Scientific/Engineering :: Artificial Intelligence',
                      'Topic :: Software Development :: Libraries :: Python Modules',
                      'Operating System :: POSIX :: Linux',
                      'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                      'Programming Language :: Python :: 2',
                      'Programming Language :: Python :: 2.7',
                      'Intended Audience :: Developers',
                      'Intended Audience :: Science/Research',
                     ],
      keywords     = 'XSB Prolog interface AI artificial intelligence reasoning programming in logic',
      platforms    = 'Linux',
      license      = 'LGPLv3',
      package_dir  = {'xsbprolog': 'xsbprolog'},
      packages     = ['xsbprolog'],
      author       = "Guenter Bartsch",
      author_email = "guenter@zamia.org",
      )
