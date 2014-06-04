#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml import sax

class Handler(sax.handler.ContentHandler):
    _is_abstract_text = False
    def startElement(self, name, attrs):
        if name == "AbstractText":
            self._is_abstract_text = True

    def endElement(self, name):
        pass

    def characters(self, content):
        if self._is_abstract_text:
            with open("./medline.txt", "a") as f:
                f.write(content+"\n")
            self._is_abstract_text = False

if __name__ == "__main__":
    handler = Handler()
    sax.parse("./pubmed_result.xml", handler)

