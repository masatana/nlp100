#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ cut -f 1 address.txt | sort | uniq | wc -l

with open("./address.txt") as f:
    col1 = set(line.split("\t")[0] for line in f.read().strip().split("\n"))
    print(len(col1))
