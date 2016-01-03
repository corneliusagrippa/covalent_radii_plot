import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(16,6))
x, y = np.loadtxt('test.csv', unpack= True, skiprows = 1, delimiter =',')
plt.plot(x, y, color = 'violet', marker = 'o')

#peaks = {'Li': '3','Na': '11','K': '19','Rb': '37','Cs': '55','Fr': '87'}
#peaks_x = (2, 10, 18, 36, 54, 86)

plt.annotate('Li',
            xy=(x[2], y[2]),
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.title('Covalent radii trend')
plt.ylabel('Covalent Radii')
plt.xlabel('Atomic number')

plt.show()