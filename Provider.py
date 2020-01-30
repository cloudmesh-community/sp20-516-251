import os

class Provider:

    def list_image (self):
        os.system("multipass find")

    def list_instance(self):
        os.system("multipass list")

    def launch_instance(self,name):
        os.system(f"multipass launch --name {name}")

    def start_instance (self,name):
        os.system(f"multipass start {name}")

    def stop_instance(self,name):
        os.system(f"multipass stop {name}")

    def delete_instance(self,name):
        os.system(f"multipass delete {name}")

    def purge(self):
        os.system("multipass purge")

    def run_command(self,instance,command):
        os.system(f"multipass exec {instance} -- {command}")



if __name__ == '__main__':
    instance_name = "testinstance1"
    p = Provider()
    p.list_image()
    p.launch_instance(instance_name)
    p.list_instance()
    p.start_instance(instance_name)
    # p.run_command(instance_name,"lsb_release -a")
    p.stop_instance(instance_name)
    p.delete_instance(instance_name)
    p.purge()
