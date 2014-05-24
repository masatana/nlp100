#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("./address.txt") as f:
    f_cache = f.read().strip().split("\n")
    print("\n".join(line for line in sorted(f_cache, key = lambda x: x.split("\t")[1])))
