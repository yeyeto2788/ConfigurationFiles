#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
EXECUTE THE CODE
"""


Data = []
with open("RequirementsPIP.txt", "r") as f:
    for line in f.readlines():
        Data.append(line.rstrip())

SortedData = sorted(Data, key=str.lower)
f.close()

with open("RequirementsPIP.txt", "w") as g:
    for i in range(0, len(SortedData)):
        g.write(SortedData[i] + "\n")
g.close
