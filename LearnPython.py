import os
import platform
#pip install psutil
from psutil import virtual_memory
from psutil import disk_usage
import pprint

class Provider:
    def list(self):
        print("list")

    def shell(self):
        # print("shell")
        os.system("multipass shell")

    def run(self,command):
        print(f"run{command}")
        #os.system(f"multipass exec {command}")

    def mycomputer(self):
        my_os = platform.platform()

        mem = virtual_memory()
        my_mem = mem.total/1024/1024/1024

        total_disk = disk_usage("/").total
        my_disk = total_disk/1024/1024/1024

        dict = {}
        dict["memory"] = my_mem
        dict["os"] = my_os
        dict["disk"] = my_disk
        pprint.pprint(dict)

if __name__ =="__main__":
    p=Provider()
    p.mycomputer()





