'''
1. cho 1 dãy số 123456789
chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100
yêu cầu:
- không dùng package itertools
- không dùng 9 vòng for
'''

'''
    1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
    1 + 23 - 4 + 56 + 7 + 8 + 9 = 100
    1 + 23 - 4 + 5 + 6 + 78 - 9 = 100
    12 + 3 - 4 + 5 + 67 + 8 + 9 = 100
    .......
'''
ops=['','+','-']

def sum_100(s, i):
    if i < 10:
        for o in ops:
            sum_100(s + o + str(i), i+1)
    else:
        if eval(s) == 100:
            print(s + ' = 100')

sum_100('1',2)