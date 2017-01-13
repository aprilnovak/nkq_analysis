from omnibus.formats.comp import Compositions
from robus import load_hdf5_compositions, Nuclide_Metadata, Composition
Nuclide_Metadata.load_SCL()

# load in the HDF5 file
comps = load_hdf5_compositions("hybrid.shift_compositions.h5")

# convert comps to a list of dictionaries
comps_list = [c._asdict() for c in comps]
print(len(comps_list))

# add custom materials not in the VERA input
custom_mat = Composition(300.0, [1001, 1002, 8016, 8017], [6.67e-2, 7.67e-6, 3.32e-2, 1.26e-5])
comps_list.append(custom_mat._asdict())
print(len(comps_list))
#print(comps_list[4])

h5_c = Compositions.from_list(comps_list)# convert from list of dicts to h5 compatible data type
# dump this to hdf5

import h5py as h5
with h5.File("my_output.h5", 'w') as f:
    h5_c.dump(f)
