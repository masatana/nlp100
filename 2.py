#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ TODO

with open("./address.txt") as f:
    for line in f:
        print(line.strip().replace("\t", " "))
