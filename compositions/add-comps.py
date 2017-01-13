import sys
import h5py as h5
from omnibus.formats.comp import Compositions
from robus import load_hdf5_compositions, Nuclide_Metadata, Composition

Nuclide_Metadata.load_SCL()

# The syntax for defining a custom material is:
#
# custom_mat_name = Composition(temperature in Kelvin, \
#                               [zaids],\
#                               [number densities] (atoms/barn-cm),\
#                               fissionable? (TRUE or FALSE (default)),\
#                               depletable? (TRUE or FALSE (default)))

# CUSTOM MATERIAL DEFINITIONS
water = Composition(300.0, [1001, 1002, 8016, 8017], [6.67e-2, 7.67e-6, 3.32e-2, 1.26e-5])

# put custom materials in a list for appending
custom_mats = [water]

try:
    # expected extension on the file read in by this script
    extension = ".shift_compositions.h5"
    filename = sys.argv[1]
    base_filename = filename[:-len(extension)]
    filename_out = base_filename + ".shift_compositions-custom.h5"

    # load in the HDF5 file
    comps = load_hdf5_compositions(filename)
    original_number = len(comps)

    # convert comps to a list of dictionaries
    comps_list = [c._asdict() for c in comps]

    # add custom materials not already in the HDF5 file
    for material in custom_mats:
        comps_list.append(material._asdict())

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

except:
    print("""Error: the usage of this script requires the following syntax:\n
          python add-comps.py <file>.shift_compositions.h5\n
          This script should be run from the location containing the input.""")
