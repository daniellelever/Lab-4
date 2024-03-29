#PART 4: Group 10: done by Danielle Lever

import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt


#inital conditons =  y(t=0) = [maxswing, 0 ,0]
pen_length =  9.81 #m
amp_period = 2 * (np.pi)
maxswing = (np.pi)/6 # in rad

#function finding the pendulum amplitude
def pendulum_amp(time, thetastate, maxswing, Q_damp):
    thetaprime = thetastate[1]
    thetaprime2 = -1 / Q_damp * thetaprime - np.sin(thetastate[0])
    return([thetaprime, thetaprime2])


def event(time, thetastate, maxswing, Q_damp):
    x = pendulum_amp(time, thetastate, maxswing, Q_damp)
    return thetastate[1]
    
pendulum_amp.terminal = True

Q_damp = [1,5,10,25,50]
t_soln = np.linspace(0,10*np.pi,10000)
yinit = np.array([0,maxswing])

#solving for each value in Q:1,5,10,25,20
  
for Q in Q_damp:
    result = scint.solve_ivp(pendulum_amp, [0,10*np.pi], yinit, \
                               args=(maxswing, 2), events=[event])


#accessing event values to compare time and amplitude
peakval = result.y_events
timeest = result.t_events
inital = peakval[0]/np.exp(1)

peakval = result.y_events
time_est = result.t_events
inital = peakval[0][0]/np.exp(1)

t_est1 = time_est[0][0]
t_est2 = time_est[0][1]
t_est3 = time_est[0][2]
Q1 = Q_damp[0]
Q2 = Q_damp[3]
Q3 = Q_damp[4]

#plotting relation to Q and time of amplitude drop values 
fig, ax = plt.subplots()
for Q in Q_damp:
    ax.plot = ax.scatter(t_est1, Q1)
    ax.plot = ax.scatter(t_est2, Q2)
    ax.plot = ax.scatter(t_est3, Q3)
    
plt.title("Relation between Q and time of amplitude drop")
plt.xlabel('time estimate')
plt.ylabel('amplitude fall of 1/e of inital value')
plt.show()