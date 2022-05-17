import numpy as np

class Layer:
    def __init__(size):
        size = size
        weights = []
        bias = []
        
    def activation(v):
        return v #f(v) whatever f may be

    # for each layer transforms the data
    # returns a vector of the transformed data
    def fp(input_data):
        return [np.dot(n, weights) for n in input_data] + bias

    def bp():
        pass

class Net:
    def __init__(rate):
        layers = []
        learning_rate = rate

    def error(r,s):
        pass

    def forward(self,data):
        for layer in self.layers:
            data = layer.fp(data)
        return data

    def back(self,result,solution):
        error = self.error(result,solution)
        for layer in reversed(self.layers):
            error = layer.bp(error)
    
    def train(dataset, n):
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
