class Workshop:
    def __init__(self, name, position, tcycle = 0):
        self.name = name
        self.ina = []
        self.oua = []
        self.tcycle = tcycle
        self.topLeftCorner = position

    def setBehavior(self, bt):
        self.behavior = bt

    def addInEdge(self, transit):
        self.ina.append(transit)

    def addOutEdge(self, transit):
        self.oua.append(transit)

    def render(self,g,w,h):
        bbox = (self.topLeftCorner["x"], self.topLeftCorner["y"], self.topLeftCorner["x"] + w,
                self.topLeftCorner["y"] + h)
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + w/2, bbox[1] + 20), text=str(self.name), font=('times', 14, 'bold'), fill='black')

    def update(self):
        self.behavior.update()
