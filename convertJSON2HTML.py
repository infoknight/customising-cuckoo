#!/usr/bin/env python
from json2html import *
import json

def main():
    fin = open("report.json","r")
    input = ""
    for line in fin:
        input = input + line

    result = json2html.convert(json = input)

    fout = open("report.html","w")
    fout.write("<html>")
    fout.write("<body>")
    fout.write(result)
    fout.write("</body>")
    fout.write("</html>")
    fout.close()
    return

if __name__ == "__main__":
    main()
