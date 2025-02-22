from qiskit.algorithms import Shor
from qiskit import BasicAer

def main():
    N = 15  # Factorizar 15 => factores (3, 5)
    shor = Shor()
    backend = BasicAer.get_backend('statevector_simulator')
    result = shor.factor(N, backend=backend)
    print(result)

if __name__ == "__main__":
    main()