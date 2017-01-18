import sys

filename = sys.argv[1]

base_filename = filename[:-7]

find = "rtk_fuel"
replace = "core-array"

with open(filename, 'r') as fi:
    with open(base_filename + "-replaced.gg.xml", 'w') as fo:
        print("Performing find-and-replace of {0} by {1}".format(find, replace))
	for line in fi:
            fo.write(line.replace(find, replace))
