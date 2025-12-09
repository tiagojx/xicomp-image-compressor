#!/usr/bin/env python
'''
    Convert a generic image file to .webp
    Can handle multiple files via command line arguments.
'''

import os, sys
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", type=str)
parser.add_argument("-o", "--output", default="", type=str)
args = parser.parse_args()

outpath = ""
try:
    outpath = os.path.relpath(args.output)
except ValueError:
    outpath = ""

try:
    for raw_infile in args.files:
        infile = raw_infile.split("/")[1]
        filename, _ext = os.path.splitext(infile)
        outfile = filename + ".webp"
        if infile != outfile:
            try:
                with Image.open(raw_infile) as im:
                    if outpath != "":
                        im.save(f"{outpath}/{outfile}")
                    else:
                        im.save(outfile)
            except OSError:
                print("Cannot convert", infile)
            else:
                print(f"{filename} has been successfully converted!")
except IndexError:
    print("No argument was provided.")
finally:
    print("Finished.")
