#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser

"""
EXECUTE THE CODE
"""

def orderPIPFile(pstrFileName):
    Data = []
    with open(pstrFileName, "r") as f:
        for line in f.readlines():
            Data.append(line.rstrip())

    SortedData = sorted(Data, key=str.lower)
    f.close()

    with open(pstrFileName, "w") as g:
        for i in range(0, len(SortedData)):
            g.write(SortedData[i] + "\n")
    g.close
    print("The file {} was correctly sorted.".format(pstrFileName))



def main():
    usage = "Usage: %prog [options] <arguments>"
    parser = OptionParser(usage, version="%prog 0.1")
    parser.add_option("-i", "--input",
                      action="store",
                      type="string", dest="filename",
                      help="Input file name to order alphabetically the requirements. (This is mandatory")
    (options, args) = parser.parse_args()

    mandatories = ['filename']

    if len(sys.argv[1:]) == 0:
        parser.error("\nSeems like there is no enough arguments.\nPlease type {} --help for more information.".format(__file__))
        parser.print_help()
        exit(-1)
    else:
        for m in mandatories:
            if not options.__dict__[m]:
                printError("There are arguments missing.")
                parser.print_help()
                exit(-1)
        if options.filename:
            print("\nSorting the {} file.\n".format(options.filename))
            orderPIPFile(options.filename)
        else:
            printError("You have to specify the input file name.")

if __name__ == "__main__":
    main()
