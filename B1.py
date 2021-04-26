'''
1. cho 1 dãy số 123456789
chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100
yêu cầu:
- không dùng package itertools
- không dùng 9 vòng for
'''

def Div(a,num):
    tmp=num
    dv = 100000000
    while tmp!=0:
        a.append(int(tmp//dv))
        tmp = tmp%dv
        dv/=10

def combine(a,b):
    return a*10+b

def cacul(a):
    pass

if __name__ == '__main__':
    #a = []
    #Div(a,123456789)
    print(123+45-67+8-9)
