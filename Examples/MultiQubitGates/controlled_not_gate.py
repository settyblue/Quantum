# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:48:09 2019

@author: rakshith kunchum

Simple program to demonstrate Controlled-NOT gate.
Circuit:
0: ───H───@───M('q0')───
          │
1: ───────X───M('q1')───
Results:
q0=0111100111
q1=0111100111
Counter({1: 7, 0: 3})
Counter({1: 7, 0: 3})
"""
import cirq


def main():
    circuit = cirq.Circuit()
    (q0, q1) = cirq.LineQubit.range(2)
    circuit.append([cirq.H(q0), cirq.CNOT(q0, q1),
                    cirq.measure(q0, key='q0'), cirq.measure(q1, key='q1')])
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=10)
    print("Circuit:", circuit, sep='\n')
    print("Results:", results, sep='\n')
    print(results.histogram(key='q0'))
    print(results.histogram(key='q1'))
    
if __name__ == '__main__':
    main()