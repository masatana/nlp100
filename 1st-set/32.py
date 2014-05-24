#!/usr/bin/env python
# -*- coding: utf-8 -*-

import marshal

with open("./inflection.table.txt") as f:
    dic = {}
    for line in f:
        word, pos, _, inflection, _, _, base, _ = line.strip().split("|")
        dic[word] = (pos, inflection, base,)

with open("./inflection.dic", "wb") as f:
    marshal.dump(dic, f)
