import sys
import os
import h5py as h5
from omnibus.formats.comp import Compositions
from robus import load_hdf5_compositions, Nuclide_Metadata, Composition
import glob

# Count number of different state composition files
files = glob.glob('*state_*_compositions.h5')
num_files = len(files)

Nuclide_Metadata.load_SCL()

# The syntax for defining a custom material is:
#
# custom_mat_name = Composition(temperature in Kelvin, \
#                               [zaids],\
#                               [number densities] (atoms/barn-cm),\
#                               fissionable? (TRUE or FALSE (default)),\
#                               depletable? (TRUE or FALSE (default)))

# CUSTOM MATERIAL DEFINITIONS
waterfuel = Composition(300.0, [92235, 1002, 8016, 8017], [6.67e-1, 7.67e-6, 3.32e-2, 1.26e-5])
A533B = Composition(600.0, [26000, 28000, 25000, 6000], [0.0826629819844095, 0.0004418614290647755, 0.0011157909201793218, 0.000981486568441265])
SS394 = Composition(600.0, [26000, 28000, 24000, 25000], [0.059749083796901956, 0.008239050912318932, 0.017670518184104, 0.0017604481951154249])
concrete = Composition(600.0, [26000, 6000, 14000, 20000, 19000, 13000, 12000, 11000, 8000, 1000], [0.000937154895116098, 0.00011406804307554929, 0.016629421894907362, 0.0015041077393724734, 0.00045903492707033937, 0.001741645302085446, 0.00012401075905897963, 0.0009654120547480707, 0.04324341585988146, 0.006932147676780611])


# put custom materials in a list for appending
custom_mats = [waterfuel]

#try:
# expects only the base file name (i.e. before the .shift_state_<n>_compositions.h5 extension)
base_filename = sys.argv[1]

try:
	for i in range(num_files):
	    new_extension = ".shift_state_" + str(i) + "_compositions-custom.h5"
	    old_extension = ".shift_state_" + str(i) + "_compositions.h5"
	    filename_out = base_filename + new_extension
	    filename_in = base_filename + old_extension

	    # load in the HDF5 file
	    comps = load_hdf5_compositions(filename_in)
	    original_number = len(comps)
	    matid_number = original_number

	    # convert comps to a list of dictionaries
	    comps_list = [c._asdict() for c in comps]

	    # add names for all the VERA materials (no names are defined on the VERA side)
	    matid = 0
	    for c in comps_list:
		c['name'] = matid
		matid += 1

	    # add custom materials not already in the HDF5 file
	    for material in custom_mats:
		comps_list.append(material._asdict())

		# adjust the material IDs to increase sequentially from the matids
		# in the original input
		added = comps_list[-1]
		added['matid'] = matid_number

		# add names for all the new materials
		added['name'] = matid_number
		matid_number += 1

	    final_number = len(comps_list)

	    # convert comps_list from a list of dictionaries to a HDF5 compatible type
	    h5_c = Compositions.from_list(comps_list)

	    # dump to HDF5. Because the output file is a different name, repeated
	    # application of this script to the same composition input file should not
	    # produce repeated custom materials in the output HDF5 file.
	    with h5.File(filename_out, 'w') as f:

		h5_c.dump(f)
		new = final_number - original_number
		print("Wrote {0} new material{1}!".format(new, '' if new == 1 else 's'))

	    # copy over the metadata from the first compositions file, since this is required 
	    # for pulling in compositions to Jupyter Notebook
	    os.system("h5copy -i {0} -s metadata -o {1} -d metadata".format(filename_in, filename_out))

except:
    print("""Error: the usage of this script requires the following syntax:\n
          python add-comps.py <file>.shift_compositions.h5\n
          This script should be run from the location containing the input.""")
            
