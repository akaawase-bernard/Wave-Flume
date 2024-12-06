

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Measured wavelength is 134.9 mm

#Length in meters
wavelengths_desired = np.array([0.4, 0.260, 0.1])
#wavelengths_desired = np.array([0.1349])
print("The desired wavelengths are", wavelengths_desired, "in meters")

k_desired = 2 * np.pi/wavelengths_desired
print("The k values are", k_desired, "in rad/m")


def calculate_omega_vs_wavenumber(wavelengths, h, g=9.81, sigma=0.074, rho=1000):
    """
    Calculate omega vs wavenumber for a range of wavelengths considering surface tension.
    
    Parameters:
    wavelengths (array): Array of wavelengths in meters
    h (float): Water depth in meters
    g (float): Gravitational acceleration (default is 9.81 m/s^2)
    sigma (float): Surface tension of water (default is 0.074 N/m)
    rho (float): Density of water (default is 1000 kg/m^3)
    
    Returns:
    k (array): Wavenumbers
    omega (array): Angular frequencies
    """
    # Calculate wavenumber k from the wavelengths
    k = 2 * np.pi / wavelengths
    
    # Calculate omega using the dispersion relationship with surface tension
    omega = np.sqrt((g * k + (sigma / rho) * k**3) * np.tanh(k * h))
    
    return k, omega

#Water depth in meters
h = 0.4

#Range of wavelengths for figures
wavelengths_range = np.linspace(0.01, 5, 500)
k_desired, omega_desired = calculate_omega_vs_wavenumber(wavelengths_desired, h)


k, omega = calculate_omega_vs_wavenumber(wavelengths_range, h)

#figure of omega vs k in linear scale
plt.figure(figsize= (10,6))
plt.plot(k, omega, linewidth = 5, color ='k')
plt.xlabel('k [rad/m]', fontsize=28)
plt.ylabel('ω [rad/s]', fontsize=28)

colors = ['red' ,'gold', 'cyan']
for item in range(len(k_desired)):
    
    plt.plot(k_desired[item], omega_desired[item], 'o', color =colors[item], markersize=12)

#plt.grid()
# plt.xscale('log')
# plt.yscale('log')
# plt.axvline(15.707, color='red' ,label='k is 15.71, omega is 12.42')
# plt.axvline(24.16, color='gold', label='k is 24.16, omega is 15.43')
# plt.axvline(62.83, color='cyan', label='k is 62.83, omega is 25.19')
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.tick_params(axis='both', which='major', labelsize=17)
plt.rcParams.update({'font.size': 23})
plt.xlim([0,400])
plt.ylim([0,100])

plt.legend(['Dispersion Relation (with Surface Tension)', 
            f'k is {wavelengths_desired[0]}', 
            f'k is {wavelengths_desired[1]}',
            f'k is {wavelengths_desired[2]}'], fontsize=15)
plt.tight_layout()
plt.savefig("figs/omega_k.png") 
plt.show()

# #figure of omega vs k in log scale
plt.figure(figsize= (10,6))
plt.plot(k, omega, label='Dispersion Relation (with Surface Tension)')
plt.xlabel('Wavenumber (k) [rad/m]')
plt.ylabel('Angular Frequency (ω) [rad/s]')
plt.title('Angular Frequency (ω) vs Wavenumber (k), Log Scale')

colors = ['red' ,'gold', 'cyan']
for item in range(len(k_desired)):
    
    plt.plot(k_desired[item], omega_desired[item], 'o', color =colors[item])

plt.grid()
plt.xscale('log')
plt.yscale('log')
plt.axvline(15.707, color='red' ,label='k is 15.71, omega is 12.42')
plt.axvline(24.16, color='gold', label='k is 24.16, omega is 15.43')
plt.axvline(62.83, color='cyan', label='k is 62.83, omega is 25.19')
plt.legend()
plt.show()


####################################################################
#period vs wavelength plotting

def calculate_T_from_omega(omega):
    'can use input from the omega_desired, converts values to period'
    T = (2 * np.pi)/omega
    print("Periods are", T, "in seconds")
    return T

T = calculate_T_from_omega(omega_desired)


T_disp = (2 * np.pi)/omega
#figure of period vs wavelength
plt.figure(figsize= (10,6))
plt.plot(wavelengths_range, T_disp, linewidth = 5, color ='k')
plt.xlabel('Wavelength [m]', fontsize=28)
plt.ylabel('Period [s]', fontsize=28)

colors = ['red' ,'gold', 'cyan']
# for item in range(len(k_desired)):
    
#     plt.plot(wavelengths_range[item], T[item], 'o', color =colors[item], markersize=12)

#plt.grid()
# plt.xscale('log')
# plt.yscale('log')
# plt.axvline(15.707, color='red' ,label='k is 15.71, omega is 12.42')
# plt.axvline(24.16, color='gold', label='k is 24.16, omega is 15.43')
# plt.axvline(62.83, color='cyan', label='k is 62.83, omega is 25.19')
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.tick_params(axis='both', which='major', labelsize=17)
plt.rcParams.update({'font.size': 23})
plt.xlim([0,1])
plt.ylim([0,1])

# plt.legend(['Dispersion Relation (with Surface Tension)', 
#             f'T is {T[0]}', 
#             f'T is {T[1]}',
#             f'T is {T[2]}'], fontsize=15)
plt.tight_layout()
plt.savefig("figs/T_wavelength.png") 
plt.show()


