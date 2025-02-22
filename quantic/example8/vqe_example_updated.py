from qiskit_aer import Aer  # Importar Aer desde qiskit_aer
from qiskit_algorithms import VQE  # Importar VQE desde qiskit_algorithms
from qiskit.quantum_info import SparsePauliOp  # Importar SparsePauliOp para definir el Hamiltoniano
from qiskit.circuit.library import TwoLocal  # Importar TwoLocal para el ansatz
from qiskit_algorithms.optimizers import COBYLA  # Importar COBYLA como optimizador

def main():
    """
    Función principal para ejecutar el algoritmo VQE en un Hamiltoniano simple.
    """
    # 1. Definir un Hamiltoniano simple: H = Z ⊗ Z
    hamiltonian = SparsePauliOp.from_list([("ZZ", 1.0)])  # H = Z ⊗ Z

    # 2. Definir el ansatz (circuito variacional)
    ansatz = TwoLocal(
        num_qubits=2,  # Número de qubits
        rotation_blocks=["ry", "rz"],  # Bloques de rotación
        entanglement_blocks="cz",  # Bloques de entrelazamiento
        reps=1,  # Número de repeticiones
    )

    # 3. Definir el optimizador (COBYLA con un máximo de 50 iteraciones)
    optimizer = COBYLA(maxiter=50)

    # 4. Obtener el backend del simulador (statevector_simulator)
    backend = Aer.get_backend("statevector_simulator")

    # 5. Crear una instancia de VQE
    vqe = VQE(
        ansatz=ansatz,  # Circuito variacional
        optimizer=optimizer,  # Optimizador
        quantum_instance=backend,  # Backend para la simulación
    )

    # 6. Ejecutar VQE para encontrar el valor propio mínimo del Hamiltoniano
    result = vqe.compute_minimum_eigenvalue(operator=hamiltonian)

    # 7. Imprimir el valor propio mínimo aproximado
    print("Valor propio mínimo aproximado:", result.eigenvalue.real)

if __name__ == "__main__":
    main()