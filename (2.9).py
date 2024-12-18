col = int(input())  # количество измерений
X = []
for i in range(0, col):
    X.append(int(input()))  # ввод значений х
Y = []
for i in range(0, col):
    Y.append(int(input()))  # ввод значений y


def MNK(col, X, Y):
    XY = []
    for i in range(0, col):
        XY.append(X[i] * Y[i])
    x_2 = []
    for i in range(0, col):
        x_2.append(X[i] ^ 2)
    chisl_a = col * sum(XY) - sum(X) * sun(Y)
    znamen_a = col * sum(x_2) - sum(X) ** 2
    a = chisl_a / znamen_a

    b = (sum(Y) - a * sum(X)) / col
    return (a, b)