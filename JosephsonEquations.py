import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt, cm, colors
from scipy.constants import pi,hbar,e,h
flux_0 = h/2./e

def phase_evolution (voltage_function,t_list):
	return np.array([quad(voltage_function,0.,t)[0] for t in t_list])

def potential (Ic, phase_list):
	return (hbar*Ic/e)*np.cos(2.*pi*phase_list)


N = 1001
def voltage(t):
	return 3.*t
t_list = np.linspace(0,1,N)

phase_list =phase_evolution(voltage,t_list)
potential_list = potential (2., phase_list)

plt.plot(phase_list, potential_list)
plt.xlabel('Phase')
plt.ylabel('Potential')
plt.show()
plt.close()