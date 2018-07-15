import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_0_ext_cl_lensed.dat', '/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_0_ext_no_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['dmeff_0_ext_cl_lensed', 'dmeff_0_ext_no_cl_lensed']

fig, ax = plt.subplots()
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ax.set_xlabel('$\ell$', fontsize=16)
plt.show()