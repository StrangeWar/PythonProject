#!/usr/bin/env python
import shutil
import psutil
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    print(free)
    return free > 20

def check_cpu_usage():
    usage  = psutil.cpu_percent(2)
    print(usage)
    return usage < 75
if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!")
else:
    print("Everything is OK!")
        
