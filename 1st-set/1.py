#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ wc -l address.txt

with open("./address.txt") as f:
    print(len(f.read().strip().split("\n")))
