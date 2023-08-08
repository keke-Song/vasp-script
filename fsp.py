from pynep.calculate import NEP
from pynep.select import FarthestPointSample
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
a = read('all.xyz', ':')
calc = NEP("nep.txt")
print(calc)
des = np.array([np.mean(calc.get_property('descriptor', i), axis=0) for i in a])
sampler = FarthestPointSample(min_distance=0.5)
selected_i = sampler.select(des, [])
write('selected.xyz', [a[i] for  i in selected_i])
reducer = PCA(n_components=2)
reducer.fit(des)
proj = reducer.transform(des)
plt.scatter(proj[:,0], proj[:,1], label='all data')
selected_proj = reducer.transform(np.array([des[i] for i in selected_i]))
plt.scatter(selected_proj[:,0], selected_proj[:,1], label='selected data')
plt.legend()
plt.axis('off')
plt.savefig('select.png')
