import cirq

# pick a quibit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,
    cirq.measure(qubit, key='m')
)

print("Circuit:")
print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
