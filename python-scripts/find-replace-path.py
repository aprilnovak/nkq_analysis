import sys

filename = sys.argv[1]

base_filename = filename[:-7]

print(base_filename)

find = sys.argv[2]
replace = sys.argv[3]

with open(filename, 'r') as fi:
    with open(base_filename + "-notebook.gg.xml", 'w') as fo:
        print("Performing find-and-replace of {0} by {1}".format(find, replace))
        for line in fi:
            fo.write(line.replace(find, replace))
