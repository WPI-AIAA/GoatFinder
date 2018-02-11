class PID:
    #Really basic PID controller. Has manually set delta-t, maybe implement a system to check, rather than assuming it's constant?
    def __init__(self, Cp, Ci, Cd, delta, IFactor = .9):
        self.Cp = Cp 
        self.Ci = Ci 
        self.Cd = Cd
        self.delta = delta
        self.IFactor = IFactor #Determines falloff curve for integral term
        self.P = 0
        self.I = 0
        self.D = 0
        self.oldError = 0
    def update(self, error): #Call this for one cycle of the controller
        self.P = (self.Cp*error)
        self.I = (self.IFactor*self.I)+(self.Ci*(1-self.IFactor)*error*self.delta)
        self.D = (self.Cd*(error-self.oldError)/self.delta) #Only one previous sample taken. Will perform badly in response to large disturbances.
        self.oldError = error
        return P+I+D
    def reset(self): #Resets terms to 0, to reduce issues due to changing the target point
        self.I = 0
        self.oldError = 0