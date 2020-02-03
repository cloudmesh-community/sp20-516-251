# fal19-516-251 E.Cloudmesh.Common.4

# develop a program that demonstrates the use of cloudmesh.common.shell

from cloudmesh.common.Shell import Shell

class example():
    def shell(self):
        result_1 = Shell.execute('pwd')
        print(result_1)
        result_2 = Shell.execute('ls',["-1","-a"])
        print(result_2)


if __name__ == '__main__':
    p = example()
    p.shell()

