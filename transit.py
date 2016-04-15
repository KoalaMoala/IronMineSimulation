class Transit:
    def __init__(self, name, input_workshop, output_workshop, stock_name, stock_max_quantity, stock_actu=0, unit=''):
        self.name = name
        self.nodeFrom = input_workshop
        self.nodeTo = output_workshop
        self.stockName = stock_name
        self.w = stock_actu
        self.stockMaxQuantities = stock_max_quantity
        self.unit = unit

    def setNodeFrom(self, nodeFr):
        self.nodeFrom = nodeFr

    def setNodeTo(self, nodeTo):
        self.nodeTo = nodeTo

    def getCapacity(self):
        return self.stockMaxQuantities

    def render(self,g,w,h):
        if(self.nodeTo == None or self.nodeFrom == None):
            return
        bfont = ('times', 12)
        text_coordinate = {}
        pFromTo = []
        if(self.nodeFrom.topLeftCorner['x'] + w < self.nodeTo.topLeftCorner['x']):
            text_coordinate = {"x": (self.nodeFrom.topLeftCorner["x"] + self.nodeTo.topLeftCorner["x"] + w) / 2,
                                "y": (self.nodeFrom.topLeftCorner["y"] + self.nodeTo.topLeftCorner["y"]) / 2}
            pFromTo = [self.nodeFrom.topLeftCorner["x"] + w, self.nodeFrom.topLeftCorner["y"] + h/2,
                        self.nodeTo.topLeftCorner["x"], self.nodeTo.topLeftCorner["y"] + h/2]
        elif(self.nodeFrom.topLeftCorner['x'] > self.nodeTo.topLeftCorner['x'] + w) :
            text_coordinate = {"x": (self.nodeFrom.topLeftCorner["x"] + self.nodeTo.topLeftCorner["x"] + w) / 2,
                                "y": (self.nodeFrom.topLeftCorner["y"] + self.nodeTo.topLeftCorner["y"]) / 2}
            pFromTo = [self.nodeTo.topLeftCorner["x"], self.nodeTo.topLeftCorner["y"] + h/2,
                    self.nodeFrom.topLeftCorner["x"] + w, self.nodeFrom.topLeftCorner["y"] + h/2]
        elif(self.nodeFrom.topLeftCorner['y'] + h < self.nodeTo.topLeftCorner['y']):
            text_coordinate = {"x": (self.nodeFrom.topLeftCorner["x"] + self.nodeTo.topLeftCorner["x"] + w) / 2 + 50,
                                "y": (self.nodeFrom.topLeftCorner["y"] + self.nodeTo.topLeftCorner["y"]) / 2}
            pFromTo = [self.nodeFrom.topLeftCorner["x"] + w / 2, self.nodeFrom.topLeftCorner["y"] + h,
                        self.nodeTo.topLeftCorner["x"]+ w/2, self.nodeTo.topLeftCorner["y"]]
        elif(self.nodeFrom.topLeftCorner['y']  >= self.nodeTo.topLeftCorner['y'] + h):
            text_coordinate = {"x": (self.nodeFrom.topLeftCorner["x"] + self.nodeTo.topLeftCorner["x"] + w) / 2 + 50,
                                "y": (self.nodeFrom.topLeftCorner["y"] + self.nodeTo.topLeftCorner["y"]) / 2}
            pFromTo = [self.nodeTo.topLeftCorner["x"]+ w/2, self.nodeTo.topLeftCorner["y"],
                       self.nodeFrom.topLeftCorner["x"] + w / 2, self.nodeFrom.topLeftCorner["y"] + h]

        if len(pFromTo)>3 :
            g.create_line(pFromTo[0],pFromTo[1],pFromTo[2],pFromTo[3], width=1.5, fill="gray80")
            g.create_text((text_coordinate["x"], text_coordinate["y"] + 5), text=str(self.name), font=bfont, fill='black')
            g.create_text((text_coordinate["x"], text_coordinate["y"] + 25), text=str(self.stockName), font=bfont, fill='black')
            g.create_text((text_coordinate["x"], text_coordinate["y"] + 45), text=str(self.w)+self.unit, font=bfont, fill='black')
