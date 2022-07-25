"""
import psutil
data=psutil.cpu_times()
print(data)
# ans : scputimes(user=53139.40624999999, system=40205.42187499994, idle=478262.40625, interrupt=11623.203125, dpc=1974.84375)

"""

"""
import psutil
percentage=psutil.cpu_percent(interval=1)
print(percentage)
# ans :3.1

"""



"""
import psutil  
import platform  
  
# getting the username  
username = platform.uname()  
# print(username) # uname_result(system='Windows', node='RNT-PUN-1185', release='10', version='10.0.19043', machine='AMD64')

print(f"System: {username.system}")  
print(f"Node Name: {username.node}")  
print(f"Release: {username.release}")  
print(f"Version: {username.version}")  
print(f"Machine: {username.machine}")  
print(f"Processor: {username.processor}")  
print("Physical cores:", psutil.cpu_count(logical = False))  
print("Total cores:", psutil.cpu_count(logical = True))  


# CPU frequencies  
cpu_freq = psutil.cpu_freq()  
print(f"Max Frequency: {cpu_freq.max : .2f}Mhz")  
print(f"Min Frequency: {cpu_freq.min : .2f}Mhz")  
print(f"Current Frequency: {cpu_freq.current : .2f}Mhz")  

"""


# ans :
# System: Windows
# Node Name: RNT-PUN-1185
# Release: 10
# Version: 10.0.19043
# Machine: AMD64
# Processor: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
# Physical cores: 2
# Total cores: 4
# PS C:\Users\Kishor Kore\Desktop\psutil> python psutil1.py
# System: Windows
# Node Name: RNT-PUN-1185
# Release: 10
# Version: 10.0.19043
# Machine: AMD64
# Processor: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
# Physical cores: 2
# Total cores: 4
# Max Frequency:  2995.00Mhz
# Min Frequency:  0.00Mhz
# Current Frequency:  2995.00Mhz
 
"""

import psutil  
  
# defining the function  
def getSize(bytes, suffix = "B"):  
    
    # Scaling bytes to its proper format- KB, MB, GB, TB and PB  
      
    the_factor = 1024  
    for the_unit in ["", "K", "M", "G", "T", "P"]:  
        if bytes < the_factor:  
            return f"{bytes:.2f}{the_unit}{suffix}"  
        bytes /= the_factor  
  
print("Virtual memory")  
sv_mem = psutil.virtual_memory()  
print(f"Total: {getSize(sv_mem.total)}")  
print(f"Available: {getSize(sv_mem.available)}")  
print(f"Used: {getSize(sv_mem.used)}")  
print(f"Percentage: {sv_mem.percent} %")  
print("SWAP memory")  

# getting the swap memory details (if exists)  
swap_mem = psutil.swap_memory()  
print(f"Total: {getSize(swap_mem.total)}")  
print(f"Free: {getSize(swap_mem.free)}")  
print(f"Used: {getSize(swap_mem.used)}")  
print(f"Percentage: {swap_mem.percent} %")  

#  ans Virtual memory
# Total: 7.71GB
# Available: 1.99GB
# Used: 5.72GB
# Percentage: 74.2 %
# SWAP memory
# Total: 4.00GB
# Free: 1.80GB
# Used: 2.20GB
# Percentage: 55.0 %

"""

"""
import psutil  
  
VIRTUAL_MEMORY_THRESHOLD = 100 * 1024 * 1024  # 100MB  
SWAP_MEMORY_THRESHOLD = 45  
if  psutil.virtual_memory().available <= VIRTUAL_MEMORY_THRESHOLD:  
    print("Low Virtual Memory warning")  
if psutil.swap_memory().percent >= SWAP_MEMORY_THRESHOLD:  
    print("Low Swap Memory warning")  

"""


"""
# Importing the module before utilization

import psutil
mem = psutil.virtual_memory()
print("------------",mem)

# Returning a sorted list of currently running processes
print(psutil.pids())
 
# Returns an iterator which prevents the race condition for process stats
print(psutil.process_iter())
 
# Used to check whether a certain process exists in the current process list
print(psutil.pid_exists(0))
 
# An example to terminate and wait for the children
def on_terminate(proc):
    print("process {} terminated with exit code {}".format(proc, proc.returncode))
 
procs = psutil.Process().children()
for p in procs:
    p.terminate()
gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
for p in alive:
    p.kill()
"""
"""
import psutil
from psutil._common import BatteryTime

batarydata=psutil.sensors_battery()
print(psutil.cpu_percent(1))
print(batarydata)


if batarydata.power_plugged:
    print("power is connected")
else:
    print("power is not connectesd")

"""



"""
from email import message
from importlib.resources import path
from sre_constants import RANGE
import psutil,datetime,openpyxl,time,schedule

pid=int(input("enter the process id :"))

def warning():
    cpuusage=psutil.cpu_percent(interval=1)

    if cpuusage>50:
        print("cpu usage above 50 %")

    memsage=psutil.virtual_memory().percent

    if memsage>50:
        print("memory utilises above 50 % ",memsage)


def monitor():
    time=datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    
    p=psutil.Process(pid)
    cpu=p.cpu_percent(interval=1)/psutil.cpu_count()
    memory_mb=p.memory_full_info().rss/(1024*1024)
    memory=p.memory_percent()
    
    path=r"C:\Users\Kishor Kore\Desktop\psutil\task_manager.xlsx"
    # path=r".\\task_manager.xlsx"
    file=openpyxl.load_workbook(path)
    sheet=file.active

    sheet.cell(column=1,row=sheet.max_row+1,value=time)
    sheet.cell(column=2,row=sheet.max_row,value=pid)
    sheet.cell(column=3,row=sheet.max_row,value=cpu)
    sheet.cell(column=4,row=sheet.max_row,value=memory_mb)
    sheet.cell(column=5,row=sheet.max_row,value=memory)

    file.save(path)

schedule.every(1).second.do(warning)
schedule.every(5).seconds.do(monitor)

while True:
    schedule.run_pending()
    time.sleep(1)

""" 


