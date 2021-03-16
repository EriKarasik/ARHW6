import numpy as np
from numpy import hstack as h, vstack as v
import matplotlib.pyplot as plt
from robotmove import *

def viz(q):
    ax = plt.axes(projection='3d')
    pos = [[0, 0, 0]]
    T = Rz(q[0])*Tz(l2)
    pos.append(transpose(T[0:3, 3])[0])
    T = T*Rx(q[1])*Ty(l1)
    pos.append(transpose(T[0:3, 3])[0])
    T = T*Ty(q[2])
    pos.append(transpose(T[0:3, 3])[0])
    x = [i[0] for i in pos]
    y = [i[1] for i in pos]
    z = [i[2] for i in pos]
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    ax.set_zlim(0, 150)
    ax.plot(x, y, z)
    ax.scatter(x, y, z)
    plt.show()

def poe(S,q):
    Sw = np.asarray(S[0:3])
    Sv = np.asarray(S[3:6])
    return v([h([np.eye(3), Sv*q]), [0, 0, 0, 1]]) if Sw.all() == 0 else v([h([np.eye(3)+np.sin(q)*skew(Sw)+(1-np.cos(q))*skew(Sw)**2,np.dot(np.eye(3)*q+(1-np.cos(q))*skew(Sw)/q+(q-np.sin(q))*(skew(Sw))**2,Sv)]),[0, 0, 0, 1]])

l1,l2 = 100,10
M = [[1.,0.,0.,0],[0.,1.,0.,l1],[0.,0.,1.,l2],[0.,0.,0.,1.]]
S = [[[0],[0],[1],[0],[0],[0]],[[1],[0],[0],[0],[1],[0]],[[0],[0],[0],[0],[1],[0]]]


def FK(M, S, q):
    for i in range(len(q)-1,-1,-1): M = np.dot(M,poe(S[i],q[i]))
    return M[0:3, 3]

def Jacobian(S, q):
    J,T = zeros(6,3),np.eye(4)
    J[0] = S[0]
    for i in range(1,len(q)):
        T = np.dot(T, poe(S[i-1],q[i-1]))
        J[i] = np.dot(Adjoint(T), S[i])
    return J

def Adjoint(T):
    R = np.transpose(T[0:3,0:3])
    return v([h([R, np.dot(skew(T[0:3,3]),R)]),h([zeros(3, 3), R])])

viz([0,0,0])
