import os
import sys

filename = sys.argv[1]
base_filename = filename[:-4]

print(base_filename)

print("Adding new compositions to {0}.shift_compositions.h5".format(base_filename))
os.system("python ~/projects/nkq_analysis/python-scripts/add-comps.py {0}".format(base_filename))

print("Generating XML version of GG file")
os.system("~/install/bin/gg2xml {0}.gg.omn".format(base_filename))

print("Renaming generated XML file")
os.system("mv {0}.gg.gg.xml {0}.gg.xml".format(base_filename))

#os.system("python ~/projects/nkq_analysis/python-scripts/find-replace.py {0}.gg.xml rtk_fuel core-array".format(base_filename))

#os.system("mv {0}-replaced.gg.xml {0}.gg.xml".format(base_filename))

os.system("omnibus-run {0}.omn".format(base_filename))


os.system("python ~/projects/nkq_analysis/python-scripts/find-replace-path.py {0}.gg.xml /home/nkq/ /Users/aprilnovak/Mounts/orthanc/".format(base_filename))

# still have to swap out rtk_fuel with core-array for viewing with Notebook, even after Tom's fix
os.system("python ~/projects/nkq_analysis/python-scripts/find-replace.py {0}-notebook.gg.xml rtk_fuel core-array".format(base_filename))

# perform unneccessary clean up actions
os.system("rm *omnibus-2017* *2017*.rst *.inp-2017* *.out-2017* *.json *.mesh_tally-2017*")
