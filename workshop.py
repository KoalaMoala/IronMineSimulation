class Workshop:
    def __init__(self, name, tree, ingredients_inputs, products_outputs):
        self.name = name
        self.input = ingredients_inputs  # transits before workshop
        self.output = products_outputs  # transits after workshop
        self.behaviorTree = tree




