"""
glucosetools - tools for cleaning, condensing, and reformatting history data


"""
from .version import __version__

import argparse
import json

from openaps.uses.use import Use

from glucose import clean as clean_glucose


# set_config is needed by openaps for all vendors.
# set_config is used by `device add` commands so save any needed
# information.
# See the medtronic builtin module for an example of how to use this
# to save needed information to establish sessions (serial numbers,
# etc).
def set_config(args, device):
    # no special config
    return


# display_device allows our custom vendor implementation to include
# special information when displaying information about a device using
# our plugin as a vendor.
def display_device(device):
    # no special information needed to run
    return ''


# openaps calls get_uses to figure out how how to use a device using
# agp as a vendor.  Return a list of classes which inherit from Use,
# or are compatible with it:
def get_uses(device, config):
    return [clean, latest]


def _opt_json_file(filename):
    """Parses a filename as JSON input if defined

    :param filename: The path to the file to parse
    :type filename: basestring
    :return: A decoded JSON object if a filename was specified
    :rtype: dict|list|NoneType
    """
    if filename:
        return json.load(argparse.FileType('r')(filename))


class BaseUse(Use):
    def configure_app(self, app, parser):
        """Define command arguments.

        Only primitive types should be used here to allow for serialization and partial application
        in via openaps-report.
        """
        parser.add_argument(
            'infile',
            nargs=argparse.OPTIONAL,
            default='-',
            help='JSON-encoded glucose data'
        )

    def get_params(self, args):
        return dict(infile=args.infile)

    def get_program(self, params):
        """Parses params into history parser constructor arguments

        :param params:
        :type params: dict
        :return:
        :rtype: tuple(list, dict)
        """
        return [json.load(argparse.FileType('r')(params['infile']))], dict()


# noinspection PyPep8Naming
class latest(BaseUse):
    """Returns the latest glucose entry from a sequence of glucose data"""

    def main(self, args, app):
        args, _ = self.get_program(self.get_params(args))

        cleaned = clean_glucose(*args)
        return cleaned[0] if len(cleaned) > 0 else None


# noinspection PyPep8Naming
class clean(BaseUse):
    """Resolve inconsistencies and ordering from a sequence of glucose data

Tasks performed by this pass:
 - Removes unknown and erroneous data entries
 - Re-sorts all known values in reverse-chronological order
    """
    def main(self, args, app):
        args, _ = self.get_program(self.get_params(args))

        return clean_glucose(*args)
