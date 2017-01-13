import sys
import h5py as h5
from omnibus.formats.comp import Compositions
from robus import load_hdf5_compositions, Nuclide_Metadata, Composition

Nuclide_Metadata.load_SCL()

custom_mat = Composition(300.0, [1001, 1002, 8016, 8017], [6.67e-2, 7.67e-6, 3.32e-2, 1.26e-5])

try:
    # expected extension on the file read in by this script
    extension = ".shift_compositions.h5"
    filename = sys.argv[1]
    base_filename = filename[:-len(extension)]

    # load in the HDF5 file
    comps = load_hdf5_compositions(filename)

    # convert comps to a list of dictionaries
    comps_list = [c._asdict() for c in comps]

    # add custom materials not already in the HDF5 file
    comps_list.append(custom_mat._asdict())

    # convert comps_list from a list of dictionaries to a HDF5 compatible type
    h5_c = Compositions.from_list(comps_list)

    # dump to HDF5
    with h5.File("my_output.h5", 'w') as f:
        h5_c.dump(f)

except:
    print("""Error: the usage of this script requires the following syntax:\n
          python add-comps.py <file>.shift_compositions.h5\n
          This script should be run from the location containing the input.""")
