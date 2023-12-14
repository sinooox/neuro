import matrix
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

    def output(self):
        print(self.W_i_h)
        print(self.W_h_o)

    def query(self, inputs):
        self.O_h = matrix.f_activate(matrix.mult(self.W_i_h, inputs))
        self.O_o = matrix.f_activate(matrix.mult(self.W_h_o, self.O_h))

        return self.O_o

    def train(self, inputs, target):
        self.O_h = matrix.f_activate(matrix.mult(self.W_i_h, inputs))
        self.O_o = matrix.f_activate(matrix.mult(self.W_h_o, self.O_h))

        E_o = matrix.minus(target, self.O_o)
        E_h = matrix.mult(matrix.transpose(self.W_h_o), E_o)

        dW_i_h = matrix.multElement(matrix.multElement(E_h, self.O_h),
                                    matrix.minusConst(self.O_h, 1))
        dW_i_h = matrix.mult(dW_i_h, matrix.transpose(inputs))
        dW_i_h = matrix.multConst(dW_i_h, self.learning_rate)
        self.W_i_h = matrix.sumMatrix(self.W_i_h, dW_i_h)

        dW_h_o = matrix.multElement(matrix.multElement(E_o, self.O_o),
                                    matrix.minusConst(self.O_o, 1))
        dW_h_o = matrix.mult(dW_h_o, matrix.transpose(self.O_h))
        dW_h_o = matrix.multConst(dW_h_o, self.learning_rate)
        self.W_h_o = matrix.sumMatrix(self.W_h_o, dW_h_o)
