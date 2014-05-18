#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ head -n 2 address.txt

import sys

N = int(sys.argv[1])

with open("./address.txt") as f:
    for i, line in enumerate(f):
        if i >= N:
            sys.exit()
        print(line, end="")
