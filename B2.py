'''
2. cho trước 2 số y, x (y > x). Có 2 cách thay đổi giá trị của x:
	- tăng gấp đôi x
	- bớt x đi 1 đơn vị
Tìm số bước nhỏ nhất để x = y.
'''
import math

def div_func(y,x):

    while y > x:
        y/=2
    return math.ceil(y)

def GT(y,x):
    try:
        if x < 1 or y < 1 or x > y:
            print("values invalid")
        elif x == y:
            print("step = 0")
        else:
            count = 0
            while True:
                value = div_func(y,x)
                sub = x-value
                count+=sub
                x=value*2
                count+=1
                if x > y:
                    x-=1
                    count+=1
                    print("{} number of step = {}".format(x,count))
                    break
    except:
        print("step = NULL")

if __name__ == '__main__':
    GT(5,4)










