from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  # Usar AerSimulator en lugar de Aer
from qiskit.visualization import plot_histogram  # Para visualización de resultados

def main():
    # Crear un circuito cuántico con 1 qubit y 1 bit clásico
    qc = QuantumCircuit(1, 1)

    # Aplicar la puerta Hadamard al qubit 0
    qc.h(0)

    # Medir el qubit 0 y almacenar el resultado en el bit clásico 0
    qc.measure(0, 0)

    # Usar AerSimulator como el backend
    simulator = AerSimulator()

    # Ejecutar el circuito en el simulador con 1024 shots
    job = simulator.run(qc, shots=1024)
    result = job.result()

    # Obtener los conteos de las mediciones
    counts = result.get_counts()
    print("Resultados de medición:", counts)

    # Visualizar los resultados usando un histograma
    # plot_histogram(counts).show()

    # Esperar una entrada del teclado antes de cerrar
    # input("Presiona cualquier tecla para cerrar la gráfica y salir...")

if __name__ == "__main__":
    main()
