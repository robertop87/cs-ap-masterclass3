from qiskit import Aer
from qiskit.algorithms import VQE
from qiskit.opflow import Z, I
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import COBYLA

def main():
    # 1. Definir Hamiltoniano simple: H = Z ^ Z
    hamiltonian = (Z ^ Z)

    ansatz = TwoLocal(rotation_blocks=['ry','rz'], entanglement_blocks='cz', reps=1)
    optimizer = COBYLA(maxiter=50)

    backend = Aer.get_backend('statevector_simulator')

    vqe = VQE(ansatz, optimizer=optimizer, quantum_instance=backend)
    result = vqe.compute_minimum_eigenvalue(operator=hamiltonian)

    print("Eigenvalue mínimo aproximado:", result.eigenvalue.real)

if __name__ == "__main__":
    main()