# c vs k plotting

def calculate_c_vs_k(wavelengths, h, g=9.81, sigma=0.074, rho=1000):
    """
    Calculate the phase speed c vs wavenumber k for a range of wavelengths, including surface tension.
    
    Parameters:
    wavelengths (array): Array of wavelengths in meters
    h (float): Water depth in meters
    g (float): Gravitational acceleration (default is 9.81 m/s^2)
    sigma (float): Surface tension of water (default is 0.074 N/m)
    rho (float): Density of water (default is 1000 kg/m^3)
    
    Returns:
    k (array): Wavenumbers
    c (array): Phase speeds
    """
    # Calculate wavenumber k from the wavelengths: k = 2 * pi / L
    k = 2 * np.pi / wavelengths
    
    # Calculate angular frequency omega using the dispersion relationship with surface tension
    omega = np.sqrt((g * k + (sigma / rho) * k**3) * np.tanh(k * h))
    
    # Calculate the phase speed c = omega / k
    c = omega / k
    
    return k, c

#wavelengths_range and h defined earlier
k, c = calculate_c_vs_k(wavelengths_range, h)
k_desired, c_desired = calculate_c_vs_k(wavelengths_desired, h)

plt.figure(figsize= (10,6))
plt.plot(k, c, label='Phase Speed (c) with Surface Tension')
plt.xlabel('Wavenumber (k) [rad/m]')
plt.ylabel('Phase Speed (c) [m/s]')
plt.title('Phase Speed (c) vs Wavenumber (k)')
plt.grid()

colors = ['red' ,'gold', 'cyan']
for item in range(len(k_desired)):
    
    plt.plot(k_desired[item], c_desired[item], 'o', color =colors[item])

plt.axvline(15.707, color='red' ,label='k is 15.71, c is 0.79')
plt.axvline(24.16, color='gold', label='k is 24.16, c is 0.63')
plt.axvline(62.83, color='cyan', label='k is 62.83, c is 0.40')
plt.legend()


# c vs lambda

plt.figure(figsize= (10,6))
plt.plot(wavelengths_range, c, label='Phase Speed (c) with Surface Tension',linewidth = 5, color ='k')
plt.xlabel('λ [m]')
plt.ylabel('c [m/s]')


for item in range(len(k_desired)):
    
    plt.plot(wavelengths_desired[item], c_desired[item], 'o', color =colors[item])

# plt.axvline(0.4, color='red' ,label='λ is 0.4, c is 0.79')
# plt.axvline(0.26, color='gold', label='λ is 0.26, c is 0.63')
# plt.axvline(0.1, color='cyan', label='λ is 0.1, c is 0.40')
plt.legend(['Dispersion Relation (with Surface Tension)', 
            f'c is {c_desired[0]}', 
            f'c is {c_desired[1]}',
            f'c is {c_desired[2]}'], fontsize=15)
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.tick_params(axis='both', which='major', labelsize=17)
plt.rcParams.update({'font.size': 23})
plt.xlim([0,1])
plt.ylim([0,1])
plt.tight_layout()
plt.savefig("figs/c_wavelength.png") 
plt.show()


# combined plot

fig, ax1 = plt.subplots(figsize=(10, 6))
# Primary x-axis (wavenumber)
ax1.plot(k, c, label='Phase Speed (c) with Surface Tension')
ax1.set_xlabel('k [rad/m]', fontsize = 20)
ax1.set_ylabel('c [m/s]', fontsize = 20)
#ax1.set_title('Phase Speed (c) vs Wavenumber (k)')
ax1.grid()

for item in range(len(k_desired)):
    
    plt.plot(k_desired[item], c_desired[item], 'o', color =colors[item])

plt.axvline(15.707, color='red' ,label='k is 15.71, c is 0.79, λ is 0.4')
plt.axvline(24.16, color='gold', label='k is 24.16, c is 0.63, λ is 0.26')
plt.axvline(62.83, color='cyan', label='k is 62.83, c is 0.40, λ is 0.1')
plt.show()
# Secondary x-axis (wavelengths)
def wavenumber_to_wavelength(k):
    return 2 * np.pi / k

secax = ax1.secondary_xaxis('top', functions=(wavenumber_to_wavelength, lambda L: 2 * np.pi / L))
secax.set_xlabel('Wavelength (λ) [m]', fontsize = 20)
#secax.set_xscale('log')  # Log scale to match the primary x-axis

plt.legend()
plt.show()




# Slope = amplitude * phase speed    s=ak       a=s/k     H=2a

def calculate_f_from_omega(omega):
    'can input from the omega_desired, converts values to frequency'
    f = omega/(2 * np.pi)
    print("frequencies are", f, "in 1/second")
    return f

f = calculate_f_from_omega(omega_desired)




def calculate_H_from_k(k):
    'Input k_desired'
    s2 = 0.2
    s25 = 0.25
    s3 = 0.3
    a2 = s2/k
    a25 = s25/k
    a3 = s3/k
    H2 = 2 * a2
    H25 = 2 * a25
    H3 = 2 * a3
    print("H at s=0.2 will be", H2, "in meters")
    print("H at s=0.25 will be", H25, "in meters")
    print("H at s=0.3 will be", H3, "in meters")
    return H2, H25, H3
    

H_values = calculate_H_from_k(k_desired)




calculate_T_from_omega(omega_desired)
T = calculate_T_from_omega(omega_desired)

