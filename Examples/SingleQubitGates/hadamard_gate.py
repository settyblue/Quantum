# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:23:25 2019

@author: rakshith kunchum

Simple program to demonstrate Hadamard gate.
H gate creates a state which is in superposition when the
input is in any of the computational basis.

Typical Output
Circuit:
1: ───H───M('q0')───

Results:
q0=0011101111
Counter({1: 7, 0: 3})
"""
import cirq


def main():
    circuit = cirq.Circuit()
    q0 = cirq.LineQubit(1)
    circuit.append(cirq.H(q0))
    circuit.append(cirq.measure(q0, key='q0'))
    
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=10)
    print("Circuit:\n", circuit)
    print("\nResults:\n", results)
    print(results.histogram(key='q0'))


if __name__ == '__main__':
    main()