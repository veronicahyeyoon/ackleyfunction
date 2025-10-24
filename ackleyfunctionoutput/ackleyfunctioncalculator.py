import numpy as np

def ackleyinput (x,y):
    a= -0.2*(((x**2+y**2)/2)**0.5)
    b= (np.cos(2*np.pi*x)+np.cos(2*np.pi*y))/2
    z= -20*np.exp(a)-np.exp(b)+20+np.e

    return z