import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_-2_cl_lensed.dat', '/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_-2_halofit_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['dmeff_-2_cl_lensed', 'dmeff_-2_halofit_cl_lensed']

fig, ax = plt.subplots()
y_axis = ['phiphi']
tex_names = ['phiphi']
x_axis = 'l'
ax.set_xlabel('$\ell$', fontsize=16)
plt.show()