class Node:
    def __init__():
        self.layer = None
        self.weights = []
        self.value = None
        self.bias = None
        self.network = self.layer.network

    # activation function
    def activation(self, x):
        return max(0,x)

    # updates the value of the node according to the previous layer and weights
    def forward_prop(self):
        self.value = self.bias + sum([self.activation(n.value) for n in self.network.get_previous_layer(self.layer.index).nodes] * self.weights)

    # updates the weights according to the error function
    def back_prop(self):
        pass

class Layer:
    def __init__(n):
        self.nodes = []
        self.network = None
        self.index = None

    def forward_prop(self):
        for n in self.nodes:
            n.forward_prop()

    def back_prop():
        pass

class Network():
    def __init__(lr):
        self.layers = []
        self.rate = lr

    def add_layer(self, n):
        self.layers.push(Layer(n))

    def get_previous_layer(self, l):
        return self.layers[l-1] if l > 0 else None

    # excludes the first layer which holds data but doesn't have a previous layer
    def forward_prop(self):
        for l in range(1,len(self.layers)):
            self.layers[l].forward_prop()

    def back_prop(self):
        # cost function
        pass

    def train(self,inp):
        for i in range(len(self.layer[0].nodes)):
            self.layer[0].nodes[i].weight = inp[0][i]
        forward_prop()
        back_prop()

    def get_output(self):
        return max([v.value for v in self.layers[len(self.layers)-1].nodes])

# XOR dataset
data = [
        [[0,0],0],
        [[0,1],1],
        [[1,0],1],
        [[1,1],0]
        ]

net = Network(.1)

# training iteraitons
n = 1000
for _ in range(n):
    for c in data:
        net.train(c)
