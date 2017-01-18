import sys

filename = sys.argv[1]

base_filename = filename[:-7]

with open(filename, 'r') as fi:
    with open(base_filename + "-replaced.gg.xml", 'w') as fo:
        print(base_filename + "-replaced.gg.xml")
