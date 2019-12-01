# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:49:26 2019

@author: rakshith kunchum
This program demonstrates the qubit state being teleported. This method
destroys the original qubit state, since it will be measured.

Typical Output:
[-0.042+0.649j  0.445+0.616j]
Circuit:
0: ───X^0.217───Y^0.564───@───H─────────M('qm')───@───
                          │                       │
1: ───H─────────@─────────X───M('q1')───@─────────┼───
                │                       │         │
2: ─────────────X───────────────────────X─────────@───
Results:
measurements: q1=0 qm=0
output vector: (-0.042+0.649j)|000⟩ + (0.445+0.616j)|001⟩
[-0.042+0.649j  0.445+0.616j  0.   +0.j     0.   +0.j     0.   +0.j
 -0.   +0.j     0.   +0.j    -0.   +0.j   ]
"""
import cirq
import numpy as np
import random


def main():
    random_x = random.random()
    random_y = random.random()
    
    # Build circuit to exhibit random state.
    q_rand = cirq.LineQubit(0)
    random_state = cirq.Simulator().simulate(
            cirq.Circuit([cirq.X(q_rand)**random_x, cirq.Y(q_rand)**random_y]))
    print(np.around(random_state.final_state, 3))
    
    circuit = cirq.Circuit()
    # qm is the message qubit to be teleported.
    # q1 is the qubit with sender.
    # q2 is the qubit with receiver.
    (qm, q1, q2) = cirq.LineQubit.range(3)
    
    # Initially create a bell state to be shared between sender and receiver.
    circuit.append([cirq.H(q1), cirq.CNOT(q1, q2)])
    # Create a random state for the message using rotation gates.
    circuit.append([cirq.X(qm)**random_x, cirq.Y(qm)**random_y])
    
    circuit.append([cirq.CNOT(qm, q1), cirq.H(qm)])
    circuit.append([cirq.measure(qm, key='qm'), cirq.measure(q1, key='q1')])
    circuit.append([cirq.CNOT(q1, q2), cirq.CZ(qm, q2)])
    
    sim = cirq.Simulator()
    results = sim.simulate(circuit, qubit_order=[qm, q1, q2])
    print("Circuit:", circuit, sep='\n')
    print("Results:", results, sep='\n')
    print(np.around(results.final_state, 3))

    
if __name__ == '__main__':
    main()