'''
2. cho trước 2 số y, x (y > x). Có 2 cách thay đổi giá trị của x:
	- tăng gấp đôi x
	- bớt x đi 1 đơn vị
Tìm số bước nhỏ nhất để x = y.
'''

def Alo(y,x):
    try:
        if x<1 or y<1 or x>y:
            print("values invalid")
        elif x==y:
            print("step = 0")
        else:
            tmp = x
            count = 0
            while tmp!=y:
                tmp*=2
                count+=1
                print(tmp)
                while tmp>y:
                    tmp-=1
                    count+=1
                    print(tmp)
        return print("step = %d" %count)
    except:
        print("step = NULL")

if __name__ == '__main__':
    Alo(16,5)

    #5x2-1-1x2 = 16 st=4
