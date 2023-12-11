from random import random


class NeuralNetwork:
    def __init__(self, i_nodes, h_nodes, o_nodes, lr):
        self.input_nodes = i_nodes
        self.hidden_nodes = h_nodes
        self.output_nodes = o_nodes
        self.learning_rate = lr

        self.W_i_h = [[0]*self.input_nodes for i in range(self.hidden_nodes)]
        for i in range(self.hidden_nodes):
            for j in range(self.input_nodes):
                self.W_i_h[i][j] = random()

        self.W_h_o = [[0]*self.hidden_nodes for i in range(self.output_nodes)]
        for i in range(self.output_nodes):
            for j in range(self.hidden_nodes):
                self.W_h_o[i][j] = random()

        print(self.W_i_h)
        print(self.W_h_o)


net = NeuralNetwork(2, 4, 2, 0.1)
