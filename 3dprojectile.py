from vpython import *
tgraph=graph(xtitle="Time [s]",ytitle="thickness [m]")
f1=gcurve(color=color.blue)
k=1
theta=10  #deg C
rho=0.015
L=5  #m
x=1
t=0
dt=0.001

while t<=20:
    m=(k*theta)/(x*rho*L)
    x+=m*dt
    f1.plot(t,x)
    t+=dt
