# openaps glucosetools
An [openaps](https://github.com/openaps/openaps) plugin for cleaning and parsing glucose sensor data

[![Build Status](https://travis-ci.org/loudnate/openaps-glucosetools.svg)](https://travis-ci.org/loudnate/openaps-glucosetools)

## Motivation
Interpreting recent historical events is a foundational component in any [openaps](https://github.com/openaps/openaps) project, and this plugin aspires to be a central place for documenting and testing the parsing of glucose sensor data.

## Getting started
### Installing from pypi

```bash
$ sudo easy_install openapscontrib.glucosetools
```

### Installing from source for development
Clone the repository and link via setuptools:
```bash
$ python setup.py develop
```

### Adding to your openaps project
```bash
$ openaps vendor add openapscontrib.glucosetools
$ openaps device add glucose glucosetools
```

## Usage
Use the device help menu to see available commands.
```bash
$ openaps use glucose -h
usage: openaps-use glucose [-h] USAGE ...

optional arguments:
  -h, --help  show this help message and exit

## Device glucose:
  vendor openapscontrib.glucosetools

  glucosetools - tools for cleaning, condensing, and reformatting history data





  USAGE       Usage Details
    clean     Resolve inconsistencies and ordering from a sequence of glucose
              data
    latest    Returns the latest glucose entry from a sequence of glucose data
```

Use the command help menu to see available arguments.
```bash
$ openaps use glucose clean -h
usage: openaps-use glucose clean [-h] [infile]

Resolve inconsistencies and ordering from a sequence of glucose data

positional arguments:
  infile      JSON-encoded glucose data

optional arguments:
  -h, --help  show this help message and exit

Tasks performed by this pass:
 - Removes unknown and erroneous data entries
 - Re-sorts all known values in reverse-chronological order
```

## Contributing
Contributions are welcome and encouraged in the form of bugs and pull requests.

### Testing

Unit tests can be run manually via setuptools.

```bash
$ python setup.py test
```
