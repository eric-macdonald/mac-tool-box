#!/Users/eric.w.macdonald/miniconda2/bin/python
import grammar_check
import sys
import os
import fileinput
import string
import shutil

start1 = 0
start2 = 0
finish = 0
index = 0

#shutil.copyfile(fileToSearch, 'temp.pdf')
#os.system("pdf2txt.py temp.pdf > temp.txt")
f = open("final.txt","w+")

for line in fileinput.input('abs.txt'):
    index = index + 1
 #   line = line.decode("ascii", errors="ignore").encode()
    if (index < 50):
#        print line.rstrip()
        print "Abstract" in line
        print "\n"
    if "Abstract" in line:
        if(start1):
            print '#########start2'
            start2 = 1
        else:
            print '#########start1'
            start1 = 1
    if 'Intro' in line:
        print '#########intro'
        start2 = 1
    if 'References' in line:
        print '#########references'
        finish = 1
    if 'Acknowl' in line:
        finish = 1
    if(start2 and not finish):
#        line = line.rstrip()
        f.write(line)
#        if len(line):
#            tool = grammar_check.LanguageTool('en-US')
#            matches = tool.check(line)
#            if len(matches):
#                if matches[0].ruleId == "UPPERCASE_SENTENCE_START":
#                    pass
#                elif matches[0].ruleId == "COMMA_PARENTHESIS_WHITESPACE":
#                    pass
#                elif matches[0].ruleId == "EN_UNPAIRED_BRACKETS":
#                    pass
#                elif matches[0].ruleId == "WHITESPACE_RULE":
#                    pass
#                else:
#                    pass
#                    print matches[0].ruleId, matches[0].context

f.close()
