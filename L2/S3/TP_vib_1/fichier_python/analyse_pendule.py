# -*- coding: utf-8 -*-
'''Programme réalisé par Arnaud Pieren'''
import sys
from scipy import *
from pylab import *
from scipy.optimize import curve_fit
import numpy as np

""" 1) Check data file name from command-line arguments """

narg = len(sys.argv)
if narg < 2:
    print("Missing data file name")
    quit()
elif narg > 2:
    print("Too many data file names: just one is expected")
    quit()

""" 2) Determine number of data points """

datafile = open(sys.argv[1], 'r')
ndata = 0
for line in datafile:
    ndata = ndata + 1
print("Number of data points =",ndata)
datafile.close

""" 3) Fill in data array """

data = np.zeros((ndata,2))

datafile = open(sys.argv[1], 'r')
ndata = 0
for line in datafile:
    words = line.split(',')
    data[ndata,0] = words[0]
    data[ndata,1] = words[1]
    ndata = ndata + 1
datafile.close

""" 4) Fit curve """

def sinusoide_amortie(t,amplitude,phase,period,damping,offset):
    return amplitude*cos(2*pi*t/period-phase)*exp(-t/damping)+offset

def get_index_from_time(t,tab):
    if t < min(tab) or t > max(tab):
        return len(tab)-1
    else:
        for i in range(len(tab)-2):
            if t > tab[i] and t < tab[i+1]:
                return i
        return len(tab)-1

tmax = max(data[:,0])
i = get_index_from_time(tmax,data[:,0])
"""print("Time t =",tmax,"Index i =",i)"""
times = data[0:i,0]
angles = data[0:i,1]
params,cov = curve_fit(sinusoide_amortie,times,angles)
t = linspace(0,tmax, 1000)
print("Fit over time interval [0;",tmax,"]")
plot(data[0:i,0],data[0:i,1], 'o', color="r")
(amplitude,phase,period,damping,offset) = params
print("Amplitude theta0 =",'{:.3f}'.format(amplitude),"rad =",
      '{:.1f}'.format(amplitude*180/pi),"deg")
print("Period T         =",'{:.3f}'.format(period),"s")
print("Damping time     =",'{:.0f}'.format(damping),"s")
print("Offset angle     =",'{:.3f}'.format(offset),"rad =",
      '{:.1f}'.format(offset*180/pi),"deg")
plot(t,sinusoide_amortie(t,amplitude,phase,period,damping,offset), '-', zorder=-2)
#show()

""" 5) Theory """

g = 9.81
R = 0.04   # R = 4 cm
mc = 0.25
radius = 0.025 # r = 2.5 cm
h = 0.017      # h = 1.7 cm
n = 4
m = n*mc
mt = 0.20
ma = 0.565
l = 0.58 # 0.66-(R+n*h/2)  # l = 58 cm
OC = (m*(R+l+0.5*n*h)+mt*(R+l/2))/(mt+m+ma)
IOx = m*(R+l+n*h/2)**2+0.25*m*(radius**2+(n*h)**2/3)
IOx = IOx + mt*l**2/12+mt*(R+l/2)**2+0.5*ma*R**2
T0 = 2*pi*sqrt(IOx/((m+mt+ma)*g*OC))
print("\nLength of the rod:   l =",'{:.1f}'.format(l*100),"cm")
print("Mass of the rod:    mt =",'{:.0f}'.format(mt*1000),"g")
print("Mass of axial disc: ma =",'{:.0f}'.format(ma*1000),"g")
print("Total mass: M =",'{:.0f}'.format((m+ma+mt)*1000),"g")
print("Center-of-mass distance from rotation axis: OC =",
      '{:.1f}'.format(OC*100),"cm")
print("Harmonic period T0 =",'{:.3f}'.format(T0),"s")
theta0 = amplitude
TBorda = T0*(1+theta0**2/16)
Texact = T0*(1+0.25*sin(theta0/2)**2)
print("Borda formula   T  =",'{:.3f}'.format(TBorda),
      "s  (with theta0 =",'{:.3f}'.format(theta0),"rad)")
print("Exact formula   T  =",'{:.3f}'.format(Texact),
      "s  (with theta0 =",'{:.3f}'.format(theta0),"rad)")

T0=period/(1+theta0**2/16)
print("\nExperimentally deduced T0 =",'{:.3f}'.format(T0),"s")
omega0=2*pi/T0
alpha = l**2/12+(R+l/2)**2
beta = m*(R+l+n*h/2)**2+ma*R**2/2
gamma = R+l/2
delta = m*(R+l+n*h/2)
mt = (delta-omega0**2/g*beta)/(omega0**2/g*alpha-gamma)
print("Experimentally deduced mass of the rod:   mt =",
      '{:.0f}'.format(mt*1000),"g")

rho = mc/(pi*radius**2*h-pi*(0.5*0.007)**2*h)
#rho = mc/(pi*radius**2*h) # hole neglected
print("Estimated density of the rod: rho =",
      '{:.0f}'.format(rho),"kg/m^3")
diameter = 0.0075 # Diameter of the rod (effective solid rod)
mt = rho*pi*diameter**2/4*l
print("Estimated mass of the rod (from density): mt =",
      '{:.0f}'.format(mt*1000),"g")


quit()
