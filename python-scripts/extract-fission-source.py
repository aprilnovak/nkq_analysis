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

    def extract_statepoint(self):
        """ Method to extract the fission source from an HDF5 file.

	    This function extracts all unique statepoints in the *.shift.h5 
	    input file and writes one output file for each state that only
    	    consists of the fission_source group. """

	# expected suffix for input to this file
	suffix_in = ".shift.h5"
	
        # open the HDF5 file for reading
        with h5py.File(self.filename, "r") as fi:
	    # only extract the fission source data sets. This assumes that the number of groups in the
	    # fission source file is 3 + the number of states and that the first state is the second entry
	    # (CORE is the first entry)
	    input_groups = fi.values()

	    for s in range(len(input_groups) - 3):
		    # output filename
		    filename_out = self.filename[:-len(suffix_in)] + ".src-extracted_state_" + str(s + 1) + ".shift.h5"
		    
		    # open an HDF5 file for writing
		    with h5py.File(filename_out, "w") as fo:
			try:
				# loop through all of the entries to determine which group corresponds to source
				fission_source = input_groups[s + 1]["fission_source"]
				
				for i in fission_source.keys():
					fo.create_dataset(str(i), data=fission_source[str(i)])
			except:
			    print("""Error: Syntax for this script is:\n
			    python extract-fission-source.py <filename>.shift.h5.\n\n
			    This script should be run from the directory where the original HDF5 file is located. This script has failed for some reason, check that the file exists and that it is in the correct format.""")
    
print("Converting fission source for {0}".format(sys.argv[1]))
instance = ExtractFissionSource(os.getcwd() + '/' + str(sys.argv[1]))
instance.extract_statepoint()
