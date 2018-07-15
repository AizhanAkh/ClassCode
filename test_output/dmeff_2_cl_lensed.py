import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_2_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['dmeff_2_cl_lensed']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['phiphi']
tex_names = ['phiphi']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 5]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()