from matplotlib.pyplot import *
import numpy as np

import tarfile

for i in range(2016, 2017, 1):
    year = str(i)
    for j in range(1, 13, 1):
        if(j<10):
            month = str(0) + str(j)
        else:
            month = str(j)
        for k in range(1, 32, 1):
            if (k < 10):
                day = str(0) + str(k)
            else:
                day = str(k)
            filename = year + month + day + ".tar.gz"
            try:
                if(tarfile.is_tarfile(filename)):
                    print(filename)
                    tar = tarfile.open(filename)
                    tec_len = len(tar.getnames())
                    for i in range(tec_len):
                        tmp = tar.getmember(tar.getnames()[i])
                        if(tmp.name[len(tmp.name)-7:]=="TEC.txt"):
                            tar.extract(tmp.name)
                    tar.close()
            except:
                continue

