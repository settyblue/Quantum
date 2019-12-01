# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:36:38 2019

@author: rakshith kunchum
Simple program to demonstrate how to read the internal state of a wave function.

"""
import cirq
import numpy as np

def main():
    circuit = cirq.Circuit()
    qubit = cirq.LineQubit.range(2)
    circuit.append(cirq.H(qubit[0]))
    circuit.append([cirq.H(qubit[1]), cirq.Y(qubit[1])])
    # Adding a measuring device will collapse the wave function.
    # This will not allow us to observe the state.
    # circuit.append(cirq.measure(qubit[0], key= 'q0'))
    
    # So, in order to observe the state of the wave function, we
    # will need simulate without a measuring device.
    
    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    
    print("Circuit:\n", circuit)
    print(np.around(result.final_state, 3))
    

if __name__ == '__main__':
    main()