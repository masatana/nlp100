#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def main():
    with open("./tweets.tweet", encoding = "utf-8") as f, open("tweets.txt", "a") as g:
        tmp = ""
        normalized_tweets = []
        for i, line in enumerate(f):
            if line.endswith("}\n"):
                g.write(tmp + line)
                tmp = ""
            else:
                tmp += line[:-1]

if __name__ == "__main__":
    main()
