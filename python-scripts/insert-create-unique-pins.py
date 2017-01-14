import sys
import os

try:
    xml_file = sys.argv[1]
    filename = os.getcwd() + '/' + xml_file
    filename_out = os.getcwd() + '/' + xml_file[:-4] + '-unique-pins' + xml_file[-4:]
    print("Inserting create_unique_pins parameter in " + filename_out + "...")

    # We don't want to add this line if it already exists
    with open(filename, 'r') as f:
        for line in f:
            if line.strip()[-63:] == '<Parameter name="create_unique_pins" type="bool" value="true"/>':
                raise IOError

    with open(filename, 'r+') as fi:
        with open(filename_out, 'w') as fo:
            for line in fi:
                if line.strip()[-28:] == '<ParameterList name="SHIFT">':
                     fo.write(line)
                     fo.write('    <Parameter name="create_unique_pins" type="bool" value="true"/>\n')
                else:
                    fo.write(line)

    # delete the original file
    os.remove(xml_file)

    # replace the new file with the original filename
    os.rename(filename_out, xml_file)

except IOError:
    print("""Warning: This file has already been edited!""")

except:
    print("""Error: this script has the following call method:\n
            python insert-create-unique-pins.py <filename>.xml\n\n
            This script must be called from the directory containing the file.""")

