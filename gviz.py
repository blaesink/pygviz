class Tree:
    """A Tree is for hierarchy
    :param: top -- top level node for this Tree
    :param: layers -- lists of strings that are layers each layer is a child to
    the layer above (top is the highest layer)
    """
    def __init__(self, top: str):
        self.top = top
        self.layers = []

    def add_layer(self, nodes: list):
        """Adds a layer to the tree"""
        assert isinstance(nodes, list)
        self.layers.append(nodes)

    def generate(self)
