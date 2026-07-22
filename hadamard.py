import qiskit as qk
from board_control import *
import matplotlib.pyplot as plt
import math
qubit1 = qk.QuantumRegister(1)
simulator = qk.BasicAer.get_backend('qasm_simulator')
bit1 = qk.ClassicalRegister(1)
circuit = qk.QuantumCircuit(qubit1, bit1)
circuit.h(qubit1[0])
circuit.measure(qubit1, bit1)
print(circuit)
i = 0
namelist = ["|0>", "|1>"]
steplist = [0, 0]
while i < 25:
    job = qk.execute(circuit, backend=simulator, shots = 5)
    result = job.result()
    write(13, 1)
    time.sleep(0.1)
    write(13, 0)
    count = result.get_counts(circuit)
    superposition(6)
    if '0' in count:
        x = count['0']
    else:
        x = 0
    if '1' in count:
        y = count['1']
    else:
        y = 0
    time.sleep(1)
    write(13, 1)
    time.sleep(0.01)
    write(13, 0)
    if x>y:
        write(6, 1)
        print("STATE: " + str(i + 1) + ": " + "|1>") 
        steplist[1] += 1
    elif x<y:
        write(6, 0)
        print("STATE: " + str(i + 1) + ": " + "|0>") 
        steplist[0] += 1
    else:
        write(6, math.random.randint(0,1))
    input("")
    i += 1
write(6, 0)
write(13, 1)
time.sleep(1)
write(13, 0)
print("STATE VALUES")
print("0 : " + str(steplist[0]))
print("1 : " + str(steplist[1]))
print("END")
plt.bar(namelist, steplist, color ='blue', width = 1)
plt.xlabel("Quantum States")
plt.ylabel("No. of Measurements")
plt.title("Hadamard Gate Outcome")
plt.show()