
def ribABD(Sz, Sy):
    from math import sin,cos, sqrt,atan,pi,tan

    Ca=0.515
    ha=0.248
    #simplification with 3 booms

    #Forces, angles,


    qb1arm=0.13

    qb = []
    #shearflow lengths
    s= sqrt((0.5*ha)**2+(Ca-0.5*ha)**2)    #distance along which shearflow qb1 and qb2 act
    s3= ha    #distance along which shearflow qb3 acts
    #Equations
    #Moment Equation around boom 1 CCW=+
    qb23=(Sz*0.5*ha)/(qb1arm*s)
    qb.append(qb23)
    #Sum of forces in z-direction, left is positive
    b= atan((0.5*ha)/(Ca-0.5*ha)) #Angle b in radians

    qb13= (Sz - qb23*cos(b)*s)/(cos(b)*s)
    qb.append(qb13)

    #Sum of forces in y
    qb12 = (Sy - qb23*sin(b) + qb13*sin(b))/s3
    qb.append(qb12)

    #MAKE CUT AT 12
    #Take moment around boom1
    A= pi*(0.5*ha)
    Pz2=((2*A*qb12) + Sz*0.5*ha)/ha

    #Sum of forces in z-direction left=positive
    Pz1=-Pz2+Sz

    #Sum in forces in y-direction, down = pos
    Py1=Pz1*tan(b)
    Py2=Pz2*tan(b)
    qb1=(qb12*ha-Py1+Py2 -Sy)/ha
    qb.append(qb1)

    #TE Cell spar12
    qb2=(qb1*ha-Py1-Py2-Sy)/ha
    qb.append(qb2)
    return max(qb)