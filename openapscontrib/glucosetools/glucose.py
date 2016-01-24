def _filter_entry(entry):
    if ('date' in entry) or ('display_time' in entry):
        if 'sgv' in entry and entry['sgv'] > 0:
            return True
        elif 'amount' in entry and entry['amount'] > 0:
            return True
        elif 'glucose' in entry and entry['glucose'] > 35:
            return True

    return False

def _rename_entry(entry):
    if 'sgv' in entry:
      entry['glucose'] = entry['sgv']
      del entry['sgv']

    if 'amount' in entry:
      entry['glucose'] = entry['amount']
      del entry['amount']

    if 'date' in entry:
      entry['display_time'] = entry['date']
      del entry['date']

    return entry

def clean(glucose_entries):
    """Resolve inconsistencies and ordering from a sequence of pump history

    :param glucose_entries: A list of glucose entries
    :type glucose_entries: list(dict)
    :return: Cleaned glucose entries in reverse-chronological order
    :rtype: list(dict)
    """
    cleaned = filter(_filter_entry, glucose_entries)
    renamed = map(_rename_entry, cleaned)
    return sorted(renamed, key=lambda x: x.get('date', x.get('display_time')), reverse=True)
