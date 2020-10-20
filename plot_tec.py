import os.path

file = '201601010000_TEC.txt'
trash_info = 20
vertical_len = 52

tecarray = []

result = 0

for i in range(2019, 2020, 1):
    year = str(i)
    for j in range(7, 8, 1):
        if(j<10):
            month = str(0) + str(j)
        else:
            month = str(j)
        for k in range(1, 32, 1):
            if (k < 10):
                day = str(0) + str(k)
            else:
                day = str(k)
            for m in range(24):
                if (m < 10):
                    hour = str(0) + str(m)
                else:
                    hour = str(m)
                for n in range(4):
                    time = n*15
                    if(n<10):
                        time = str(0)+str(0)
                    else:
                        time = str(time)
                file = "."+year+month+day+hour+time+"_TEC.txt"
                print(os.path.isfile(file))
                if (os.path.isfile(file)):

                    fp = open(file, 'r')
                    lines = fp.readlines()
                    sum = trash_info
                    while (sum <= len(lines)):
                        print(lines[sum])
                        sum += vertical_len
                        result += 1
print(result)