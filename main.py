import math
import matrix


def sigma(x):
    return 1 / (1 + math.exp(-x))


a = 0.1
i = [[0.2], [0.12], [0.3]]
t = [[0.5], [0.1], [0.75]]
W_i_h = [[0.1, 0.3, 0.4], [0.11, 0.05, 0.6], [0.15, 0.2, 0.22]]
W_h_o = [[0.1, 0.2, 0.05], [0.02, 0.4, 0.13], [0.2, 0.5, 0.09]]

X = matrix.mult(W_i_h, i)
O_h = [[sigma(x[0])] for x in X]

X1 = matrix.mult(W_h_o, O_h)
O_o = [[sigma(x[0])] for x in X1]

E_o = matrix.minus(t, O_o)
E_h = matrix.mult(matrix.transpose(W_h_o), E_o)

dW_h_o = [[0]*3 for i in range(3)]
dW_h_o = matrix.multElement(matrix.multElement(E_o, O_o),
                            matrix.minusConst(O_o, 1))
dW_h_o = matrix.multConst(dW_h_o, a)
dW_h_o = matrix.mult(dW_h_o, matrix.transpose(O_o))

dW_i_h = [[0]*3 for i in range(3)]
dW_i_h = matrix.multElement(matrix.multElement(E_h, O_h),
                            matrix.minusConst(O_h, 1))
dW_i_h = matrix.multConst(dW_i_h, a)
dW_i_h = matrix.mult(dW_i_h, matrix.transpose(i))

print(dW_h_o)
print(dW_i_h)
