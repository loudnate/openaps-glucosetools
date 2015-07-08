from setuptools import setup, find_packages

long_description ='''openaps MMGlucoseTools plugin
==============================
This package is a vendor plugin for openaps that provides tools for cleaning and
parsing glucose data.
'''

requires = ['openaps', 'python-dateutil']

__version__ = None
exec(open('openapscontrib/mmglucosetools/version.py').read())

setup(
    name='openapscontrib.mmglucosetools',
    version=__version__,
    url='http://github.com/loudnate/openaps-mmglucosetools',
    download_url='http://pypi.python.org/pypi/openapscontrib.mmglucosetools',
    license='MIT',
    author='Nathan Racklyeft',
    author_email='loudnate+pypi@gmail.com',
    description='openaps mmglucosetools plugin',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['openapscontrib'],
    test_suite="tests"
)
