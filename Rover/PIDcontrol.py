import time

class PID:
    #Really basic PID controller. Has manually set delta-t, maybe implement a system to check, rather than assuming it's constant?
    def __init__(self, Cp, Ci, Cd, IFactor = .9):
        self.Cp = Cp 
        self.Ci = Ci 
        self.Cd = Cd
        self.oldtime = time.time()
        self.IFactor = IFactor #Determines falloff curve for integral term
        self.P = 0
        self.I = 0
        self.D = 0
        self.oldError = 0
    def update(self, error): #Call this for one cycle of the controller
        delta = time.time() - self.oldtime
        self.oldtime = time.time()
        self.P = (self.Cp*error)
        self.I = (self.IFactor*self.I)+(self.Ci*(1-self.IFactor)*error*delta)
        self.D = (self.Cd*(error-self.oldError)/delta) #Only one previous sample taken. Will perform badly in response to large disturbances.
        self.oldError = error
        return self.P+self.I+self.D
    def reset(self): #Resets terms to 0, to reduce issues due to changing the target point
        self.oldtime = time.time()
        self.I = 0
        self.oldError = 0
