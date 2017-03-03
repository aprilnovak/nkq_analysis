import numpy as np	# for: absolute value

# script to compute the number densities in atoms/barn-cm for input to Shift
# based on material compositions in weight percent

density = 7.83 # grams/cm^3
wt_frac = [0.9790, 0.0055, 0.0130, 0.0025]

# check that the weight fractions sum to 1
wt_frac_sum = 0
for i in range(len(wt_frac)):
	wt_frac_sum += wt_frac[i]

if np.abs(wt_frac_sum - 1) >= 1e-6:
	print("Entered weight fractions do not sum to one!")
