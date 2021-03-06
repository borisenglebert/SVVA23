from math import *
import matplotlib.pyplot as plt
import numpy as np

Iyy = 7.21*(10**(-5))
Izz = 1.409*(10**(-5))

def reactionforces(Izz, Iyy):

    x1 = 0.174
    x2 = 1.051
    x3 = 2.512
    d1 = 0.01034
    d3 = 0.02066
    xa = 0.3
    theta = 25.0*(np.pi)/180.
    E = 73.1*(10**9)
    q = 1.0*(10**3)
    L = 2.691
    P = 20.6*(10**3)
    ch = 0.515
    h = 0.248

   

    ## H2x == 0

    ## Rotated forces and deflections

    qy = q*np.cos(theta)
    qz = q*np.sin(theta)
    Py = P*np.sin(theta)
    Pz = P*np.cos(theta)
    dy1 = d1*np.cos(theta)
    dz1 = d1*np.sin(theta)
    dy2 = 0.0
    dz2 = 0.0
    dy3 = d3*np.cos(theta)
    dz3 = d3*np.sin(theta)

    ## Torque about the hinge line
    ## Actuator force

    A = (qy*L*((0.25*ch) - (h/2.0)) + Pz*(h/2.0) - Py*(h/2.0))/((np.sin(theta)*(h/2.0)) - (np.cos(theta)*(h/2.0)))

    Ay = A*np.sin(theta)
    Az = A*np.cos(theta)

## ------------ Macaulay in y -------------- ##

    ## [H1y,H2y,H3y,cf1,cf2]

    ## Maccauly at Hinge 1

    C11 = 0.0
    C12 = 0.0
    C13 = 0.0
    C14 = -x1
    C15 = -1.0

    ## Maccauly at Hinge 2

    C21 = ((x2 - x1)**3)/6.0
    C22 = 0.0
    C23 = 0.0
    C24 = -x2
    C25 = -1.0

    ## Maccauly at Hinge 3

    C31 = ((x3 - x1)**3)/6.0
    C32 = ((x3 - x2)**3)/6.0
    C33 = 0.0
    C34 = -x3
    C35 = -1.0

    ## Force equilibrium

    C41 = 1.0
    C42 = 1.0
    C43 = 1.0
    C44 = 0.0
    C45 = 0.0

    ## Moment equilibrium
    
    C51 = x1
    C52 = x2
    C53 = x3
    C54 = 0.0
    C55 = 0.0

    ## Matric of coefficients

    C = np.array([[C11, C12, C13, C14, C15],
                  [C21, C22, C23, C24, C25],
                  [C31, C32, C33, C34, C35],
                  [C41, C42, C43, C44, C45],
                  [C51, C52, C53, C54, C55]])

    ## Matrix of knowns K

    K1 = (qy/24.0)*(x1**4) + (E*Izz*dy1)
    K2 = (qy/24.0)*(x2**4) + (Ay/6.0)*((x2+(xa/2.0)-x2)**3) + (E*Izz*dy2)
    K3 = (qy/24.0)*(x3**4) + (Ay/6.0)*((x3+(xa/2.0)-x2)**3) + (Py/6.0)*((x3-(xa/2.0)-x2)**3) + (E*Izz*dy3)
    K4 = qy*L + Py + Ay
    K5 = (qy/2.0)*(L**2) + Ay*(x2-(xa/2.0)) + Py*(x2+(xa/2.0))

    K = np.array([K1, K2, K3, K4, K5])

