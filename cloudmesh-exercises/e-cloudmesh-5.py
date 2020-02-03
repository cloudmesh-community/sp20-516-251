# fal19-516-251 E.Cloudmesh.Common.5

# develop a program that demonstrates the use of cloudmesh.common.StopWatch

from cloudmesh.common.StopWatch import StopWatch
from time import sleep


if __name__ == "__main__":
    StopWatch.start("abc")
    a=0
    for i in range(1,100000000):
        a=a+1

    StopWatch.stop("abc")
    print(StopWatch.get("abc"))
