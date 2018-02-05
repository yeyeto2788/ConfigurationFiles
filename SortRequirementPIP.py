#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from optparse import OptionParser

"""
EXECUTE THE CODE
"""

def printError(pstrRawData):
    """
    Prints the error in a specific format.

    Args:
        pstrRawData: String that would be display on the terminal

    Returns:
        Nothing.
    """
    if sys.platform == "win32":
        RED = ""
        DEFAULT = ""
    else:
        RED = "\x1b[01;05;37;41m"
        DEFAULT = "\x1b[0m"
    print(RED + "ERROR INI {:*<20}".format("*") + DEFAULT)
    print(">>> " + str(pstrRawData))
    print("ERROR END {:*<20}".format("*"))

def orderPIPFile(pstrFileName):
    """
    This is function where the actual magic happens, takes the given file and modifies it to be sorted alphabetically.

    Args:
        pstrFileName: String with the name of the file.

    Returns:
        Nothing.
    """
    Data = []
    if os.path.exists(os.path.abspath(pstrFileName)):
        fileDirectory = os.path.normpath(os.path.abspath(pstrFileName))
        with open(fileDirectory, "r") as f:
            for line in f.readlines():
                Data.append(line.rstrip())

        SortedData = sorted(Data, key=str.lower)
        f.close()

        with open(fileDirectory, "w") as g:
            for i in range(0, len(SortedData)):
                g.write(SortedData[i] + "\n")
        g.close()
        print("The file {} was correctly sorted.".format(pstrFileName))
    else:
        printError("The directory does not exists. The file received was {}".format(pstrFileName))



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
