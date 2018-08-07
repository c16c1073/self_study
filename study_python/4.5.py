# p.98, 4.5: for による反復処理

# 次のように、シーケンスをループで処理するのはpythonコードとして決して間違ってない
rabbits=[ 'flopsy','mopsy','cottontail','peter' ] 
current=0
while current < len(rabbits):
        print( rabbits[current] )
        current+=1

print("----------------------------------------")

# しかし、python らしいコードは、、、
for rabbit in rabbits:
        print( rabbit )


print("-------------------------")


word='cat'
for s in word:
        print(s)

print("------------辞書をforで処理--------------" )
accusation={ 'room','ballroom','weapon','lead pipe','person','col mustard' }
for a in accusation:
        print( a )
















