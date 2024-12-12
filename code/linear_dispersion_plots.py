import numpy as np
import matplotlib.pyplot as plt



#inputs
h = 0.34
g=9.81
sigma=0.074
rho=1000


wavelengths = np.linspace(0.01, 1.2, 500)
k = 2 * np.pi / wavelengths

# Calculate omega using the dispersion relationship with surface tension
omega = np.sqrt((g * k + (sigma / rho) * k**3) * np.tanh(k * h))
c = omega / k



## oberved values
obs_wavelength1 = 333.3/1000
obs_T1 = 0.46

obs_wavelength2 = 232.6/1000
obs_T2 = 0.33

obs_wavelength3 = 153.4/1000
obs_T3 = 0.3



c_obs1 = obs_wavelength1/ obs_T1
k_obs1 = 2 * np.pi / obs_wavelength1
f1 = 1/obs_T1
obs_omega1 = 2*np.pi*f1

c_obs2 = obs_wavelength2/ obs_T2
k_obs2 = 2 * np.pi / obs_wavelength2
f2 = 1/obs_T2
obs_omega2 = 2*np.pi*f2

c_obs3 = obs_wavelength3/ obs_T3
k_obs3 = 2 * np.pi / obs_wavelength3
f3 = 1/obs_T3
obs_omega3 = 2*np.pi*f3



plt.figure(figsize= (10,6))
plt.plot(k, omega, label='Dispersion', linewidth=5, color ='k')
plt.plot(k_obs1, obs_omega1, 'o', color ='r', label ='observation 1')
plt.plot(k_obs2, obs_omega2, 'o', color ='g', label ='observation 2')
plt.plot(k_obs3, obs_omega3, 'o', color ='pink', label ='observation 3')
plt.xlabel('Wavenumber [rad/m]', fontsize = 20)
plt.ylabel('ω [rad/s]', fontsize = 20)
plt.tick_params(axis='both', which='major', labelsize=20)  
plt.legend()
plt.tight_layout()


plt.figure(figsize= (10,6))
plt.plot(k, c, label='Dispersion', linewidth=5, color ='c')
#plt.plot(k_obs, c_obs, 'o', color ='r', label ='observation')
plt.plot(k_obs1, c_obs1, 'o', color ='r', label ='observation 1')
plt.plot(k_obs2, c_obs2, 'o', color ='g', label ='observation 2')
plt.plot(k_obs3, c_obs3, 'o', color ='pink', label ='observation 3')
plt.tick_params(axis='both', which='major', labelsize=20)  
plt.ylabel('Phase Speed  [m/s]', fontsize = 20)
plt.legend()
plt.tight_layout()

#optional
plt.figure(figsize= (10,6))
plt.plot(wavelengths, c, label='dispersion', linewidth=5, color ='b')
plt.plot(obs_wavelength1, c_obs1, 'o', color ='r', label ='observation 1')
plt.plot(obs_wavelength2, c_obs2, 'o', color ='g', label ='observation 2')
plt.plot(obs_wavelength3, c_obs3, 'o', color ='pink', label ='observation 3')
plt.tick_params(axis='both', which='major', labelsize=20)  
plt.xlabel('Wavelength  [m]', fontsize = 20)
plt.ylabel('Phase Speed  [m/s]', fontsize = 20)
plt.legend()
plt.tight_layout()