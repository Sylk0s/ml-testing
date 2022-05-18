import numpy as np
import random as rand

class Layer:
    def __init__(self, size, prev, net):
        self.net = net
        self.size = size
        self.weights = [[rand.random() for _ in range(prev)] for _ in range(size)]
        self.bias = 0
        self.prev = prev

    def __str__(self):
        return f"Size: {self.size}, Weights: {self.weights}, Bias: {self.bias}"
        
    def activation(self):
        return v #f(v) whatever f may be

    # for each layer transforms the data
    # returns a vector of the transformed data
    def fp(self, input_data):
        return [np.dot(input_data, self.weights[n])+self.bias for n in range(self.size)]

    def bp(self):
        pass

class Net:
    # rate = learning rate of the network
    # sizes must include an array with the first element as the input data size,
    # the last element as the output size, and all inbetween the sizes of the layers desired
    def __init__(self, sizes, rate=0.1):
        self.layers = [Layer(sizes[s],(sizes[0] if s==0 else sizes[s-1]),self) for s in range(len(sizes))]
        self.learning_rate = rate

    def error(self, r,s):
        pass

    def forward(self,data):
        for layer in self.layers:
            data = layer.fp(data)
        return data

    def back(self,result,solution):
        error = self.error(result,solution)
        for layer in reversed(self.layers):
            error = layer.bp(error)
    
    def train(self, dataset, n):
        for _ in range(n):
            # [0][i] must have the same length as [1][i]
            # these represent inputs and results
            # both are vector values with a value between 0 and 1 for the correctness of an output
            # each value corrresponds to a node in the io layers
            for i in len(dataset[0]):
                data_in = dataset[0][i]
                solution = dataset[1][i]
                result = self.forward(data_in)
                self.back(result, solution)

net = Net([4,4,2])
print([f"{j}: {net.layers[j]}" for j in range(len(net.layers))])

print(net.forward([0,0,0,1]))
