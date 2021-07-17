#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 Sotiris Papatheodorou
# SPDX-License-Identifier: BSD-2-Clause

import json
import sys

if len(sys.argv) == 1:
    print("Usage: " + sys.argv[0] + " FILE")
    print("Read emoji data from a JSON file downloaded from")
    print("https://github.com/iamcal/emoji-data and print a")
    print("Python dictionary for use in weemoji.py on stdout.")
    print("This is the direct URL to the JSON file:")
    print("https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json")
    sys.exit()

with open(sys.argv[1]) as f:
    print({e['short_name']:e['unified'] for e in json.load(f)})

