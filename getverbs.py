#!/usr/bin/env python
'''
Use https://ankiweb.net/shared/info/1589071665 to export cards from Anki (once
installed you can find plugin in Tools menu).

Use following settings:
- JSON
- limit to deck and tag you want
- unset ALL include settings
'''

import codecs
import json
import sys


# Name of the field to use
field = 'Spanish'


def flatten_list(items):  # Flatten list of lists
    return [item for sublist in items for item in sublist]


def read_file(filename):
    items = []
    with open(filename, 'r') as f:
        items = json.load(f)
    return items


def clean_value(value):
    value = value.strip()
    value = value.split(" ")[0]  # Spanish verbs are one word only
    if "(" in value and value[-1] == ")":
        v, p = value.split("(")
        value = [v, v+p[:-1]]  # e.g. cuidar, cuidarse
    else:
        value = [value]
    return value


def clean_field(field_value):
    value = field_value.replace('/', ',').replace('&nbsp;', ' ')
    values = [clean_value(v) for v in value.split(',')]
    return flatten_list(values)


def get_fields(items):
    for item in items:
        if item:
            yield clean_field(item[field])


def save_verbs(verbs):
    with codecs.open('verbs.txt', encoding='utf-8', mode='w') as f:
        for verb in verbs:
            f.write(verb + '\n')


def main(filename):
    verbs = []
    items = read_file(filename)
    verbs = flatten_list(get_fields(items))
    verbs = list(set(verbs)) # Deduplicate
    verbs.sort()
    save_verbs(verbs)


if __name__ == '__main__':
    f = sys.argv[1]
    main(f)
