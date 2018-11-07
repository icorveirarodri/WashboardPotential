import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt, cm, colors
from scipy.constants import pi,hbar,e,h
flux_0 = h/2./e

def potential(t_list,Ic,voltage_function=None,current_function = None):

	if current_function == None:
		# compute voltage evolution
		phase_list = np.array([quad(voltage_function,0.,t)[0] for t in t_list])
		current_list = Ic*np.sin(2.*pi*phase_list)
		voltage_list = np.vectorize(voltage_function)(t_list)

	if voltage_function == None:
		# compute current evolution
		current_list = np.vectorize(current_function)(t_list)
		phase_list = np.arcsin(current_list/Ic)
		voltage_list = np.concatenate([(phase_list[1:]-phase_list[:-1])/(t_list[1]-t_list[0]),[0]])

	potential_list = np.array([np.trapz(voltage_list[:i]*current_list[:i],t_list[:i]) for i in range(len(t_list))])
	return phase_list,potential_list,current_list,voltage_list


N = 1001
def voltage(t):
	return 1.
def current(t):
	return 1.
t_list = np.linspace(0,100.,N)
Ic = 1.

# phase,U,I,V = potential(t_list,Ic,voltage_function=voltage,current_function = None)
phase,U,I,V = potential(t_list,Ic,voltage_function=None,current_function = current)

plt.plot(I)
plt.plot(V)

# plt.plot(phase,U)
plt.xlabel('Phase')
plt.ylabel('Potential')
plt.show()
plt.close()