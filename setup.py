# encoding: utf-8

import sys
import re
from os import path
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return open(file_path).read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]
    # integration with setup.py as described in
    # http://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='django-url-breadcrumbs',
    version=find_version('urlbreadcrumbs', '__init__.py'),
    description='a generic app to provide a simple breadcrumbs functionality in django projects',
    long_description=read('README.rst'),
    author='Sławek Ehlert',
    author_email='slafs@op.pl',
    license='BSD',
    url='https://bitbucket.org/slafs/django-url-breadcrumbs/',
    packages=find_packages(exclude=['testproject']),
    tests_require=['pytest', 'pytest-django', 'Django'],
    cmdclass = {'test': PyTest},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
