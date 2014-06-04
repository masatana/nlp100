#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import Counter
import porter2

def ngrams(text, n):
    for i in range(len(text) - n + 1):
        yield text[i:i+n]

def oldngrams(text, n):
    for i in range(len(text)):
        for j in range(i + n, min(len(text), i + n) + 1):
            yield text[i:j]

def normalize():
    with open("./medline.txt") as f, open("./new_medline.txt", "w") as g:
        for line in f:
            if line.endswith(".\n"):
                g.write(line)

def twentyone():
    with open("./medline.txt") as f:
        for line in f:
            print(".\n".join(line.strip().split(". ")), end="")

def twentytwo():
    p = re.compile(r"\. [A-Z]")
    with open("./medline.txt") as f:
        for line in f:
            i = 0
            for m in p.finditer(line):
                yield line[i:m.start()+1]
                i = m.start()+2
            yield line[i:]

def twentythree():
    for sentence in twentytwo():
        print("\n".join(word for word in sentence.strip().split()))
        print()

def twentyfour():
    p = re.compile(r"(\w+)")
    for sentence in twentytwo():
        words = [word for word in sentence.strip().split()]
        for word in words:
            match = p.split(word)
            yield "".join(match[:-1])
            if match[-1] != "":
                yield match[-1]

def twentyfive():
    for token in twentyfour():
        #print(token + "\t" + token.lower())
        print(token.lower())

def twentysix():
    with open("./medline.txt.send.tok") as f:
        for token in f:
            token = token.strip()
            if token.endswith("less") or token.endswith("ly"):
                print(token)

def twentyseven():
    with open("./medline.txt.send.tok") as f:
        counter = Counter(token.strip() for token in f)
        print(counter.most_common(10))

def twentyeight():
    with open("./medline.txt.send.tok") as f:
        counter = Counter(bigram for token in f for bigram in ngrams(token.strip(), 2))
        print(counter.most_common(10))

def twentynine():
    pass

def thirty():
    with open("./medline.txt.send.tok") as f:
        for token in f:
            print(porter2.stem(token.strip()))
if __name__ == "__main__":
    #normalize()
    #twentyone()
    #twentytwo()
    #twentythree()
    #twentyfour()
    twentyfive()
    #twentysix()
    #twentyseven()
    #twentyeight()
    #twentynine()
    #thirty()
