import sys

filename = sys.argv[1]

base_filename = filename[:-7]

with open(filename, 'r') as fi:
    with open(base_filename + "-replaced.gg.xml", 'w') as fo:
        print("Performing find-and-replace of rtk_fuel by core_array")
	for line in fi:
            fo.write(line.replace("rtk_fuel", "core-array"))
