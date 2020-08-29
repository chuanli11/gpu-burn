import sys
import matplotlib.pyplot as plt
import numpy as np

hostname = sys.argv[1]
num_gpu = int(sys.argv[2])
gpu_thermal_threshold = 90
cpu_thermal_threshold = 100
gpu_temp_filename = "log/" + hostname + '_gpu_temp.txt'
cpu_temp_filename = "log/" + hostname + '_cpu_temp.txt'

num_tokens = num_gpu * 3

def get_cpu_temp(path):
	file1 = open(path, 'r') 
	Lines = file1.readlines()

	list_temp = []
	list_step = []
	step = 0

	for line in Lines:
		if len(line) > 10:
			list_temp.append([float(t) for t in line.split(' ')])
			list_step.append(step)
			step += 1

	num_cpu = len(list_temp[0])

	t = np.asarray(list_step)
	temperature = np.transpose(np.asarray(list_temp))

	return t, temperature, num_cpu


def get_gpu_temp(path):
	file1 = open(path, 'r') 

	Lines = file1.read().splitlines()

	list_temp = []
	list_step = []
	step = 0

	for line in Lines:
		if len(line) > 10:
			str_temp = line.split(' ')[-1 * num_tokens::3]
			list_temp.append([int(t) for t in str_temp])
			list_step.append(step)
			step += 1

	t = np.asarray(list_step)
	temperature = np.transpose(np.asarray(list_temp))

	return t, temperature

# Get temperature
t_gpu, temperature_gpu = get_gpu_temp(gpu_temp_filename)
# t_cpu, temperature_cpu, num_cpu = get_cpu_temp(cpu_temp_filename)

fig, (ax0, ax1) = plt.subplots(2, 1)

ax0.set_xlim((t_gpu[0], t_gpu[-1]))
ax0.set_ylim((0, max(gpu_thermal_threshold * 1.1, np.amax(np.amax(temperature_gpu)) * 1.25)))
ax0.set_title('GPU temperature')
ax0.set_xlabel('Progress (step)')
ax0.set_ylabel('Degree (celsius)')		
for i in range(num_gpu):
	ax0.plot(t_gpu, temperature_gpu[i], 'b')

if gpu_thermal_threshold > 0:
	ax0.plot(t_gpu, gpu_thermal_threshold * np.ones_like(t_gpu), 'r')


# ax1.set_xlim((t_cpu[0], t_cpu[-1]))
# ax1.set_ylim((0, max(cpu_thermal_threshold * 1.1, np.amax(np.amax(temperature_cpu)) * 1.25)))
# ax1.set_title('CPU temperature')
# ax1.set_xlabel('Progress (seconds)')
# ax1.set_ylabel('Degree (celsius)')		
# for i in range(num_cpu):
# 	ax1.plot(t_cpu, temperature_cpu[i], 'b')

# if cpu_thermal_threshold > 0:
# 	ax1.plot(t_cpu, cpu_thermal_threshold * np.ones_like(t_cpu), 'r')

plt.show()
