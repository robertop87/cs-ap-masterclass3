from qiskit import QuantumCircuit, Aer, execute

def main():
    qc = QuantumCircuit(1, 1)
    qc.h(0)             # Aplica Hadamard al qubit 0
    qc.measure(0, 0)    # Mide el qubit 0 en el bit clásico 0

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print("Resultados de medición:", counts)

if __name__ == "__main__":
    main()