from matplotlib import pyplot as plt
import numpy as np

data = np.array([[354.769222, 15.377504, 13.886702],[ 361.954770, 15.361353, 10.121975],[358.021756,15.356095,8.158909 ],[351.722487,15.417412,7.134628  ]])

Int_serial = data[:,0]
Int_np = data[:,1]
Int_numexp = data[:,2]


ratio_serial = data[:,0]/data[0,0]
ratio_np = data[:,1]/data[0,1]
ratio_numexp = data[:,2]/data[0,2]

xVals = [1,2,4,8]
plt.figure(1, figsize=(10,6))
plt.plot(xVals, Int_serial, label = 'Serial Integration', marker = 'o')
plt.plot(xVals, Int_np, label = 'Integration with numpy', marker = 'o')
plt.plot(xVals, Int_numexp, label = 'Integration with numexpr', marker = 'o')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.xlabel('Number of Threads')
plt.ylabel('Integration time (s)')


plt.figure(2, figsize=(10,6))
plt.plot(xVals, ratio_serial, label = 'Serial Integration', marker = 'o')
plt.plot(xVals, ratio_np, label = 'Integration with numpy', marker = 'o')
plt.plot(xVals, ratio_numexp, label = 'Integration with numexpr', marker = 'o')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.xlabel('Number of Threads')
plt.ylabel('Ratio Integration time (s)')