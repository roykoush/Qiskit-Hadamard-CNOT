import qiskit as qk
import matplotlib.pyplot as plt
from board_control import *
qubit1 = qk.QuantumRegister(2)
simulator = qk.BasicAer.get_backend('qasm_simulator')
bit1 = qk.ClassicalRegister(2)
circuit = qk.QuantumCircuit(qubit1, bit1)
circuit.h(qubit1[0])
circuit.h(qubit1[1])
circuit.measure(qubit1, bit1)
circuit.cx(qubit1[0], qubit1[1])
print(circuit)
i = 0
namelist = ['|00>', '|01>', '|10>', '|11>']
steplist = [0, 0, 0, 0]
while i < 50:
    valuelist = []
    write(13, 1)
    time.sleep(0.1)
    write(13, 0)
    job = qk.execute(circuit, backend=simulator, shots = 500)
    result = job.result()
    count = result.get_counts(circuit)
    write(5, 0)
    write(9, 0)
    superposition(11)
    superposition(10)   
    time.sleep(1)
    if '00' in count:
        a = count['00']
    else:
        a = 0
    valuelist.append(a)
    if '01' in count:
        b = count['01']
    else:
        b = 0
    valuelist.append(b)
    if '10' in count:
        c = count['10']
    else:
        c = 0
    valuelist.append(c)
    if '11' in count:
        d = count['11']
    else:
        d = 0
    valuelist.append(d)
    value = max(a,b,c,d)
    for x in valuelist:
        if x == value:
            break
        else:
            pass
    name = str(namelist[valuelist.index(value)])
    print("STEP " + str(i+1) + ": " + name)
    write(13, 1)
    time.sleep(0.01)
    write(13, 0)
    if name == "|00>":
        write(10, 0)
        write(11, 0)
        time.sleep(.1)
        write(13, 1)
        time.sleep(0.01)
        write(13, 0) 
        write(5, 0)
        write(9, 0)
        steplist[0] += 1
    elif name  == "|01>":
        write(10, 0)
        write(11, 1)
        time.sleep(.1)
        write(13, 1)
        time.sleep(0.01)
        write(13, 0)
        write(5, 1)
        write(9, 1)
        steplist[1] += 1
    elif name == "|10>":
        write(10, 1)
        write(11, 0)
        time.sleep(.1)
        write(13, 1)
        time.sleep(0.01)
        write(13, 0)
        write(5, 1)
        write(9, 0)
        steplist[2] += 1
    elif name == "|11>":
        write(10, 1)
        write(11, 1)
        time.sleep(.1)
        write(13, 1)
        time.sleep(0.01)
        write(13, 0)
        write(5, 0) 
        write(9, 1)
        steplist[3] += 1
    time.sleep(1)   
    i += 1
write(10, 0)
write(11, 0)
write(5, 0)
write(9, 0)
write(13, 1)
time.sleep(1)
write(13, 0)
j = 0
print("STATE VALUES")
while j < len(steplist):
    print(namelist[j] + ": " + str(steplist[j]))
    j +=1
plt.bar(namelist, steplist, color ='blue', width = 1)
plt.xlabel("Quantum States")
plt.ylabel("Number of Measurements")
plt.title("CNOT Gate Outcome")
plt.show()
print("END")    