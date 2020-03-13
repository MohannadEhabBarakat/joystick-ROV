from math import sin, cos 
from toServer import send

def calcSpeed(x,y):
    b=(y*cos(120)/sin(120)+x)/(cos(60)-cos(120)/sin(120))*170
    
    a=(-b*sin(60)+y)/sin(120)*170

    a1=a
    a2=-a
    b1=b
    b2=-b
    send("a1="+ str(a1))
    send("a2="+ str(a2))
    send("b1="+ str(b1))
    send("b2="+ str(b2))
    print("a: "+ str(a) + "     b: "+ str(b))

# calcSpeed(0,1)





