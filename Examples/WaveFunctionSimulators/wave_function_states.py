# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:36:38 2019

@author: rakshith kunchum
Simple program to demonstrate how to read the internal state of a wave function.
For n qubits, the internal state will have 2^n dimensions and each dimensional
value can be a complex number.
Typical Output:
Circuit:
0: ───H───Y───

1: ───H───Z───
[ 0.-0.5j  0.+0.5j  0.+0.5j -0.-0.5j]
"""
import cirq
import numpy as np

def main():
    circuit = cirq.Circuit()
    (q0, q1) = cirq.LineQubit.range(2)
    circuit.append([cirq.H(q0), cirq.Y(q0)])
    circuit.append([cirq.H(q1), cirq.Z(q1)])
    # Adding a measuring device will collapse the wave function.
    # This will not allow us to observe the state.
    # circuit.append(cirq.measure(q0, key= 'q0'))

    # So, in order to observe the state of the wave function, we will need
    # simulate without a measuring device.

    sim = cirq.Simulator()
    # set the qubit order to correctly read the value of the multi-qubit
    # state function.
    result = sim.simulate(circuit, qubit_order = [q0, q1])

    print("Circuit:", circuit, sep='\n')
    print(np.around(result.final_state, 3))


if __name__ == '__main__':
    main()
