import h5py
import sys
import os

class ExtractFissionSource:
    """ Class to extract the fission source from an HDF5 file."""

    # constructor
    def __init__(self, filename):
        """ The filename is the full path to the file containing the original
            fission source HDF5 file."""

        self.filename = filename

    def extract_statepoint(self, statepoint):
        """ Method to extract the fission source from an HDF5 file.

            This function takes a statepoint (referring to one of the possibly
            multiple [STATE] blocks in a VERA input). The statepoint is an
            integer that refers to the position in time of the statepoint.
            For instance - the first statepoint is 0, the second 1, etc."""

        # suffix of the filename that is appended by the vera_to_shift executable
        suffix_in = ".shift.h5"

        # output filename
        filename_out = self.filename[:-len(suffix_in)] + ".src-extracted" + self.filename[-len(suffix_in):]

        # open the HDF5 file for reading
        with h5py.File(self.filename, "r") as fi:

            # open an HDF5 file for writing
            with h5py.File(filename_out, "w") as fo:
                # extract the entire statepoint group
                #input_keys = fi.keys()
                #fi.copy('/{0}'.format(input_keys[statepoint]), fo)

                # only extract the fission source data sets
                input_groups = fi.values()
                fission_source = input_groups[statepoint]["fission_source"]

                for i in fission_source.keys():
                    fo.create_dataset(str(i), data=fission_source[str(i)])

try:
    print("Converting fission source for {0}".format(sys.argv[1]))
    #print(os.getcwd() + '/' + str(sys.argv[1]))
    instance = ExtractFissionSource(os.getcwd() + '/' + str(sys.argv[1]))
    instance.extract_statepoint(0)
except:
    print("""Error: Syntax for this script is:\n
    python extract-fission-source.py <filename>.shift.h5.\n\n
    This script should be run from the directory where the original HDF5 file is located.""")
