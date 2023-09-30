from screw_thread_lib import Assembly
import matplotlib.pyplot as plt
import numpy as np

# Setup
sD_list = np.linspace(1.4,2.4, num=500)
bolt = Assembly.from_ASME_B11_UN_2A2B('1/2-13')
dbsc = bolt.dbsc

# Calculate
C1 = []
for sD in sD_list:
    C1.append(bolt.C1_ISO(sD*dbsc))
    
# Plotting
fig, ax = plt.subplots()
plt.plot(sD_list, C1)
plt.xlabel('Ratio of Width Across Flats of the Nut to Nominal Thread Diameter of the Nut, $s/D$')
plt.ylabel('Nut Dilation Factor, $C_1$')
plt.show()
