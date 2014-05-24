#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ paste col1.txt col2.txt

with open("./col1.txt") as col1, open("./col2.txt") as col2:
    col1_cache = col1.read().strip().split("\n")
    col2_cache = col2.read().strip().split("\n")
    restored_address = "\n".join([foo + "\t" + bar for foo, bar in zip(col1_cache, col2_cache)])
    with open("./restored_address.txt", "w") as f:
        f.write(restored_address)
