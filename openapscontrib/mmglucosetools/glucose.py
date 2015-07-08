from dateutil.parser import parse


def _filter_entry(entry):
    if 'date' in entry:
        entry['date'] = parse(entry['date'])

        if 'sgv' in entry and entry['sgv'] > 0:
            return True
        elif 'amount' in entry and entry['amount'] > 0:
            return True

    return False


def _stringify_dates(entry):
    entry['date'] = entry['date'].isoformat()

    return entry


def clean(glucose_entries):
    """Resolve inconsistencies and ordering from a sequence of pump history

    :param glucose_entries: A list of glucose entries
    :type glucose_entries: list(dict)
    :return: Cleaned glucose entries in reverse-chronological order
    :rtype: list(dict)
    """
    cleaned = filter(_filter_entry, glucose_entries)

    return map(_stringify_dates, sorted(cleaned, cmp=lambda x, y: x['date'] > y['date']))
