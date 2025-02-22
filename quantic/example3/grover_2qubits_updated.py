from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  # Usar AerSimulator en lugar de Aer
from qiskit.visualization import plot_histogram  # Para visualización de resultados

def grover_2qubits():
    # Crear un circuito cuántico con 2 qubits y 2 bits clásicos
    qc = QuantumCircuit(2, 2)

    # 1. Superposición: Aplicar puertas Hadamard a ambos qubits
    qc.h([0, 1])

    # 2. Oráculo para |11⟩
    qc.x(0)  # Aplicar puerta X al qubit 0
    qc.x(1)  # Aplicar puerta X al qubit 1
    qc.h(1)  # Aplicar puerta Hadamard al qubit 1
    qc.cx(0, 1)  # Aplicar puerta CNOT (controlada por el qubit 0, objetivo el qubit 1)
    qc.h(1)  # Aplicar puerta Hadamard al qubit 1
    qc.x(0)  # Aplicar puerta X al qubit 0
    qc.x(1)  # Aplicar puerta X al qubit 1

    # 3. Difusor (amplificación de amplitud)
    qc.h([0, 1])  # Aplicar puertas Hadamard a ambos qubits
    qc.x([0, 1])  # Aplicar puertas X a ambos qubits
    qc.h(1)  # Aplicar puerta Hadamard al qubit 1
    qc.cx(0, 1)  # Aplicar puerta CNOT (controlada por el qubit 0, objetivo el qubit 1)
    qc.h(1)  # Aplicar puerta Hadamard al qubit 1
    qc.x([0, 1])  # Aplicar puertas X a ambos qubits
    qc.h([0, 1])  # Aplicar puertas Hadamard a ambos qubits

    # Medir los qubits y almacenar los resultados en los bits clásicos
    qc.measure([0, 1], [0, 1])
    return qc

def main():
    # Crear el circuito de Grover para 2 qubits
    qc = grover_2qubits()

    # Usar AerSimulator como el backend
    simulator = AerSimulator()

    # Ejecutar el circuito en el simulador con 1024 shots
    job = simulator.run(qc, shots=1024)
    result = job.result()

    # Obtener los conteos de las mediciones
    counts = result.get_counts()
    print("Resultados de Grover para 2 qubits:", counts)

    # Visualizar los resultados usando un histograma
    plot_histogram(counts).show()

    # Esperar una entrada del teclado antes de cerrar
    input("Presiona cualquier tecla para cerrar la gráfica y salir...")

if __name__ == "__main__":
    main()
