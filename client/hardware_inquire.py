#!/usr/bin/env python3
# Michiel Merkx Inne Lemstra
'''Find Statistics about the amount of RAM and the specific CPU on the current linux computer using bash commands'''


import subprocess

comGetRAM = ["free", "-m"]
comGetCPU = "lscpu"
pipe = subprocess.PIPE

#calling bash functions
infoCPU = subprocess.run(comGetCPU, stdout= pipe)
infoRAM = subprocess.run(comGetRAM, stdout= pipe)

#conferting to list
infoCPU = str(infoCPU.stdout).split("\\n") #beware this makes a list not a string
infoRAM = str(infoRAM.stdout).split("\\n") #beware this makes a list not a string

#cpuField is a line in the output of lscpu
#Take the first index in the list (should only be 1  model name) and convert to str
cpuName = [cpuField for cpuField in infoCPU if "Model name" in cpuField]
#format and convert
cpuName = str(cpuName[0]).split("  ")[-1]


#RAM availible is the last field in the free -m call. These fields are split with
#spaces that try to emulate \t (meaning there is a lot of them)
#convert 1st idex of list available memory (should be only 1)  to str
ramAvail = str([line.split(" ")[-1] for line in infoRAM if "Mem" in line][0])

#check is empty and raise error if so (for travis)
if not(cpuName) or not(ramAvail):
	raise ValueError('One of the strings is empty, script broke')

print("cpu is {0}\n machine has {1} MB of RAM available\n".format(cpuName,\
							 ramAvail))