## ------------ Macaulay in z -------------- ##
    
    ## [H1z,H2z,H3z,cf1,cf2]

    ## Maccauly at Hinge 1

    D11 = 0.0
    D12 = 0.0
    D13 = 0.0
    D14 = x1
    D15 = 1.0

    ## Maccauly at Hinge 2
    
    D21 = ((x2 - x1)**3)/6.0
    D22 = 0.0
    D23 = 0.0
    D24 = x2
    D25 = 1.0

    ## Maccauly at Hinge 3

    D31 = ((x3 - x1)**3)/6.0
    D32 = ((x3 - x2)**3)/6.0
    D33 = 0.0
    D34 = x3
    D35 = 1.0

    ## Force equilibrium

    D41 = 1.0
    D42 = 1.0
    D43 = 1.0
    D44 = 0.0
    D45 = 0.0

    ## Moment equilibrium
    
    D51 = x1
    D52 = x2
    D53 = x3
    D54 = 0.0
    D55 = 0.0

    ## Matric of coefficients

    D = np.array([[D11, D12, D13, D14, D15],
                  [D21, D22, D23, D24, D25],
                  [D31, D32, D33, D34, D35],
                  [D41, D42, D43, D44, D45],
                  [D51, D52, D53, D54, D55]])

    ## Matrix of knowns K

    M1 = (qz/24.0)*(x1**4) + (E*Iyy*dz1)
    M2 = (qz/24.0)*(x2**4) - (Az/6.0)*((x2+(xa/2.0)-x2)**3) + (E*Iyy*dz2)
    M3 = (qz/24.0)*(x3**4) - (Az/6.0)*((x3+(xa/2.0)-x2)**3) - (Pz/6.0)*((x3-(xa/2.0)-x2)**3) + (E*Iyy*dz3)
    M4 = qz*L - Pz - Az
    M5 = (qz/2.0)*(L**2) - Az*(x2-(xa/2.0)) - Pz*(x2+(xa/2.0))

    M = np.array([M1, M2, M3, M4, M5])



    Zf = np.linalg.solve(D, M)

    Yf = np.linalg.solve(C, K)

    return (Yf, Zf, Ay, qy, Py, Az, qz, Pz, x1, x2, x3, xa, E, theta, A)


RF = reactionforces(Izz, Iyy)
Yf = RF[0]
H1y = Yf[0]
H2y = Yf[1]
H3y = Yf[2]
Cfy1 = Yf[3]
Cfy2 = Yf[4]

Ay = RF[2]
qy = RF[3]
Py = RF[4]

Zf = RF[1]
H1z = Zf[0]
H2z = Zf[1]
H3z = Zf[2]
Cfz1 = Zf[3]
Cfz2 = Zf[4]

Az = RF[5]
qz = RF[6]
Pz = RF[7]

x1 = RF[8]
x2 = RF[9]
x3 = RF[10]
xa = RF[11]
E = RF[12]
theta = RF[13]
A = RF[14]

## ------------ Input Analytical Model -------------- ##

f = open("Rotationup.txt", "r")
lines = f.readlines()
f.close()

xan = []
Vza = []
Vya = []
Mza = []
Mya = []
Txa = []

for line in lines:
    
        line = line.strip("\n")
        line = line.split("\t")

        xan.append(float(line[0]))
        Vza.append(float(line[1]))
        Vya.append(float(line[2]))
        Mya.append(float(line[3]))
        Mza.append(float(line[4]))
        Txa.append(float(line[5]))

xan = np.asarray(xan)/1000
Vza = np.asarray(Vza)*1000
Vya = np.asarray(Vya)*1000
Mza = np.asarray(Mza)*1000
Mya = np.asarray(Mya)*1000
Txa = np.asarray(Txa)*1000

k = open("Deflection.txt", "r")
lines2 = k.readlines()
k.close()

xdan = []
dya = []
dza = []
dva = []

for line2 in lines2:

    line2 = line2.strip("\n")
    line2 = line2.split("\t")

    xdan.append(float(line2[0]))
    dza.append(float(line2[1]))
    dya.append(float(line2[2]))

xdan = np.asarray(xdan)/1000
dya = (np.asarray(dya)/1000)*np.cos(theta)
dza = (np.asarray(dza)/1000)*np.sin(theta)

dva = dya - dza

