#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name             ='py-xsb',
      version          ='0.3.1',
      description      ='Python interface for XSB',
      long_description = open('README.md').read(),
      url              ='https://github.com/gooofy/py-xsb',
      classifiers      = [
                          'Topic :: Scientific/Engineering :: Artificial Intelligence',
                          'Topic :: Software Development :: Libraries :: Python Modules',
                          'Operating System :: POSIX :: Linux',
                          'Operating System :: Microsoft :: Windows',
                          'Operating System :: MacOS :: MacOS X',
                          'License :: OSI Approved :: Apache Software License',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.6',
                          'Programming Language :: Prolog',
                          'Intended Audience :: Developers',
                          'Intended Audience :: Science/Research',
                         ],
      keywords         = 'XSB interface AI artificial intelligence reasoning programming in logic',
      platforms        = 'Linux',
      license          = 'Apache',
      package_dir      = {'pyxsb': 'pyxsb'},
      packages         = ['pyxsb'],
      author           = "Guenter Bartsch",
      author_email     = "guenter@zamia.org",
      )
