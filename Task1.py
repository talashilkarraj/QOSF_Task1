import numpy as np
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
#from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit import assemble
import numpy as np
from matplotlib import pyplot as plt
from qiskit import Aer
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_state_city
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere, plot_state_city

# ckt = QuantumCircuit(3)
# def create_entangledstate_function(ckt,n):
#     ckt.h(0)
#     for i in range(1,n):
#       ckt.cx(0,i)
#     pass

# create_entangledstate_function(ckt,3)

# backend = Aer.get_backend('statevector_simulator')
# # Create a Quantum Program for execution
# job = backend.run(ckt)
# result = job.result()

# outputstate = result.get_statevector()
# print(outputstate)

# state = DensityMatrix.from_instruction(ckt)
# plot_state_city(state, color=['midnightblue', 'midnightblue'],
#      title="New State City")
# state2 = Statevector.from_instruction(ckt)
# x = plot_state_qsphere(state2)
# # plt.show()

"""
Function: Decimal to Binary Conversion
Parameters: Number to be converted
Returns: Decimal to binary converted String 
"""
def decimal_To_binary(num):
  binary = str(bin(num))
  return binary[2:len(binary)]


"""
Function: Largest_Number
Parameters: List
Returns: Tuple wtih 2 values - largest number in the list, length of binary converted 
         largest number
"""
def largest_number(list):
  big = list[0]
  for i in range(0,len(list)-1):
    if big>list[i+1]:
      pass
    else: 
      big=list[i+1]
  return big,len(decimal_To_binary(big))


"""
Function: Binary converted list 
Parameters: List
Returns: a list with every number of the list converted into its equivalent binary 
         with bitlength same for all numbers & equal to the bitlength of the largest number
"""
def binary_converted_list(list):
  big, max_bit_length = largest_number(list)
  list_of_binaries=[]
  for i in list:
    k = decimal_To_binary(i)
    if (len(k) == max_bit_length):
      pass
    else: 
      k = "0"*(max_bit_length-len(k))+k
    list_of_binaries.append(k)
  return(list_of_binaries)


"""
Debug code lines
"""
# print(decimal_To_binary(5))
# print(binary_converted_list([1,5,2,17]))
# print(type(largest_number([1,8,2,0,5,7])))


def binary_alternate_digits_list(list):
  list_of_alternate_digits=[]
  indices=[]
  print(list)
  counter = 0
  for i in list:
    
    for j in range(0,len(i)-2):
      if int(i[j]) != int(i[j+2]):
        break
    for j in range(0,len(i)-1):
      if int(i[j]) == int(i[j+1]):
          break
    else:
      list_of_alternate_digits.append(i)
      indices.append((counter))
    counter+=1
  
  indices = binary_converted_list(indices)
  return indices, list_of_alternate_digits

# print(binary_alternate_digits_list(['0101','1110','0111','1011']))
print(binary_alternate_digits_list(binary_converted_list([1,5,7,10])))
# k = decimal_To_binary(3)
# print(k)

ckt = QuantumCircuit(2)
def create_entangledstate_function(ckt,n):
    ckt.x(1)
    ckt.cx(1,0)
    ckt.h(1)

create_entangledstate_function(ckt,2)

backend = Aer.get_backend('statevector_simulator')
# Create a Quantum Program for execution
job = backend.run(ckt)
result = job.result()

outputstate = result.get_statevector()
print(outputstate)

state2 = Statevector.from_instruction(ckt)
x = plot_state_qsphere(state2)
plt.show()