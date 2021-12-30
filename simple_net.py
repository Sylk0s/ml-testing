import random
import math

# training neural net to preform XOR
data = [
    [[0,0],0],
    [[0,1],1],
    [[1,0],1],
    [[1,1],0]
]

def logistic_function(net_in):
    return 1.0/(1.0+math.pow(math.e,-net_in))

def parse_data():
    pass

class Node:
    # I don't completly understand why bias exists so im just gonna ignore it for now
    def __init__(self, layer):
        self.layer = layer
        self.activation = 0

    # I'm chosing to do these init functions AFTER creation so that the network has info about it's structure
    def init_node(self):
        if self.layer.previous is None:
            pass
            # handles something else here leter
            # this means the layer is the first layer
        else:
            self.input_nodes = self.layer.previous.nodes
            self.input_weights = [random.random() for _ in self.input_nodes] # init with random intial weights

    # calculates the activation values for each node
    # this is the sum of the input activations times the weights
    def calculate_activation(self):
        self.activation = logistic_function(sum([self.input_nodes[i].activation*self.input_weights[i] for i in len(self.input_weights)]))

class NetLayer:
    def __init__(self, node_count, net):
        self.nodes = [Node(self) for _ in range(node_count)] # need to figure out how to handle first and last layers
        self.net = net

    def init_layer(self, previous):
        self.previous = previous
        for i in range(len(self.nodes)):
            self.nodes[i].init_node()

class NeuralNet:
    def __init__(self,layer_sizes):
        self.layers = [NetLayer(layer_sizes[s], self) for s in range(len(layer_sizes))]

        # passes the previous layer to each layer, is None is layer is the input layer
        for i in range(len(self.layers)):
            try:
                self.layers[i].init_layer(self.layers[i-1])
            except IndexError:
                self.layers[i].init_layer(None)
            

layers = 3
layer_sizes = [2,4,2]

net = NeuralNet(layer_sizes)

# It seems like the first layer is getting input weights which i think is correct but im not sure why its doing this
for layer in net.layers:
    lstr = ""
    for node in layer.nodes:
        lstr += str(node.input_weights)
    print(lstr+"\n")