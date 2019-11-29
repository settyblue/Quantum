# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:59:22 2019

@author: rakshith kunchum

Simple program to demosntrate Pauli's Y gate.
Y gates also flips the amplitude of the qubit in computational basis.
Y gate is a combination of pauli-X and pauli-Z gates.

Typical Output:
Circuit:
0: ───Y───M('q0')─────────────

1: ───Y───Y─────────M('q1')───

2: ───H───Y─────────M('q2')───

Results:
q0=1111111111
q1=0000000000
q2=1001111001
Counter({1: 10})
Counter({0: 10})
Counter({1: 6, 0: 4})
"""
import cirq


def main():
    circuit = cirq.Circuit()
    qubit = cirq.LineQubit.range(3)
    # applying just the pauli-y gate on |0>.
    circuit.append(cirq.Y(qubit[0]))
    circuit.append(cirq.measure(qubit[0], key='q0'))
    
    # applying 2 pauli-y gates on |0>
    circuit.append([cirq.Y(qubit[1]), cirq.Y(qubit[1]), cirq.measure(qubit[1], key='q1')])
    
    #applying pauli-y gate after hadamard gate.
    circuit.append([cirq.H(qubit[2]), cirq.Y(qubit[2]), cirq.measure(qubit[2], key='q2')])
    
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=10)
    print("Circuit:\n", circuit)
    print("\nResults:\n", results)
    for i in range(3):
        print(results.histogram(key='q'+str(i)))

if __name__ == '__main__':
    main()
    