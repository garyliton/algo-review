from time import  sleep

def foo():
    print("yo")

def job_scheduler(func, n):
    sleep(n/1000)
    func()

job_scheduler(foo, 5000)