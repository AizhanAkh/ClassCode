import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/lcdm_ext_pk.dat', '/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/lcdm_ext_no_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['lcdm_ext_pk', 'lcdm_ext_no_pk']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 1, data[1]
y_axis = ['P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()