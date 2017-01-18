import os
import sys

filename = sys.argv[1]
base_filename = filename[:-4]

# convert the geometry to XML form
os.system("~/projects/VERA/VERAInExt/verain/scripts/react2xml.pl {0} {1}.xml".format(filename, base_filename))

# add create_unique_pins parameter
os.system("python ~/projects/nkq_analysis/python-scripts/insert-create-unique-pins.py {0}.xml".format(base_filename))

# run the vera_to_shift executable
os.system("mpirun -np 12 ~/builds/PSSDriversExt/VeraShift/src/vera_to_shift --case=\"{0}\"".format(base_filename))

# extract the fission source
os.system("python ~/projects/nkq_analysis/python-scripts/extract-fission-source.py {0}.shift.h5".format(base_filename))
