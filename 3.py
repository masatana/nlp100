#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ cut -f 1 address.txt  && cut -f 2 address.txt

with open("./address.txt") as f:
    f_cache = f.read().strip().split("\n")
    col1 = [line.split("\t")[0] for line in f_cache]
    col2 = [line.split("\t")[1] for line in f_cache]
    with open("./col1.txt", "w") as g:
        g.write("\n".join(col1))
    with open("./col2.txt", "w") as h:
        h.write("\n".join(col2))
