# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:23:25 2019

@author: rakshith kunchum

Simple program to demonstrate Pauli's X gate.
X gate is sometimes also called as Flip-gate. 
It inverts the amplitude of the qubit in computational basis.

Typical Output
Circuit:
0: ───X───M('q0')─────────────

1: ───X───X─────────M('q1')───

2: ───H───X─────────M('q2')───

Results:
q0=1111111111
q1=0000000000
q2=1100000000
Counter({1: 10})
Counter({0: 10})
Counter({0: 8, 1: 2})
"""
import cirq


def main():
    circuit = cirq.Circuit()
    (q0,q1,q2) = cirq.LineQubit.range(3)
    # applying just pauli-x gate on |0> qubit.
    circuit.append(cirq.X(q0))
    circuit.append(cirq.measure(q0, key='q0'))
    
    # applying 2 pauli-x gates on |0> qubit.
    circuit.append([cirq.X(q1), cirq.X(q1), cirq.measure(q1, key='q1')])
    
    # applying pauli-x gate after hadamard gate.
    circuit.append([cirq.H(q2), cirq.X(q2), cirq.measure(q2, key='q2')])
    
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=10)
    print("Circuit:\n", circuit)
    print("\nResults:\n", results)
    print(results.histogram(key='q0'))
    print(results.histogram(key='q1'))
    print(results.histogram(key='q2'))
    
    
if __name__ == '__main__':
    main()