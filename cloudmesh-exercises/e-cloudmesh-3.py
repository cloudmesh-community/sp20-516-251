# fal19-516-251 E.Cloudmesh.Common.3

# develop a program that demonstrates the use of FlatDict

from cloudmesh.common.FlatDict import FlatDict

class example():

    def flatdict(self):
        d= {
            'name':'shihui',
            'school':'Indiana University',
            'additional':{'class':'cloud computing',
                          'semester':'second'

            }

        }
        flat = FlatDict(d,sep=".")
        print(flat)

if __name__ == '__main__':
    p = example()
    p.flatdict()

