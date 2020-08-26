import sys
import matplotlib.pyplot as plt
import numpy as np

thermal_threshold = 90
hostname = sys.argv[1]
num_gpu = int(sys.argv[2])
num_tokens = num_gpu * 3

temp_filename = "log/" + hostname + '_temp.txt'

# print(temp_filename)
# print(num_gpu)
# print(num_tokens)

file1 = open(temp_filename, 'r') 
Lines = file1.readlines()

list_temp = []
list_step = []
step = 0

for line in Lines:
	str_temp = line.split(' ')[-1 * num_tokens::3]
	list_temp.append([int(t) for t in str_temp])
	list_step.append(step)
	step += 1

print(list_temp)
print(list_step)

t = np.asarray(list_step)
temperature = np.transpose(np.asarray(list_temp))

fig, (ax0) = plt.subplots(1, 1)

ax0.set_xlim((t[0], t[-1]))
ax0.set_ylim((0, max(thermal_threshold * 1.1, np.amax(np.amax(temperature)) * 1.25)))
ax0.set_title('temperature')
ax0.set_xlabel('Time (sec)')
ax0.set_ylabel('Degree (celsius)')		
for i in range(num_gpu):
	ax0.plot(t, temperature[i], 'b')

if thermal_threshold > 0:
	ax0.plot(t, thermal_threshold * np.ones_like(t), 'r')

plt.show()
