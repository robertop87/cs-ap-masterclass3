# Solo se agregaron comentarios respecto del otro archivo

import cirq

def main():
    """
    Función principal que crea y ejecuta un circuito cuántico simple usando Cirq.
    """
    # Crear un qubit en la posición 0 de una línea
    qubit = cirq.LineQubit(0)

    # Crear un circuito cuántico
    circuit = cirq.Circuit()

    # Aplicar una puerta Hadamard (H) al qubit
    circuit.append(cirq.H(qubit))

    # Medir el qubit y almacenar el resultado con la clave 'm'
    circuit.append(cirq.measure(qubit, key='m'))

    # Crear un simulador cuántico
    simulator = cirq.Simulator()

    # Ejecutar el circuito en el simulador con 1024 repeticiones
    result = simulator.run(circuit, repetitions=1024)

    # Imprimir el histograma de los resultados de la medición
    print("Resultados de medición:", result.histogram(key='m'))

if __name__ == '__main__':
    main()
