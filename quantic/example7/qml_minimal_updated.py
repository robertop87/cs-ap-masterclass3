# Solo se agregan comentarios respecto del anterior archivo

import pennylane as qml
from pennylane import numpy as np  # Importar numpy de PennyLane

# Definir un dispositivo cuántico con 1 qubit
dev = qml.device('default.qubit', wires=1)

# Definir un circuito cuántico usando un QNode
@qml.qnode(dev)
def circuit(params, x=None):
    """
    Circuito cuántico que aplica rotaciones RX y RY, y mide la esperanza de Pauli Z.

    Parámetros:
        params (array): Parámetros del circuito (en este caso, un solo ángulo para RY).
        x (float): Ángulo de rotación para la puerta RX.

    Retorna:
        float: Valor esperado de Pauli Z en el qubit 0.
    """
    # Aplicar una rotación RX con ángulo x en el qubit 0
    qml.RX(x, wires=0)

    # Aplicar una rotación RY con el parámetro params[0] en el qubit 0
    qml.RY(params[0], wires=0)

    # Retornar el valor esperado de Pauli Z en el qubit 0
    return qml.expval(qml.PauliZ(0))

def main():
    """
    Función principal para ejecutar el circuito con diferentes entradas.
    """
    # Datos de entrada para el ángulo x
    x_data = [0.0, 1.57]  # 0.0 radianes (0 grados) y 1.57 radianes (~90 grados)

    # Parámetros del circuito (en este caso, un solo ángulo para RY)
    params = np.array([0.8], requires_grad=True)

    # Ejecutar el circuito para cada valor de x
    for x in x_data:
        res = circuit(params, x=x)
        print(f"Entrada x={x}, resultado={res}")

if __name__ == '__main__':
    main()