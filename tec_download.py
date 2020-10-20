from urllib.request import urlretrieve
import os

sum = 0

for i in range(2016, 2017, 1):
    year = str(i)
    for j in range(4, 13, 1):
        if(j<10):
            month = str(0) + str(j)
        else:
            month = str(j)
        for k in range(1, 32, 1):
            if (k < 10):
                day = str(0) + str(k)
            else:
                day = str(k)
            url = "https://www.ngdc.noaa.gov/stp/iono/ustec/products/" + year + "/" + month + "/" + year + month + day + str("_ustec.tar.gz")
            downpos = "./tecdata/" + year + month + day + ".tar.gz"
            try:
                if(os.path.isfile(downpos)==False):
                    print(url)
                    urlretrieve(url, downpos)
            except:
                print("fail to download")
            else:
                sum+=1
                print("downloaded")
                print(str(sum/1707*100) + "%")
