#!/Users/eric.w.macdonald/miniconda2/bin/python
import grammar_check
import sys
import fileinput
import string

start1 = 0
start2 = 0
finish = 0
index = 0
country = sys.argv[1]
fileToSearch = sys.argv[2]
for line in fileinput.input(fileToSearch):
    index = index + 1
    line = line.decode("ascii", errors="ignore").encode()
    print line
    if 'Abstract' in line:
        print 'found abstract'
        if start1:
            start2 = 1
        else:
            start1 = 1
    if 'References' in line:
        print 'found references'
        finish = 1
    if(start2 and not finish):
        print index
        if len(line):
            if country == 'b':
                tool = grammar_check.LanguageTool('en-GB')
            if country == 'a':
                tool = grammar_check.LanguageTool('en-US')
            matches = tool.check(line)
            if len(matches):
                if matches[0].ruleId == "UPPERCASE_SENTENCE_START":
                    pass
                elif matches[0].ruleId == "COMMA_PARENTHESIS_WHITESPACE":
                    pass
                elif matches[0].ruleId == "EN_UNPAIRED_BRACKETS":
                    pass
                elif matches[0].ruleId == "WHITESPACE_RULE":
                    pass
                else:
                    print matches[0].ruleId, matches[0].context

print "done"
