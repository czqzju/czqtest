import time

def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper

def deco03(func):
    def wrapper(*args, **kwargs):
        print("this is deco03")
        func(*args, **kwargs)

        print("deco03 end here")
    return wrapper

@deco01
@deco02
@deco03
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))



if __name__ == '__main__':
    f = func
    f(3,4)
    #func()