from Probability import DistribTriang

class Workshop:
    def __init__(self, name, position, tcycle = 0):
        self.name = name
        self.ina = []
        self.oua = []
        self.tcycle = tcycle
        self.topLeftCorner = position
        self.dailyQty = -1
        self._num = 0
        if(name=="Mine"):
            self.distribution = DistribTriang(10,20,30)
            self.dailyQty = self.distribution.mcInv()

    def setBehavior(self, bt):
        self.behavior = bt

    def addInEdge(self, transit):
        self.ina.append(transit)

    def addOutEdge(self, transit):
        self.oua.append(transit)

    def render(self,g,w,h):
        bbox = (self.topLeftCorner["x"], self.topLeftCorner["y"], self.topLeftCorner["x"] + w,
                self.topLeftCorner["y"] + h)
        g.create_rectangle(bbox, width=1, outline="black", fill="gray70")
        g.create_text((bbox[0] + w/2, bbox[1] + 20), text=str(self.name), font=('times', 12, 'bold'), fill='black')
        if(self.dailyQty != -1):
            g.create_text((bbox[0] + w/2, bbox[1] + 40), text=str(self.dailyQty), font=('times', 12), fill='black')
        elif(self._num >0):
            g.create_text((bbox[0] + w/2, bbox[1] + 40), text="Transport: "+str(self._num), font=('times', 12), fill='dark green')

    def update(self):
        self.behavior.update()

    def computeDailyQty(self):
        if self.distribution :
            self.dailyQty = self.distribution.mcInv()

