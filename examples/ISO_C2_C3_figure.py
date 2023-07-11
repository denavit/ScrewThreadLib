from screw_thread_lib import C2_ISO, C3_ISO
import matplotlib.pyplot as plt
import numpy as np

# Setup
R_list = np.linspace(0.4, 2.2, 1000)
R_list[0] += 1e-6 
R_list[-1] -= 1e-6 
fig, ax = plt.subplots()

# Plotting
C2 = []
C3 = []

for R in R_list:
    C2.append(C2_ISO(R))
    C3.append(C3_ISO(R))

plt.vlines(x = 1, ymin = 0, ymax = 2, linestyle = 'dashdot', colors = 'k')
plt.plot(R_list, C2, label = '$C_2$')
plt.plot(R_list, C3, 'r--', label = '$C_3$')


# Plot Formatting
plt.xlim(0.4, 2.2)
plt.ylim(0.7, 1.3)
plt.ylabel('$C_2, C_3$')
plt.xlabel(r'$R_s = {R_{mn}} {A_{Sn}} / {R_m} {A_{Sb}}$')
plt.title('ISO/TR 16224:2012(E) Figure 1')
plt.text(1.05, 1.25, 'Bolt Thread Failure')
plt.text(0.49, 1.25, 'Nut Thread Failure')
plt.arrow(1.05, 1.24, 0.25, 0, width = 0.004)
plt.arrow(0.95, 1.24, -0.25, 0, width = 0.004)
plt.legend()
plt.show()
