def _filter_entry(entry):
    if ('date' in entry) or ('display_time' in entry):
        if 'sgv' in entry and entry['sgv'] > 0:
            return True
        elif 'amount' in entry and entry['amount'] > 0:
            return True
        elif 'glucose' in entry and entry['glucose'] > 0:
            return True

    return False


def clean(glucose_entries):
    """Resolve inconsistencies and ordering from a sequence of pump history

    :param glucose_entries: A list of glucose entries
    :type glucose_entries: list(dict)
    :return: Cleaned glucose entries in reverse-chronological order
    :rtype: list(dict)
    """
    cleaned = filter(_filter_entry, glucose_entries)
    if 'date' in cleaned[0]:
        return sorted(cleaned, key=lambda x: x['date'], reverse=True)
    elif 'system_time' in cleaned[0]:
        return sorted(cleaned, key=lambda x: x['display_time'], reverse=True)
    else
        print "Something is amiss ..."
