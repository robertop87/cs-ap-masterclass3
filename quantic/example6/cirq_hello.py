import cirq

def main():
    qubit = cirq.LineQubit(0)
    circuit = cirq.Circuit()
    circuit.append(cirq.H(qubit))
    circuit.append(cirq.measure(qubit, key='m'))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    print("Resultados de medición:", result.histogram(key='m'))

if __name__ == '__main__':
    main()