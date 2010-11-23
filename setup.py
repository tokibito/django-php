#!/usr/bin/env python
from setuptools import setup, find_packages
 
setup(
    name='django-php',
    version='0.1',
    description='PHP in Django.',
    author='Shinya Okano',
    author_email='tokibito@gmail.com',
    url='http://bitbucket.org/tokibito/django-php',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'Programming Language :: PHP',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=["djangophp"],
    #test_suite='tests',
)
