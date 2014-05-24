#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

with open("./inflection.table.txt") as f:
    dic = {}
    for line in f:
        word, pos, _, inflection, _, _, base, _ = line.strip().split("|")
        dic[word] = (pos, inflection, base,)

inpt = sys.argv[1]

print(dic[inpt])
