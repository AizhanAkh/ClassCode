import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_-2_halofit_pk.dat', '/Users/aizhan.akh/Documents/Projects/PT-check/class/test_output/dmeff_-2_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['dmeff_-2_halofit_pk', 'dmeff_-2_pk']

fig, ax = plt.subplots()
y_axis = ['P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()