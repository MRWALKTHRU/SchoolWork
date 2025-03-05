
"""
Name: Jules Gravestock
Assignment: Model of the integrate-and-fire neuron

Assignment Instructions:
Tau(dV/dt) = -V(t) + R*I(t)
V = IR
I = I(1) + I(2)
I = V/R + C(dV/dt)

Program Instructions:

"""
import numpy as np
import matplotlib.pyplot as p
# Values
initv = -70e-33
initi = 0
maxi = 8.495e-3
initdv = 0
vthresh = -55e-3
maxv= 40e-3
# properties
c = 0.5
r = 1
tau = r * c
ts = 0.05
epochs = list(range(100))


# Implement relevant equations

def m_dvdt(i, v):
    return (-v + r * i)//tau


def m_v(dvdt, v, dt):
    return v + dvdt * dt

voltage = [initv]
time = [0]
current = [initi]
count = 100



for _ in epochs:
    i = maxi if 3 >= time[_] >= 0.25 else 0 # Tells the current to be on for a short period
    # Factor in refractory period
    if count <= 5:
        dvdt = m_dvdt(i/1000, voltage[-1])
    elif count <= 15:
        dvdt = m_dvdt(i/5, voltage[-1])
    else:
        dvdt = m_dvdt(i, voltage[-1])
    print(dvdt)

    newvoltage = (m_v(dvdt, voltage[-1], ts))

    # Code the voltage spike when threshold is exceeded
    if voltage[_] >= vthresh and voltage[-1] != maxv:
        voltage.append(maxv)
        count = 0
    elif voltage[-1] == maxv:
        voltage.append(initv)
        newvoltage = initv
    else:
        voltage.append(newvoltage)
    count += 1
    time.append(time[-1]+ts)
    current.append(i)


p.plot(time, voltage, 'black')
p.plot(time, current, 'red')
p.xlabel("Time (ms)")
p.ylabel("Voltage (mV)")
p.title("The Leaky Integrate-And-Fire Model of Neuron")
p.legend(['Voltage', 'Current'], loc='upper right')

p.show()
