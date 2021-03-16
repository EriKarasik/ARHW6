from numpy import matrix, cos, sin, array
from sympy import *

def skew(x): return array([[0, -x[2], x[1]],[x[2], 0, -x[0]],[-x[1], x[0], 0]],dtype='float')
def cross(a, b): return transpose(Matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]))
def Tz(a): return matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, a], [0, 0, 0, 1]])
def Ty(a): return matrix([[1, 0, 0, 0], [0, 1, 0, a], [0, 0, 1, 0], [0, 0, 0, 1]])
def Tx(a): return matrix([[1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def dTz(): return matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
def dTy(): return matrix([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
def dTx(): return matrix([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
def Rx(a): return matrix([[1, 0, 0, 0], [0, cos(a), -sin(a), 0], [0, sin(a), cos(a), 0], [0, 0, 0, 1]])
def Ry(a): return matrix([[cos(a), 0, sin(a), 0], [0, 1, 0, 0], [-sin(a), 0, cos(a), 0], [0, 0, 0, 1]])
def Rz(a): return matrix([[cos(a), -sin(a), 0, 0], [sin(a), cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def dRx(a): return matrix([[0,0,0,0],[0,-sin(a),-cos(a),0],[0,cos(a),-sin(a),0],[0,0,0,0]])
def dRy(a): return matrix([[-sin(a),0,cos(a),0],[0,0,0,0],[-cos(a),0,-sin(a),0],[0,0,0,0]])
def dRz(a): return matrix([[-sin(a),-cos(a),0,0],[cos(a),-sin(a),0,0],[0,0,0,0],[0,0,0,0]])