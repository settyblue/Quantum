# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:07:44 2019

@author: rakshith kunchum
This circuit demostrates entanglement.

Circuit:
0: ───H───@───
          │
1: ───────X───
[ 0.707+0.j  0.   +0.j -0.   +0.j  0.707+0.j]

The measured output state of both the qubits can only be either 00 or 11. It
cannot be 01 or 10.
"""
import cirq
import numpy as np


def main():
    circuit = cirq.Circuit()
    (q0, q1) = cirq.LineQubit.range(2)
    circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
    sim = cirq.Simulator()
    results = sim.simulate(circuit, qubit_order = [q0, q1])
    print("Circuit:", circuit, sep='\n')
    print(np.around(results.final_state, 3))


if __name__ == '__main__':
    main()
