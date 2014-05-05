#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ cat col2.txt | sort | uniq -c | sort -r | head -n 10

from collections import Counter

with open("./col2.txt") as f:
    col2 = Counter(f.read().strip().split())
    for line in col2.most_common(10):
        print(line[0])
