import random
import matrix
from neural import NeuralNetwork

a = 0.1
I = [[0.2], [0.12], [0.3]]
t = [[0.5], [0.1], [0.75]]
W_i_h = [[0.1, 0.3, 0.4], [0.11, 0.05, 0.6], [0.15, 0.2, 0.22]]
W_h_o = [[0.1, 0.2, 0.05], [0.02, 0.4, 0.13], [0.2, 0.5, 0.09]]

for _ in range(10000):
    O_h = matrix.f_activate(matrix.mult(W_i_h, I))
    O_o = matrix.f_activate(matrix.mult(W_h_o, O_h))

    E_o = matrix.minus(t, O_o)
    E_h = matrix.mult(matrix.transpose(W_h_o), E_o)

    dW_i_h = matrix.multElement(matrix.multElement(E_h, O_h),
                                matrix.minusConst(O_h, 1))
    dW_i_h = matrix.mult(dW_i_h, matrix.transpose(I))
    dW_i_h = matrix.multConst(dW_i_h, a)
    W_i_h = matrix.sumMatrix(W_i_h, dW_i_h)

    dW_h_o = matrix.multElement(matrix.multElement(E_o, O_o),
                                matrix.minusConst(O_o, 1))
    dW_h_o = matrix.mult(dW_h_o, matrix.transpose(O_o))
    dW_h_o = matrix.multConst(dW_h_o, a)
    W_h_o = matrix.sumMatrix(W_h_o, dW_h_o)

# print(O_o)

random.seed(42)
I2 = [[0.2], [0.12]]
t2 = [[0.5], [0.1]]
net = NeuralNetwork(2, 4, 2, 0.1)
print(net.query(I2))
for i in range(1000):
    net.train(I2, t2)
print(net.query(I2))
