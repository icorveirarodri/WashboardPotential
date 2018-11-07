import stlab
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt, cm, colors
from scipy import pi,hbar,e

def phase_evolution (U, time,N):
	t_list = np.linspace(0,time,N)
	phase_dif_list = []

	U_list =  np.linspace(U, U, N) 

	for i in range (0, N):
		func = lambda x: (2*e*U*x/h_bar) 
		phase_final = (integrate.quad(func,0,t_list[i])[0])
		phase_dif_list.append(phase_final)

	return(phase_dif_list,t_list)

def potential (Ic, phase_list):
	potential_list = (h_bar*Ic/e)*np.cos(phase_list)
	return (potential_list)



phase_list, t_list = phase_evolution(2,10, 40)
potential_list = potential (2, phase_list)

plt.plot(phase_list, potential_list)
plt.xlabel('Phase')
plt.ylabel('Potential')
plt.show()
plt.close()