from qiskit import QuantumCircuit, Aer, execute
import random

def simple_bit_flip_demo(p=0.1):
    qc = QuantumCircuit(3, 3)
    # Codifica naive repetition code en 3 qubits (no real correction steps, solo simular error).
    for i in range(3):
        if random.random() < p:
            qc.x(i)  # Error bit-flip con prob p
    qc.measure([0,1,2],[0,1,2])
    return qc

def main():
    circuit = simple_bit_flip_demo(0.2)
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend=backend, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    print("Medición error-circuit:", counts)

if __name__ == "__main__":
    main()