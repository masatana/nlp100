#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

with open("./address.txt") as f:
    f_dic = defaultdict(list)
    for line in f:
        col1, col2  = line.split("\t")
        f_dic[col2].append(col1)
    for k in sorted(f_dic):
        for v in sorted(f_dic[k]):
            print(v + "\t" + k, end="")
