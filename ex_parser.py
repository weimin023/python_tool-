import os
import os.path

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', help = 'input & output file name', nargs=2)
args = parser.parse_args()

print (args.o)