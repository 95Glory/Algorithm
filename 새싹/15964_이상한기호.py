a,b= map(int, input().split())

qw = 0

def result(x,y):
    qw = (x+y)*(x-y)
    return qw

print(result(a,b))