#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $ tail -n 2 address.txt
import sys
N = int(sys.argv[1])
with open("./address.txt") as f:
    f_cache = f.read().strip().split("\n")
    print("\n".join(f_cache[-1 * N:]))
