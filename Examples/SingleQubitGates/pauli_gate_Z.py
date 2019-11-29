# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:59:22 2019

@author: rakshith kunchum

Simple program to demosntrate Pauli's Z gate.
It is a phase flip gate. It negates the phase when qubit is on.

Typical Output:
Circuit:
0: ───Z───M('q0')─────────────

1: ───Z───Z─────────M('q1')───

2: ───H───Z─────────M('q2')───

Results:
q0=0000000000
q1=0000000000
q2=0001001010
Counter({0: 10})
Counter({0: 10})
Counter({0: 7, 1: 3})
"""
import cirq


def main():
    circuit = cirq.Circuit()
    qubit = cirq.LineQubit.range(3)
    # applying just the pauli-y gate on |0>.
    circuit.append(cirq.Z(qubit[0]))
    circuit.append(cirq.measure(qubit[0], key='q0'))
    
    # applying 2 pauli-y gates on |0>
    circuit.append([cirq.Z(qubit[1]), cirq.Z(qubit[1]), cirq.measure(qubit[1], key='q1')])
    
    #applying pauli-y gate after hadamard gate.
    circuit.append([cirq.H(qubit[2]), cirq.Z(qubit[2]), cirq.measure(qubit[2], key='q2')])
    
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=10)
    print("Circuit:\n", circuit)
    print("\nResults:\n", results)
    for i in range(3):
        print(results.histogram(key='q'+str(i)))

if __name__ == '__main__':
    main()
    