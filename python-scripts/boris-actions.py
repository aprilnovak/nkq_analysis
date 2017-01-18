import os
import sys

filename = sys.argv[1]
base_filename = filename[:-4]

os.system("~/projects/VERA/VERAInExt/verain/scripts/react2xml.pl {0} {1}.xml".format(filename, base_filename))
