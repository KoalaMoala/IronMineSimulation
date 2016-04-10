class Workshop:
    def __init__(self, name, tree):
        self.name = name
        self.behaviorTree = tree
        self.input = []
        self.output = []

    def set_transit(self, ingredients_inputs, products_outputs):
        self.input = ingredients_inputs  # transits before workshop
        self.output = products_outputs  # transits after workshop





