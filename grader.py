# grader.py
"""
Grader module for Qiskit Fall Fest 2025 Day 2 exercises.

This module provides functions for evaluating Grover's algorithm implementations.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np


def ex_1(qc: QuantumCircuit) -> bool:
    """
    Exercise 1: Check if initial quantum circuit is correct.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to evaluate.
        
    Returns:
        bool: True if correct, False otherwise.
    """
    circuit_correct = QuantumCircuit(2, 2)

    if qc == circuit_correct:
        print("正解です！")
        return True
    else:
        print("不正解です...")
        return False


def ex_2(qc: QuantumCircuit) -> bool:
    """
    Exercise 2: Check if Hadamard gates are correctly applied.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to evaluate.
        
    Returns:
        bool: True if correct, False otherwise.
    """
    circuit_correct = QuantumCircuit(2, 2)
    circuit_correct.h(0)
    circuit_correct.h(1)

    if qc == circuit_correct:
        print("正解です！")
        return True
    else:
        print("不正解です...")
        return False


def ex_3(qc: QuantumCircuit) -> bool:
    """
    Exercise 3: Check if Oracle (CZ gate) is correctly applied.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to evaluate.
        
    Returns:
        bool: True if correct, False otherwise.
    """
    psi = Statevector.from_instruction(qc)
    amplitudes = psi.data  # array([a0, a1, a2, a3])

    circuit_correct = QuantumCircuit(2, 2)
    circuit_correct.h(0)
    circuit_correct.h(1)
    circuit_correct.cz(0, 1)
    psi_correct = Statevector.from_instruction(circuit_correct)
    amplitudes_correct = psi_correct.data

    is_correct = np.allclose(amplitudes, amplitudes_correct)
    
    if is_correct:
        print("正解です！")
        return True
    else:
        print("不正解です...")
        return False


def ex_4(qc: QuantumCircuit) -> bool:
    """
    Exercise 4: Check if diffusion operator is correctly applied.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to evaluate.
        
    Returns:
        bool: True if correct, False otherwise.
    """
    psi = Statevector.from_instruction(qc)
    amplitudes = psi.data  # array([a0, a1, a2, a3])
    
    circuit_correct = QuantumCircuit(2, 2)
    circuit_correct.h(0)
    circuit_correct.h(1)
    circuit_correct.cz(0, 1)
    circuit_correct.h(0)
    circuit_correct.h(1)
    circuit_correct.x(0)
    circuit_correct.x(1)
    circuit_correct.h(1)
    circuit_correct.cx(0, 1)
    circuit_correct.h(1)
    circuit_correct.x(0)
    circuit_correct.x(1)
    circuit_correct.h(0)
    circuit_correct.h(1)
    psi_correct = Statevector.from_instruction(circuit_correct)
    amplitudes_correct = psi_correct.data

    is_correct = np.allclose(amplitudes, amplitudes_correct)
    
    if is_correct:
        print("正解です！")
        return True
    else:
        print("不正解です...")
        return False


def ex_5(qc: QuantumCircuit) -> bool:
    """
    Exercise 5: Check if complete Grover's algorithm with measurement is correct.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to evaluate.
        
    Returns:
        bool: True if correct, False otherwise.
    """
    circuit_correct = QuantumCircuit(2, 2)
    circuit_correct.h(0)
    circuit_correct.h(1)
    circuit_correct.h(1)
    circuit_correct.cx(0, 1)
    circuit_correct.h(1)
    circuit_correct.id(0)
    circuit_correct.id(0)
    circuit_correct.h(0)
    circuit_correct.h(1)   
    circuit_correct.x(0)
    circuit_correct.x(1)
    circuit_correct.h(1)
    circuit_correct.cx(0, 1)
    circuit_correct.id(0)
    circuit_correct.h(1)
    circuit_correct.x(0)
    circuit_correct.x(1)
    circuit_correct.h(0)
    circuit_correct.h(1)
    circuit_correct.measure(0, 0)
    circuit_correct.measure(1, 1)

    if qc == circuit_correct:
        print("正解です！")
        return True
    else:
        print("不正解です...")
        return False


__all__ = ['ex_1', 'ex_2', 'ex_3', 'ex_4', 'ex_5']