## ------------- Deflection --------------- ##

def deflections(x):

    #Deflections in y-direction
    if x >= 0:
        y = (qy*x**4)/24. 
    if x >= x1:
        y = y - (H1y/6.)*(x-x1)**3
    if x >= (x2-xa/2.):
        y = y + (Ay/6.)*(x-x2+xa/2.)**3
    if x >= x2:
        y = y - (H2y/6.)*(x-x2)**3
    if x >= (x2+xa/2.):
        y = y + (Py/6.)*(x-x2-xa/2.)**3
    if x >= x3:
        y = y - (H3y/6.)*(x-x3)**3.
        
    y = (y+Cfy1*x+Cfy2)/(-E*Izz)

    # Deflections in z-direction
    if x >= 0:
        z = (-qz*x**4)/24. 
    if x >= x1:
        z = z + (H1z/6.)*(x-x1)**3
    if x >= (x2-xa/2.):
        z = z + (Az/6.)*(x-x2+xa/2.)**3
    if x >= x2:
        z = z + (H2z/6.)*(x-x2)**3
    if x >= (x2+xa/2.):
        z = z + (Pz/6.)*(x-x2-xa/2.)**3
    if x >= x3:
        z = z + (H3z/6.)*(x-x3)**3
        
    z = (z+Cfz1*x+Cfz2)/(-E*Iyy)
    
    #Total deflection
    v = y*np.cos(theta)-z*np.sin(theta)

    return (v, y, z)

## ----------- Shear diagrams ------------ ##

x = np.arange(0., 2.692, 0.001)

def sheardiagram(x):

    #y-direction

    if x >= 0:
        Sy = -qy*x
    if x >= x1:
        Sy = Sy + H1y
    if x >= (x2-xa/2.):
        Sy = Sy - Ay
    if x >= x2:
        Sy = Sy + H2y
    if x >= (x2+xa/2.):
        Sy = Sy - Py
    if x >= x3:
        Sy = Sy + H3y

    #z-direction

    if x >= 0:
        Sz = qz*x
    if x >= x1:
        Sz = Sz - H1z
    if x >= (x2-xa/2.):
        Sz = Sz - Az
    if x >= x2:
        Sz = Sz - H2z
    if x >= (x2+xa/2.):
        Sz = Sz - Pz
    if x >= x3:
        Sz = Sz - H3z

    return (Sy, Sz)

Sy = []
Sz = []
for j in x:
    Sy.append(sheardiagram(j)[0])
    Sz.append(sheardiagram(j)[1])

## ---------- Moment Diagram ---------- ##

def momentdiagram(x):
    
    #Moment about the z - axis

    if x >= 0:
        Mz = -qy/2.*x**2
    if x >= x1:
        Mz = Mz + H1y*(x-x1)
    if x >= (x2-xa/2.):
        Mz = Mz - Ay*(x-x2+xa/2.)
    if x >= x2:
        Mz = Mz + H2y*(x-x2)
    if x >= (x2+xa/2.):
        Mz = Mz - Py*(x-x2-xa/2.)
    if x >= x3:
        Mz = Mz + H3y*(x-x3)

    #Moment about the y - axis

    if x >= 0:
        My = qz/2.*x**2
    if x >= x1:
        My = My - H1z*(x-x1)
    if x >= (x2-xa/2.):
        My = My - Az*(x-x2+xa/2.)
    if x >= x2:
        My = My - H2z*(x-x2)
    if x >= (x2+xa/2.):
        My = My - Pz*(x-x2-xa/2.)
    if x >= x3:
        My = My - H3z*(x-x3)

    return (My, Mz)

My = []
Mz = []
for k in x:
    My.append(momentdiagram(k)[0])
    Mz.append(momentdiagram(k)[1])

## ---------- Torsion Diagram ---------- ##

