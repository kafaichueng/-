import numpy as np
from scipy import signal
n, m = 0, 0
array = np.random.randint(-128, 127, size=(6, 6))#定义输入矩阵
array
conv_array
con_calculate Result
kernel = np.random.randint(-8, 7, size=(3, 3))#卷积核
result = signal.convolve2d(array, kernel, mode='valid')#卷积
def intTohex8(i):#将输入 array 和 kernel 转为 16 进制的函数
a = 0
s = ''
r = ''
a = (bin(((1 << 8) - 1) & i)[2:]).zfill(8)
for i in range(0, len(a), 4):
s = '0b' + a[i:i+4]
s = int(s, 2)
r += str(hex(s))[2:]
return r
def intTohex16(i):#将 result 矩阵转为 16 进制的函数
a = 0
s = ''
r = ''
a = (bin(((1 << 16) - 1) & i)[2:]).zfill(16)
for i in range(0, len(a), 4):
s = '0b' + a[i:i+4]
s = int(s, 2)
r += str(hex(s))[2:]
return r
print('array_hex =\n')
for i in range(0, 6):
for j in range(0, 6):
print(intTohex8(array[i][j]), end=' ')
n += 1
if n%6 == 0:
print('\n')
print('array = \n', array)
print('kernel_hex =\n')
for i in range(0, 3):
for j in range(0, 3):
print(intTohex8(kernel[i][j]), end=' ')
n += 1
if n%3 == 0:
print('\n')
print('kernel = \n', kernel)
print('result_hex =\n')
for i in range(0, 4):
for j in range(0, 4):
print(intTohex16(result[i][j]), end=' ')
m += 1
if m%4 == 0:
print('\n')
print('result = \n', result)
