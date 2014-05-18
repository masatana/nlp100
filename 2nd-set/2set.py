#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re
import tarfile

def experiment(extracted):
    with tarfile.open("./tweets.tar.gz") as f:
        for i, line in enumerate(f.extractfile(f.getmember("tweets.txt"))):
            if i > 100:
                print(sys.getdefaultencoding())
                sys.exit()
            print(line.decode("utf-8"))

def eleven(extracted):
    for i, line in enumerate(extracted):
        j = json.loads(line)
        if "拡散希望" in j["text"]:
            print(j["text"])

def twelve(extracted):
    for i, line in enumerate(extracted):
        if i > 1000:
            sys.exit()
        j = json.loads(line)
        if j["text"].endswith("なう"):
            print(j["text"])

def thirteen(extracted):
    # http://nanapi.jp/34520/
    # 自信なし
    for i, line in enumerate(extracted):
        if i > 1000:
            sys.exit()
        j = json.loads(line)
        if " RT " in j["text"]:
            print(j["text"].split(" RT ")[0])

def fourteen(extracted):
    p = re.compile("@\w+")
    for i, line in enumerate(extracted):
        if i > 100:
            sys.exit()
        j = json.loads(line.decode("utf-8"))
        try:
            print(p.match(j["text"]).group())
        except:
            continue

def fifteen(extracted):
    p = re.compile("(@(\w+))")
    for i, line in enumerate(extracted):
        if i > 100:
            sys.exit()
        j = json.loads(line.decode("utf-8"))
        if p.match(j["text"]):
            print(p.sub("<a href=\"https://twitter.com/#!/\\2\">\\1</a>", j["text"]))

def sixteen(extracted):
    # TODO 複数ある場合に対応 (e.g. test.txt line 18)
    p = re.compile("([一-龠]+)([\(\[（「][A-Z]+[[\)\]）」])")
    for i, line in enumerate(extracted):
        if i > 100:
            sys.exit()
        j = json.loads(line.decode("utf-8"))
        match = p.search(j["text"])
        if match:
            print(match.group(1) + "\t" + match.group(2))

def seventeen(extracted):
    p = re.compile("([一-龠]+(さん|様|くん|君|先生))")
    for i, line in enumerate(extracted):
        if i > 100:
            sys.exit()
        j = json.loads(line.decode("utf-8"))
        match = p.search(j["text"])
        if match:
            print(match.group())

def eighteen(extracted):
    pass

if __name__ == "__main__":
    with tarfile.open("./test.tar.gz") as f:
        extracted = f.extractfile("test.txt")
        #experiment(extracted)
        #eleven(extracted)
        #twelve(extracted)
        #thirteen(extracted)
        #fourteen(extracted)
        #fifteen(extracted)
        #sixteen(extracted)
        #seventeen(extracted)
        eighteen(extracted)
