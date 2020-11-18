import os.path
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
import pickle
import csv

# trash_info = 45
# vertical_len = 52
# latitude = -117
#
# tecarray = []
# days = [20200819 ,
# 20200817 ,
# 20200817 ,
# 20200810 ,
# 20200809 ,
# 20200706 ,
# 20200630 ,
# 20200625 ,
# 20200624 ,
# 20200624 ,
# 20200623 ,
# 20200619 ,
# 20200608 ,
# 20200604 ,
# 20200522 ,
# 20200520 ,
# 20200519 ,
# 20200517 ,
# 20200517 ,
# 20200516 ,
# 20200516 ,
# 20200515 ,
# 20200515 ,
# 20200515 ,
# 20200515 ,
# 20200515 ,
# 20200515 ,
# 20200515 ,
# 20200510 ,
# 20200411 ,
# 20200411 ,
# 20200404 ,
# 20200401 ,
# 20200331 ,
# 20200326 ,
# 20200322 ,
# 20200321 ,
# 20200318 ,
# 20200318 ,
# 20200318 ,
# 20200318 ,
# 20200307 ,
# 20200215 ,
# 20200125 ,
# 20200119 ,
# 20191212 ,
# 20191130 ,
# 20191015 ,
# 20190910 ,
# 20190822 ,
# 20190726 ,
# 20190718 ,
# 20190712 ,
# 20190712 ,
# 20190711 ,
# 20190707 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190706 ,
# 20190705 ,
# 20190704 ,
# 20190704 ,
# 20190704 ,
# 20190704 ,
# 20190623 ,
# 20190622 ,
# 20190420 ,
# 20190409 ,
# 20190406 ,
# 20190117 ,
# 20190115 ,
# 20190105 ,
# 20190104 ,
# 20181119 ,
# 20181109 ,
# 20180728 ,
# 20180705 ,
# 20180506 ,
# 20180409 ,
# 20180407 ,
# 20180405 ,
# 20180323 ,
# 20180319 ,
# 20180121 ,
# 20180120 ,
# 20180119 ,
# 20180119 ,
# 20171113 ,
# 20170911 ,
# 20170910 ,
# 20170910 ,
# 20170906 ,
# 20170904 ,
# 20170903 ,
# 20170903 ,
# 20170902 ,
# 20170706 ,
# 20170706 ,
# 20170329 ,
# 20161228 ,
# 20161228 ,
# 20161228 ,
# 20161214 ,
# 20161213 ,
# 20161120 ,
# 20161107 ,
# 20161017 ,
# 20161013 ,
# 20160903 ,
# 20160827 ,
# 20160815 ,
# 20160810 ,
# 20160721 ,
# 20160707 ,
# 20160610 ,
# 20160328 ,
# 20160328 ,
# 20160224 ,
# 20160216 ,
# 20160213 ,
# 20160107 ,
# 20151230 ,
# 20151227 ,
# 20151130
# ]
#
# result = 0
# cal = 0
#
# for i in range(2016, 2017, 1):
#     year = str(i)
#     for j in range(1, 13, 1):
#         if(i==2020 and j>1):
#             break
#         if(j<10):
#             month = str(0) + str(j)
#         else:
#             month = str(j)
#         for k in range(1, 32, 1):
#             if (k < 10):
#                 day = str(0) + str(k)
#             else:
#                 day = str(k)
#             for m in range(24):
#                 if (m < 10):
#                     hour = str(0) + str(m)
#                 else:
#                     hour = str(m)
#                 for n in range(4):
#                     time = n*15
#                     cal=cal+1
#                     if(time<10):
#                         time = str(0)+str(0)
#                     else:
#                         time = str(time)
#                     file = year+month+day+hour+time+"_TEC.txt"
#                     if (os.path.isfile(file)):
#                         fp = open(file, 'r')
#                         print(file)
#                         result += 1
#                         lines = fp.readlines()
#                         sum = trash_info
#                         tokens = []
#                         tokens.append(float(lines[sum].split()[34]))
#                         earthquake_check = int(year+month+day)
#                         if earthquake_check in days:
#                             tokens.append(1)
#                         else:
#                             tokens.append(0)
#                         tecarray.append(tokens)
#                         fp.close()
                        # while (sum <= len(lines)):
                        #     tecarray.append(float(lines[sum].split()[34]))
                        #     sum += vertical_len

############ 학습 데이터 생성 부분
tecarray = np.load('C:/Users/학생1/Desktop/research_geonwoo/result/label/tecarray_total_2.npy')
# raw_dir = Path('.')
# tecarray2  = []
# for i in range(len(tecarray)):
#     if(tecarray[i][1]==0):
#         tecarray2.append(tecarray[i])
# labeled_whole_dir = raw_dir.parent.joinpath('labeled', 'whole')
# labeled_whole_dir.mkdir(parents=True, exist_ok=True)
# with open(str(labeled_whole_dir.joinpath('tecdata2').with_suffix('.pkl')), 'wb') as pkl:
#     pickle.dump(tecarray, pkl)
# cutting_point = int(0.75*len(tecarray2))
# labeled_train_dir = raw_dir.parent.joinpath('labeled', 'train')
# labeled_train_dir.mkdir(parents=True, exist_ok=True)
# labeled_test_dir = raw_dir.parent.joinpath('labeled', 'test')
# labeled_test_dir.mkdir(parents=True, exist_ok=True)
# with open(str(labeled_train_dir.joinpath('tecdata2').with_suffix('.pkl')), 'wb') as pkl:
#     pickle.dump(tecarray2[:cutting_point], pkl)
# with open(str(labeled_test_dir.joinpath('tecdata2').with_suffix('.pkl')), 'wb') as pkl:
#     pickle.dump(tecarray2[cutting_point:], pkl)
#학습 데이터 처리 끝

##############################excel 작성 부분
# f = open('tec_output.csv','w',encoding='utf-8', newline="")
# wr = csv.writer(f)
# wr.writerow(["timestamp","value"])
# cal = 0
# for i in range(2016, 2017, 1):
#     year = str(i)+"-"
#     for j in range(1, 13, 1):
#         if(i==2020 and j>1):
#             break
#         if(j<10):
#             month = str(0) + str(j)
#         else:
#             month = str(j)
#         month+= "-"
#         for k in range(1, 32, 1):
#             if (k < 10):
#                 day = str(0) + str(k)
#             else:
#                 day = str(k)
#             day+=" "
#             for m in range(24):
#                 if (m < 10):
#                     hour = str(0) + str(m)
#                 else:
#                     hour = str(m)
#                 hour+=":"
#                 for n in range(4):
#                     time = n*15
#                     if(time<10):
#                         time = str(0)+str(0)
#                     else:
#                         time = str(time)
#                     time+=":"
#                     fin = year+month+day+hour+time+"00"
#                     print(fin)
#                     if(cal<len(tecarray)):
#                         wr.writerow([fin, tecarray[cal][0]])
#                     cal=cal+1
# # for i in range(len(tecarray)):
# #     wr.writerow([time_tecarray[i],tecarray[i][0]])
# f.close()
############## 엑셀 파일 작성 부분 끝
# tecarray = np.array(tecarray)
# np.save('C:/Users/학생1/Desktop/research_geonwoo/result/label/tecarray_total_2',tecarray)
time_tecarray = []
for i in range():
    

#####
fig, ax = plt.subplots()
plt.title("TEC data during 2016/1/1~2016/12/31")
# plt.xlim(0,31)
ax.plot(time_tecarray,tecarray,color = 'blue')
plt.show()