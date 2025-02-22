from qiskit import QuantumCircuit, Aer, execute

def grover_2qubits():
    qc = QuantumCircuit(2, 2)

    # 1. Superposición
    qc.h([0, 1])

    # 2. Oráculo para |11>
    qc.x(0)
    qc.x(1)
    qc.h(1)
    qc.cx(0,1)
    qc.h(1)
    qc.x(0)
    qc.x(1)

    # 3. Difusor
    qc.h([0,1])
    qc.x([0,1])
    qc.h(1)
    qc.cx(0,1)
    qc.h(1)
    qc.x([0,1])
    qc.h([0,1])

    qc.measure([0,1],[0,1])
    return qc

def main():
    qc = grover_2qubits()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print("Grover 2qubits:", counts)

if __name__ == "__main__":
    main()