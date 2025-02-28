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

# Define all the relevant variables
initv = 0
initi = 0
initdv = 1
vthresh = 0.25
c = 1
r = 1
tau = r * c
ts = 0.05
epochs = list(range(100))


# Implement relevant equations
# V(t + dt) = V(t) + dt/T(-(V-V(rest)) + R*I(t))
# V(t) = -1(V(t + dt) + dt/T(-(V-V(rest)) + R*I(t)))
# Tau(dV/dt) = -V(t) + R*I(t)


def m_dvdt(i, v):
    return (-v + r * i) /tau


def m_v(dvdt, v, dt):
    return v + dvdt * dt


def m_i(v, dvdt):
    return v / r + c * dvdt


voltage = [0]
time = [0]
current = [0]
i = initi
dvdt = initdv

for _ in epochs:
    i = 1 if 0.5 >= time[_] >= 0.25 else 0
    newvoltage = (m_v(dvdt, voltage[-1], ts))
    if voltage[-1] and voltage[_] == 0.5:
        newvoltage = 0
    dvdt = m_dvdt(i, voltage[-1])
    voltage.append(newvoltage)
    time.append(time[-1]+ts)
    current.append(i)
    if voltage[_] >= vthresh:
        # Spike event
        voltage[_] = 0.5

        # Implement a refractory period?
print(voltage)
print(time)
print(current)

p.plot(time, voltage, 'b')
p.plot(time, current, 'g')
p.show()

