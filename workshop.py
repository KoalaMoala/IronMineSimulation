class Workshop:
    def __init__(self, name, tree,  ingredients_name, ingredients_inputs, ingredients_max_quantities, products_name,
                 products_outputs, products_max_quantities):
        self.name = name
        self.input = ingredients_inputs
        self.output = products_outputs
        self.behaviorTree = tree

        # ingredients
        self.ingredientsName = ingredients_name
        self.ingredientsQuantities = []
        self.ingredientsMaxQuantities = ingredients_max_quantities

        # initializing by default ingredients quantities to 0
        for i in range(len(self.ingredientsName)):
            self.ingredientsQuantities.append(0)

        # products
        self.productsName = products_name
        self.productsQuantities = []
        self.productsMaxQuantities = products_max_quantities

        # initializing by default products quantities to 0
        for i in range(len(self.productsName)):
            self.productsQuantities.append(0)



