import numpy as np	# for: absolute value

# script to compute the number densities in atoms/barn-cm for input to Shift
# based on material compositions in weight percent

Na = 6.022140857E23 # Avogadro's number
barn = 1E-24 # conversion from barn to cm

# dictionary of atomic masses (g/mol)
m = {'Fe' : 55.845, 'Ni' : 58.6934, 'Cr' : 51.9961, 'Mn' : 54.938045, \
'C' : 12.0107, 'Si' : 28.0855, 'Ca' : 40.078, 'K' : 39.0983, 'Al' : 26.981539,\
'Mg' : 24.305, 'Na' : 22.989769, 'O' : 15.9994, 'H' : 1.00794} 

def AtomDensities(density, wt_frac, elem_mass):
	""" Function to return the atom densities in atoms/barn-cm, 
	where <density> is the density in g/cm^3, <wt_frac> are the
	weight fractions of each element, and <elem_mass> is the
	atomic mass of an element (taken from Wikipedia), in g/mol."""

	# check that the weight fractions sum to 1
	wt_frac_sum = 0
	for i in range(len(wt_frac)):
		wt_frac_sum += wt_frac[i]

	if np.abs(wt_frac_sum - 1) >= 1e-6:
		print("Entered weight fractions do not sum to one!")


	atom_dens = []
	# return vector of atom densities
	for i in range(len(wt_frac)):
		atom_dens.append(density * wt_frac[i] * Na * barn / elem_mass[i])

	return atom_dens

## A533B  #############################################################

density = 7.83 
wt_frac = [0.9790, 0.0055, 0.0130, 0.0025]
elem_mass = [m['Fe'], m['Ni'], m['Mn'], m['C']]

A533B_atom_dens = AtomDensities(density, wt_frac, elem_mass)
print("A533B atom densities are:")
print(A533B_atom_dens)

## SS-304 #############################################################

density = 8.03
wt_frac = [0.69, 0.100, 0.190, 0.02]
elem_mass = [m['Fe'], m['Ni'], m['Cr'], m['Mn']] 

SS304_atom_dens = AtomDensities(density, wt_frac, elem_mass)
print("SS304 atom densities are:")
print(SS304_atom_dens)

## concrete ##########################################################

density = 2.275
wt_frac = [0.0382, 0.0010, 0.3409, 0.0440, 0.0131, 0.0343, 0.0022, 0.0162, 0.5050, 0.0051]
elem_mass = [m['Fe'], m['C'], m['Si'], m['Ca'], m['K'], m['Al'], m['Mg'], m['Na'], m['O'], m['H']]

concrete_atom_dens = AtomDensities(density, wt_frac, elem_mass)
print("Concrete atom densities are:")
print(concrete_atom_dens)


