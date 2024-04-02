# Importing libraries
import os
import psutil  # Require: pip install psutil


# Get current CPU usage using psutil
# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(5))

# Get current CPU usage using the OS module
# Getting loadover 1, 5, and 15 minutes
load1, load5, load15 = psutil.getloadavg()
cpu_usage = (load15/os.cpu_count()) * 100  # CPU usage over the last 15 minutes. Note: os.cpu_count() --> Number of logical CPUs
print("The CPU usage is : ", cpu_usage)
print('------------------------------')


# Get current RAM usage using psutil
mem_usage = psutil.virtual_memory()
# Getting total of virtual_memory ( 1st field)
print('Total RAM memory:', mem_usage[0]/1000000000)
# Getting available of virtual_memory for processes( 2nd field)
print('Available RAM memory:', mem_usage[1]/1000000000)
# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', mem_usage[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', mem_usage[3]/1000000000)
# Getting free of virtual_memory in GB ( 5th field)
print('RAM free (GB):', mem_usage[4]/1000000000)
print('------------------------------')


# Get current swap memory usage using psutil
swap_usage = psutil.swap_memory()
# Getting total of swap ( 1st field)
print('Total swap memory:', swap_usage[0]/1000000000)
# Getting used swap memory( 2nd field)
print('Used swap memory:', swap_usage[1]/1000000000)
# Getting free swap memory ( 3rd field)
print('Free swap memory :', swap_usage[2]/1000000000)
# Getting % usage of virtual_memory ( 4th field)
print('Used swap memory % used:', swap_usage[3])
print('------------------------------')


#Get current RAM usage using the OS module (only works with the Linux system)
# Getting all memory using os.popen() and free system command
total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
# Memory usage
print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))


# Bibliography
# - How to get current CPU and RAM usage in Python? --> https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/
# - Psutil module in Python --> https://www.geeksforgeeks.org/psutil-module-in-python/
# - Monitoring RAM Usage with Python: A Simple Guide to Read and Display RAM Information --> https://medium.com/@himanshu.developer01/monitoring-ram-usage-with-python-a-simple-guide-to-read-and-display-ram-information-b361bde4157d
# - How to Get Current CPU GPU and RAM Usage of a Particular Program in Python --> https://saturncloud.io/blog/how-to-get-current-cpu-gpu-and-ram-usage-of-a-particular-program-in-python/
# - Measuring memory usage in Python: it’s tricky --> https://pythonspeed.com/articles/measuring-memory-python/
