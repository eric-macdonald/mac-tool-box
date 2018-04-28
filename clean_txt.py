#!/Users/eric.w.macdonald/miniconda2/bin/python
import grammar_check
import sys
import os
import re
import fileinput
import string

startword = None
start = 0
finish = 0
index = 0
#os.system("iconv -f utf-16 -t utf-8 abs.txt > abs2.txt")
os.system("pdf2txt.py abs.pdf > abs2.txt")

outf = open("final.txt", "w")
with open("abs2.txt",'r')  as inf:
    for line in inf:
        index = index + 1
        match1 = re.search(r"^\s*(\S+)\s+(.*)", line)
        match2 = re.search(r"(.*)\s(\S+)\-$", line)
        match3 = re.search(r"(^\s*[0-9]+)\s*", line)
        match4 = re.search(r"^\s*Fig.*", line)
        if(startword is not None and match1 is not None and match2 is None and match3 is None and match4 is None):
           endword = match1.group(1)
           oldline = match1.group(2)
           if(startword):
               newline = startword+endword + " " + oldline.rstrip() + " "
               startword = None
           else:
               newline = oldline.rstrip() + " "
        elif(match1 is not None and match2 is None and match3 is None and match4 is None):
            newline = line.rstrip() + " "

        if(match2 is not None):
            startword = match2.group(2)
            newline = match2.group(1) + " "

        if(match3 is not None):
            newline = ' '

        if(match4 is not None):
            newline = ' '

        if "Introduction" in line:
            start = 1
        if "References" in line:
            finish = 1
        if "Acknowledgment" in line:
            finish = 1
        if(start and not finish):
            newline = re.sub('\f','', newline)
            outf.write(newline)