def torsiondiagram():

    x2 = 1.051
    xa = 0.3
    theta = 25.0*(np.pi)/180.
    q = 1.0*(10**3)
    L = 2.691
    P = 20.6*(10**3)
    ch = 0.515
    h = 0.248

    n = 2100
    
    T = list()
    xt = list()
    x = -L/(2*n)
    
    for i in range(1,n+1):
        
        x += L/n 
        xt += [x]
        
        torsion = -q * x * (0.25*ch - h/2) * np.cos(theta)
        if x > x2 - xa / 2: 
            torsion -= A * h/2 * (np.cos(theta) - np.sin(theta))
        if x > x2 + xa / 2:
            torsion -= P * h/2 * (np.cos(theta) - np.sin(theta))
        T += [torsion]
        
    return (T, xt)

tors = torsiondiagram()
Tx = tors[0]
xt = tors[1]

v = []
z = []
y = []
for i in x:
    v.append(deflections(i)[0])
    z.append(deflections(i)[2])
    y.append(deflections(i)[1])


## ------- Comparison of shear / moment / torque diagrams ------- ##

plt.subplot(321)
plt.plot(x, Sy,"r-",label='Numerical', marker = "^", markevery=100)
plt.plot(xan, Vya,"-b",label='Analytical', marker = "o", markevery=2)
plt.axis([0,2.691,-30000,50000])
plt.title('Shear Force Diagram in Y Direction')
plt.xlabel('x [m]')
plt.ylabel('Vy [N]')
plt.legend(loc='lower left')
plt.grid(True)
plt.subplot(322)
plt.plot(x, Mz,"r-",label='Numerical', marker = "^", markevery=100)
plt.plot(xan, Mza,"-b",label='Analytical', marker = "o", markevery=2)
plt.axis([0,2.691,-5000,35000])
plt.title('Moment Diagram about the Z - Axis')
plt.xlabel('x [m]')
plt.ylabel('Mz [Nm]')
plt.legend(loc='upper right')
plt.grid(True)
plt.subplot(323)
plt.plot(x, Sz,"r-",label='Numerical', marker = "^", markevery=100)
plt.plot(xan, Vza,"-b",label='Analytical', marker = "o", markevery=2)
plt.axis([0,2.691,-100000,80000])
plt.title('Shear Force Diagram in Z Direction')
plt.xlabel('x [m]')
plt.ylabel('Vz [N]')
plt.legend(loc='lower right')
plt.grid(True)
plt.subplot(324)
plt.plot(x, My,"r-",label='Numerical', marker = "^", markevery=100)
plt.plot(xan, Mya,"-b",label='Analytical', marker = "o", markevery=2)
plt.axis([0,2.691,-80000,10000])
plt.title('Moment Diagram about the Y - Axis')
plt.xlabel('x [m]')
plt.ylabel('My [Nm]')
plt.legend(loc='lower left')
plt.grid(True)
plt.subplot(325)
plt.plot(xt, Tx,"r-",label='Numerical', marker = "^", markevery=100)
plt.plot(xan, Txa,"-b",label='Analytical', marker = "o", markevery=2)
plt.axis([0,2.691,-500,2500])
plt.title('Torque Diagram about the X - Axis')
plt.xlabel('x [m]')
plt.ylabel('Tx [Nm]')
plt.legend(loc='upper left')
plt.grid(True)
plt.subplot(326)
plt.plot(x, v,"r",label='Numerical', marker = "^", markevery=100)
plt.plot([0,0.174,0.901,1.201,2.512,2.691],[0.0134,0.01154524,0.000662469,0.0000520333,0.02066,0.02464151],'bo',label='Analytical')
plt.axis([0,2.691,-0.01,0.03])
plt.title('Deflection due to bending')
plt.xlabel('x [m]')
plt.ylabel('delta() [m]')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()


print(deflections(x1)[0], deflections(x2)[1], deflections(x3)[0])
print(H1y, H2y, H3y, H1z, H2z, H3z, A)
