

import Hopfild

#Не исправлено работа сразу с несколькими картинками
#Емкость сети-сколько образцов может распознать при
#данном количестве нейронов
# нейроны -длина поступаемого вектора(У НАС ФОТКА 100*100 длина вектора 10000=N
#образцы-наши файлы с фотографиями(3 фотки) =M
# M=N/log(2)N- по Хайкину. В других источниках Ln N
#  нашем случае M=10000/log(2)10000=10000ln(2)/ln(10000)=752
#Может запомнить 752 фотки


file = "hop\\3.png"
file1="hop\\len.png"

file2="hop\\men.png"

file3="hop\\merl.png"
fileEr = "hop\\4.png"
file1Er="hop\\lenEr.png"
file3Er="hop\\merl.Er.png"
train_files=[file, file1,file3]
# y = np.array([[-1, -1]])
# y1 = np.array([[-1, 1]])
# y2 = np.array([[1, -1]])
# yi=[y, y1, y2]
# c=Cosco.Cosco(train_files,yi)
#
# def n(x):
#     k=0
#     for i in yi:
#         if((i==x).all()):
#             print(k)
#             return k
#         else:
#             k=k+1
#     return k
# g=n(c.GetNumber(file3Er))
#
# print(train_files[g])

h=Hopfild.Hop(train_files)
h.classify(file3Er)

# x=np.array([[1,2,3,4,5]])
# print(len(train_files))
# y=np.array([[1,2,3,4,5]])
# print(np.dot(x.T,x ))
# print(np.dot(x,x.T))
#z=np.sum(x,y)
#print(z)
#
# r=0
# for i in range(0,len(x)):
#     r=r+x[i]
# print(r)


# one=np.array([[170,1,1,-1,1,1,1],
#      [400,1,1,-1,1,180,1]])
# x=np.zeros((2,7))
# print(x)
# x[one > 145] = 1
# print(x)
# x[x == 0] = -1
# print(x)
# print(one>145)