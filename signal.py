import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

"""
dt = 0.05
N = 100
t = np.arange(0, N) * dt + 0
y = np.sin(2 * np.pi * t)

plt.plot(t, y)
plt.xlabel('time (s)')
plt.title('y = sin(2 * pi * t)')
plt.show()

time = np.linspace(0, 10, 12000)
y = [not int(x) % 2 for x in time]

plt.plot(time, y)
plt.xlabel("time (s)")
plt.title("y = 1 if n is even, y = 0 if n is odd") 
plt.show()
"""

dt = 0.05
N = 100
t = np.arange(0, N) * dt + 0
y = 2*t+5

y = y - np.mean(y)
Y = fft.fft(y)
f = fft.fftfreq(N, dt)

plt.figure(figsize=(12,5))

plt.subplot(121)
plt.plot(f[0:int(N/2)], np.abs(Y[0:int(N/2)]))
plt.xlabel('frequency (y-1)')
plt.title('sunspots: amplitude spectrum')
plt.xlim((0, 1 / (2 * dt)))
plt.grid()

plt.subplot(122)
plt.plot(f[0:int(N/2)], np.angle(Y[0:int(N/2)]))
plt.xlabel('frequency (y-1)')
plt.title('sunspots: phase spectrum')
plt.xlim((0, 1 / (2 * dt)))
plt.grid()
plt.show()