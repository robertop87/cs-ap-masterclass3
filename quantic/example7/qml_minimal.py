import pennylane as qml
from pennylane import numpy as np

dev = qml.device('default.qubit', wires=1)

@qml.qnode(dev)
def circuit(params, x=None):
    qml.RX(x, wires=0)
    qml.RY(params[0], wires=0)
    return qml.expval(qml.PauliZ(0))

def main():
    x_data = [0.0, 1.57]
    params = np.array([0.8], requires_grad=True)
    for x in x_data:
        res = circuit(params, x=x)
        print(f"Entrada x={x}, resultado={res}")

if __name__ == '__main__':
    main()