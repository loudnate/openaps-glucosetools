# mmglucosetools
An [openaps](https://github.com/openaps/openaps) plugin for cleaning and parsing medtronic glucose sensor data

## Motivation
Interpreting recent historical events is a foundational component in any [openaps](https://github.com/openaps/openaps) project, and this plugin aspires to be a central place for documenting and testing the parsing of glucose sensor data.

## Getting started
### Installing from pypi

```bash
$ sudo easy_install openapscontrib.mmglucosetools
```

### Installing from source for development
Clone the repository and link via setuptools:
```bash
$ python setup.py develop
```

### Adding to your openaps project
```bash
$ openaps vendor add openapscontrib.mmglucosetools
$ openaps device add glucose mmglucosetools
```

## Usage
Use the device help menu to see available commands.
```bash
$ openaps use glucose -h
```

Use the command help menu to see available arguments.
```bash
$ openaps use glucose latest -h
```

## Contributing
Contributions are welcome and encouraged in the form of bugs and pull requests.

### Testing
 
Unit tests can be run manually via setuptools.
 
```bash
$ python setup.py test
```
