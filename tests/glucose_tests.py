import json
import os
import unittest

from openapscontrib.glucosetools.glucose import clean


def get_file_at_path(path):
    return "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), path)


class CleanTestCase(unittest.TestCase):
    def test_clean_values_mm(self):
        # test for mm
        with open(get_file_at_path('fixtures/iter_glucose_mm.json')) as fp:
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
                    "body": "63",
                    "packet_size": 5,
                    "amount": 99,
                    "name": "CalBGForGH",
                    "raw": "53-cd-0a-8f-63",
                    "date": "2015-07-06T18:07:00",
                    "date_type": "minSpecific",
                    "_tell": 18,
                    "op": "0x0e"
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
                }
            ],
            cleaned[0:10]
        )

        for entry in cleaned:
            self.assertIn(entry['name'], ('GlucoseSensorData', 'CalBGForGH'))

    def test_clean_values_dex(self):
        # test for dex
        with open(get_file_at_path('fixtures/iter_glucose_dex.json')) as fp:
            glucose = json.load(fp)

        cleaned = clean(glucose)

        self.assertListEqual(
            [
              {
                "trend_arrow": "FLAT",
                "system_time": "2015-08-25T18:05:23",
                "display_time": "2015-08-25T10:06:15",
                "glucose": 86
              },
              {
                "trend_arrow": "FLAT",
                "system_time": "2015-08-25T18:00:23",
                "display_time": "2015-08-25T10:01:15",
                "glucose": 89
              },
              {
                "trend_arrow": "FLAT",
                "system_time": "2015-08-25T15:45:23",
                "display_time": "2015-08-25T07:46:15",
                "glucose": 94
              },
              {
                "trend_arrow": "FLAT",
                "system_time": "2015-08-25T15:40:23",
                "display_time": "2015-08-25T07:41:15",
                "glucose": 94
              },
              {
                "trend_arrow": "FLAT",
                "system_time": "2015-08-25T15:35:23",
                "display_time": "2015-08-25T07:36:15",
                "glucose": 97
              },
              {
                "trend_arrow": "NOT_COMPUTABLE",
                "system_time": "2015-08-21T02:35:38",
                "display_time": "2015-08-20T18:36:30",
                "glucose": 134
              },
              {
                "trend_arrow": "NOT_COMPUTABLE",
                "system_time": "2015-08-21T02:30:38",
                "display_time": "2015-08-20T18:31:30",
                "glucose": 132
              },
              {
                "trend_arrow": "NOT_COMPUTABLE",
                "system_time": "2015-08-21T02:25:38",
                "display_time": "2015-08-20T18:26:30",
                "glucose": 129
              },
              {
                "trend_arrow": "NOT_COMPUTABLE",
                "system_time": "2015-08-21T01:30:39",
                "display_time": "2015-08-20T17:31:30",
                "glucose": 245
              },
              {
                "trend_arrow": "45_UP",
                "system_time": "2015-08-21T01:25:39",
                "display_time": "2015-08-20T17:26:30",
                "glucose": 242
              }
            ],
            cleaned[0:10]
        )


if __name__ == "__main__":
    unittest.main()
