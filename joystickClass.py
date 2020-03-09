import pygame
import pickle
from .motorSpeed import calcSpeed
from .toServer import send

class joystickClass:

        buttunMap={}
        path="joys/"
        led = False

    def __init__(self, joyNum):
        pygame.init()
        self.joy = pygame.joystick.Joystick(joyNum) 
        self.joy.init()
        self.selectJoy()

    def selectJoy(self):
        name = raw_input("Enter JOY name: ")
        if name.trim() =="":
            name = "main"
        elif name,trim() == "reset":
            self.reset()
        else:
            pickleIn = open(self.path+name,"rb")
            self.buttunMap = pickle.load(pickleIn)

    def execute(self, event):
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis ==0 or event.axis ==1:
                axis01()
            elif event.axis ==2 or event.axis ==3:
                axis23()
        elif event.type == pygame.JOYHATMOTION:
            hat(event.value)
        elif event.type == pygame.JOYBUTTONDOWN:
            self.buttunMap[event.button]()
            # if event.button == 0:
            #     but0()
            # elif event.button == 1:
            #      but1() 
            # elif event.button == 2:
            #      but2()
            # elif event.button == 3:
            #      but3()
            # elif event.button == 4:
            #      but4()
            # elif event.button == 5:
            #      but5()
            # elif event.button == 6:
            #      but6()
            # elif event.button == 7:
            #      but7()
            # elif event.button == 8:
            #      but8()
            # elif event.button == 9:
            #      but9()
            # elif event.button == 10:
            #      but10()
            # elif event.button == 11:
            #      but11()
    def reset(self):
        buttonNames=["R1","R2","L1","L2","Tri","Rec","X","O","Start","select","AnalogR","AnalogL"]
        for i in buttonNames:
            self.setButtonMap(i)

        name = raw_input("Enter JOY name: ")
        pickleOut= open(self.path+name,"wb")
        pickle.dump(self.buttunMap,pickleOut)
        pickleOut.close()

    def setButtonMap(self,but):
        print("priss "+but+"\n")
        self.buttunMap[event.button]=but

    def R1(self):
        # code here
        send("speedUp=1")
    def R2(self):
        # code here
        send("speedDown=1")
    def L1(self):
        # code here
        send("ROVUp=1")
    def L2(self):
        # code here
        send("ROVDown=1")
    def but4(self):
        # code here
        send("ROVDown=1")
    def Tri(self):
        # code here
        send("armClose=1")
    def X(self):
        # code here
        send("armOpen=1")
    def O(self):
        # code here
        send("armRotR=1")
    def Rec(self):
        # code here
        send("armRotL=1")
    def Select(self):
        # code here
        send("stopAll=1")
    def but10(self):
        # code here
        send("connect=1","connectJoy")
    def AnalogR(self):
        # code here
        send("LED="+str(not self.led))

    def hat(value):
        #code here
        if value==(1,0):
            send("forwardMini=1")

        elif value==(-1,0):
            send("backMini=1")

        elif value==(0,0):
            send("stopMini=1")

        elif value==(0,1):
            send("openMiniArm=1")

        elif value==(0,-1):
            send("closeMiniArm=1")



    def axis01():
        #code here
        x=self.joy.get_axis(0)
        y=self.joy.get_axis(1)
        calcSpeed(x,y)

    def axis23():
        #code here
        x=self.joy.get_axis(0)
        y=self.joy.get_axis(1)
        cam(y) 








running = True
while running:
    for event in pygame.event.get():

        joy1.execute(event)
        joy2.execute(event)


 pygame.quit()



