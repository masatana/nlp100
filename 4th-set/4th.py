#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter
try:
    import cPickle as pickle
except ImportError:
    import pickle
import leveldb

def thirtyone():
    m = {}
    with open("./inflection.table") as f:
        for line in f:
            tokens = [token for token in line.strip().split("|")]
            m[tokens[0]] = (tokens[1], tokens[2], tokens[6],)
    with open("./inflection.pickle", "wb") as f:
        pickle.dump(m, f)

def thirtytwo():
    with open("./inflection.pickle", "rb") as f:
        m = pickle.load(f, encoding = "utf-8")
    print(m["AAA"])

def thirtysix():
    with open("../3rd-set/medline.txt.send.tok") as f:
        previous_line = None
        for line in f:
            if previous_line is None:
                previous_line = line.strip()
                continue
            line_strip = line.strip()
            if line_strip == "":
                previous_line = None
                continue
            yield previous_line + "\t" + line_strip
            previous_line = line_strip

def thirtyseven():
    p = Counter()
    pall = Counter()
    for line in thirtysix():
        tok1, tok2 = line.strip().split("\t")
        p[(tok1, tok2)] += 1
        pall[tok1] += 1
    """
    for line in thirtysix():
        tok1, tok2 = line.strip().split("\t")
        #print("{}\t{}\t{}".format(p[(tok1, tok2)] / pall[tok1], tok1, tok2))
        p[(tok1, tok2)] /= pall[tok1]
    """
    return p, pall

def thirtynine():
    _leveldb = leveldb.LevelDB("./leveldb")
    p, pall = thirtyseven()
    for k, v in p.items():
        _leveldb.Put(bytes("\t".join(k), "utf-8"), bytes(str(v / pall[k[0]]), "utf-8"))

def test():
    _leveldb = leveldb.LevelDB("./leveldb")
    print(_leveldb.Get(bytes("this\tis", "utf-8")))

if __name__ == "__main__":
    #thirtyone()
    #thirtytwo()
    #thirtysix()
    #thirtyseven()
    #thirtynine()
    test()
