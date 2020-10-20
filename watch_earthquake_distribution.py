import csv
import matplotlib.pyplot as plt
import numpy as np

latitude = []
longtitude = []
magnitude = []

f = open('earthquake_data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
#지진이 어디서 발생했는지 보여주는 코드
for line in rdr:
    try:
        latitude.append(float(line[1]))
        longtitude.append(float(line[2]))
    except:
        continue
f.close()

latitude = np.array(latitude)
longtitude = np.array(longtitude)
color = np.ones(len(latitude))
color/=5
area = np.pi*4
plt.ylim(23,50)
plt.xlim(-130,-70)
plt.scatter(longtitude,latitude,label = 'samples',s=area,c=color,alpha=0.5)
plt.title("Epicenters")
plt.show()

# #규모별 지진분포 히스토그램
# for line in rdr:
#     try:
#         magnitude.append(float(line[4]))
#     except:
#         continue
# f.close()
#
# X = np.arange(len(magnitude))
# magnitude = np.array(magnitude)
# print(magnitude)
#
# hist = plt.hist(magnitude, bins=10, density=False, cumulative=False, label='A', color = 'r', edgecolor = 'black', linewidth=1)
# plt.title('scatter',pad=10)
# plt.xlabel('Magnitude',labelpad = 10)
# plt.ylabel('Number', labelpad=10)
# #
# # plt.minorticks_on()
# # plt.tick_params(axis='both',which='both',direction='in',pad=8,top=True,right=True)
# plt.show()