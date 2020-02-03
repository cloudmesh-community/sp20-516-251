# fal19-516-251 E.Cloudmesh.Common.1

# develop a program that demonstrates the use of banner, HEADING and VERBOSE

from cloudmesh.common.util import banner
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING

class Example(object):

    def banner_example(self):
        banner("This is for cloudmesh practice")


    def heading_example(self):
        HEADING()
        print("Functions")

    def verbose_example(self):
        m = {"function1":"banner","function2:":"HEADING","function2":"VERBOSE"}
        VERBOSE(m)


if __name__ == '__main__':
    p = Example()
    p.banner_example()
    p.heading_example()
    p.verbose_example()
