# fal19-516-251 E.Cloudmesh.Common.2

# develop a program that demonstrates the use of dotdict

from cloudmesh.common.dotdict import dotdict

class example():

    def dotdict_example(self,dic):
        dic = dotdict(dic)
        if dic.name == "Shihui":
            print("this is quite readable")
        else:
            print("this is not quite readable")

if __name__ == '__main__':
    p = example()
    p.dotdict_example({'name':'Ming'})

