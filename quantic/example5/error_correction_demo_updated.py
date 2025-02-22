from qiskit import QuantumCircuit  # Importar QuantumCircuit desde qiskit
from qiskit_aer import Aer  # Importar Aer desde qiskit_aer
import random  # Para generar números aleatorios

def simple_bit_flip_demo(p=0.1):
    """
    Simula un circuito cuántico con errores de bit-flip en 3 qubits.

    Parámetros:
        p (float): Probabilidad de que ocurra un error de bit-flip en cada qubit.

    Retorna:
        QuantumCircuit: Circuito cuántico con errores de bit-flip y mediciones.
    """
    # Crear un circuito cuántico con 3 qubits y 3 bits clásicos
    qc = QuantumCircuit(3, 3)

    # Aplicar errores de bit-flip con probabilidad p
    for i in range(3):
        if random.random() < p:
            qc.x(i)  # Aplicar puerta X (bit-flip) al qubit i con probabilidad p

    # Medir los qubits y almacenar los resultados en los bits clásicos
    qc.measure([0, 1, 2], [0, 1, 2])

    return qc

def main():
    """
    Función principal para ejecutar la simulación del circuito con errores de bit-flip.
    """
    # Crear el circuito con una probabilidad de error de 0.2 (20%)
    circuit = simple_bit_flip_demo(0.2)

    # Obtener el backend del simulador Qiskit Aer
    backend = Aer.get_backend('qasm_simulator')

    # Ejecutar el circuito en el simulador con 1 shot (una ejecución)
    job = backend.run(circuit, shots=1)
    result = job.result()

    # Obtener los conteos de las mediciones
    counts = result.get_counts()

    # Imprimir los resultados de la medición
    print("Resultado de la medición del circuito con errores:", counts)

if __name__ == "__main__":
    main()
