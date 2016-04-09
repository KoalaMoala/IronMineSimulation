class Transit:
    def __init__(self, name, input_workshops, output_workshops, stock_names, stock_max_quantities):
        self.name = name
        self.input = input_workshops
        self.output = output_workshops
        self.stockNames = stock_names
        self.stockQuantities = []
        self.stockMaxQuantities = stock_max_quantities

        # initializing by default stock quantities to 0
        for i in range(self.stockNames.length):
            self.stockQuantities.append(0)