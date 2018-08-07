import random

size=10

def randlist(size):
    list=[]
    for i in range(size):
            list.append( random.randint(0,500) )
    return list
randlist(size)

a=5
def randlist2(a):
    list2=[]
    for i in range(a):
            list2.append( random.randint(10,100) )
    return print(list2)
randlist2(a)


n=15
def randlist3( n,low=4500,high=5000 ):
    list2=[]
    for i in range(n):
            list2.append( random.randint( low,high ) )
    return print(list2)
randlist3(n)
#n=20

n2=10
def inner_list(n2):
    return [ random.randint(0,100) for i in range(n2) ]
#b=10
print(inner_list(n2))


def inner_list2(n=3,l=33,h=50):
    return [ random.randint(l,h) for i in range(n) ]
print( inner_list2() )




def qsort(list):
    if list==[]:
            return list
    else:
            def partition(x,list):
                a,b=[],[]
                for i in list:
                        if i<x:
                                a.append(i)
                        else:
                                b.append(i)
                return a,b
    xs.ys=partition( list[0],list[1:] )
    return qsort(xs)+[ list[0] ]+qsort(ys)
qsort(list)














