import json
import os
import unittest

from openapscontrib.mmglucosetools.glucose import clean


def get_file_at_path(path):
    return "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), path)


class CleanTestCase(unittest.TestCase):
    def test_clean_values(self):
        with open(get_file_at_path('fixtures/iter_glucose.json')) as fp:
            glucose = json.load(fp)

        cleaned = clean(glucose)

        self.assertListEqual(
            [
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 2,
                    "sgv": 150,
                    "date": "2015-07-06T18:10:00",
                    "packet_size": 0,
                    "op": 75
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 11,
                    "sgv": 150,
                    "date": "2015-07-06T18:09:00",
                    "packet_size": 0,
                    "op": 75
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 12,
                    "sgv": 148,
                    "date": "2015-07-06T18:04:00",
                    "packet_size": 0,
                    "op": 74
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 29,
                    "sgv": 144,
                    "date": "2015-07-06T17:55:00",
                    "packet_size": 0,
                    "op": 72
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 30,
                    "sgv": 142,
                    "date": "2015-07-06T17:50:00",
                    "packet_size": 0,
                    "op": 71
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 31,
                    "sgv": 138,
                    "date": "2015-07-06T17:45:00",
                    "packet_size": 0,
                    "op": 69
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 32,
                    "sgv": 136,
                    "date": "2015-07-06T17:40:00",
                    "packet_size": 0,
                    "op": 68
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 33,
                    "sgv": 132,
                    "date": "2015-07-06T17:35:00",
                    "packet_size": 0,
                    "op": 66
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 42,
                    "sgv": 132,
                    "date": "2015-07-06T17:29:00",
                    "packet_size": 0,
                    "op": 66
                },
                {
                    "name": "GlucoseSensorData",
                    "date_type": "prevTimestamp",
                    "_tell": 43,
                    "sgv": 132,
                    "date": "2015-07-06T17:24:00",
                    "packet_size": 0,
                    "op": 66
                }
            ],
            cleaned[0:10]
        )

        for entry in cleaned:
            self.assertIn(entry['name'], ('GlucoseSensorData', 'CalBGForGH'))
