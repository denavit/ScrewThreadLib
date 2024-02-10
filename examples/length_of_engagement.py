import numpy as np
import matplotlib.pyplot as plt
from screw_thread_lib import Assembly

# Input
thread_type = '1/2-13' 
UTSs = 120000
UTSn_list = np.linspace(58000,140000,1000)
s = 0.75

# Calculate Length of Engagement
LEr_FEDSTD_13 = np.empty_like(UTSn_list)
LEr_FEDSTD_14 = np.empty_like(UTSn_list)
LEr_FEDSTD_15 = np.empty_like(UTSn_list)
LEr_FEDSTD_16 = np.empty_like(UTSn_list)
LEr_FEDSTD = np.empty_like(UTSn_list)
LEr_ISO = np.empty_like(UTSn_list)
LEr_ISO_without_Dm = np.empty_like(UTSn_list)

for i, UTSn in enumerate(UTSn_list):
    a = Assembly.from_ASME_B11_UN_2A2B(thread_type,UTSs,UTSn)
    LEr_FEDSTD_13[i] = a.LEr_FEDSTD_13()
    LEr_FEDSTD_14[i] = a.LEr_FEDSTD_14()
    LEr_FEDSTD_15[i] = a.LEr_FEDSTD_15()
    LEr_FEDSTD_16[i] = a.LEr_FEDSTD_16()
    LEr_FEDSTD[i] = a.LEr_FEDSTD()
    LEr_ISO[i] = a.LEr_ISO(s)
    
    a.use_Dm_ISO = False
    LEr_ISO_without_Dm[i] = a.LEr_ISO(s)

# Make Plot
fig, ax = plt.subplots(figsize=(6.5,3.5))
ax.set_position((0.12,0.15,0.85,0.80))

plt.plot(UTSn_list, LEr_FEDSTD_13, label = 'FED STD Formula (13)')
plt.plot(UTSn_list, LEr_FEDSTD_14, label = 'FED STD Formula (14)')
plt.plot(UTSn_list, LEr_FEDSTD_15, label = 'FED STD Formula (15)')
plt.plot(UTSn_list, LEr_FEDSTD_16, label = 'FED STD Formula (16)')
plt.plot(UTSn_list, LEr_FEDSTD, 'k', linewidth = 2, label = 'FED STD Controlling')
plt.plot(UTSn_list, LEr_ISO, label = 'ISO')
plt.plot(UTSn_list, LEr_ISO_without_Dm, label = 'ISO (without $D_m$)')

plt.xlabel('UTSn (psi)')
plt.ylabel('Length of Engagement (in.)')
plt.legend(ncol=2)
plt.show()
