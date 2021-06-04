#!/usr/bin/env python3

import random
import sys

if len(sys.argv) > 1:
    options = sys.argv[1:]
    selection = random.choice(options)
    print(selection)
else:
    print("Please supply one or more options!")
