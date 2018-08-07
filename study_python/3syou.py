'''
p53 

<3.1：リストとタプル>

pythonには文字列以外に、タプルとリストの二種類のシーケンス（連続）を作ることができる
文字列とは異なり、要素は型がまちまちで良い。
個々の要素はリスト、タプルを含む任意のpythonオブジェクトでよい。だから、いくらでも深く、複雑な構造を作れる。

リストはミュータブルで、要素の挿入と削除を行うことができる
タプルはイミュータブルなので、できない。

'''


# 3.2.1 : [] や list() でのリストの作成

empty=[]
weekdays=[ 'monday','tuesday','wednesday','thursday','friday' ]
another_empty=list()

print( empty )
print( weekdays )
print( another_empty )




# 3.2.2 :  list()による他のデータ型からリストへの変換

# 文字列を一文字毎の文字列リストに変換している
print( list( 'cat' ) )
moziretu='dog'
print( moziretu )
print( list(moziretu) )



print( "-------------------タプル（後述）をリストに変換--------------------" )
a_tuple=( 'ready','fire','aim' )
print( a_tuple )


        # 2.6.9より、split()関数でセパレータを指定して文字列を分割できる
brithday='1/6/1952'
print( brithday.split( '/' ) )
splitme=' a/b//c/d///e '
print( splitme.split('/') )
print( splitme.split('//') )


# 　3.2.3　:　[offset]を使った要素の書き出し
# 文字列と同じで、オフセットを使うとリストからも個々の要素を取り出せる
marxes=[ 'groucho','chico','harpo' ]
print( marxes[1] )


#3.2.4 :  リストのリスト
small_birds=[ 'hummingbird','finch' ]
extinct_birds=[ 'dodo','passenger pigeno','norwegian blue' ]
carol_birds=[ 3,'french hens',2,'turtledoves' ]

all_birds=[ small_birds,extinct_birds,'macaw',carol_birds ]
print( all_birds )
print( all_birds[0][1] )
print(all_birds[1])



# 3.2.5  [offset]による要素の書き換え
marxes[2]='wanda'
print( marxes )
# 文字列はイミュータブルなので文字列内の文字を書き換えることはできないが、リストの要素自体を書き換えることはできる


# 3.2.6 : オフセットの範囲を指定したスライスによるサブシーケンスの取り出し
marxes2=[ 'irohani','hoheto','tirinuruo','hakayo','taresotu' ]
print( marxes2[0:3] )
print( marxes2[::2] )
print( marxes2[::-2] )
print( marxes2[::-1] )


# 3.2.7 : append()による末尾への要素の追加
marxes.append( 'zeppo' ) # リストの末尾に追加される
print( marxes )


# 3.2.8 : extend()または+＝を使ったリストの結合
# extend()を使えば、2つのリストを一つにまとめることができる
others=[ 'gummo','karl' ]
marxes.extend( others )
print( marxes )

others2=[ 'poke','mon' ]
marxes+=others2
print( marxes )
marxes.append( others )
print( marxes )# 確かに、リストは異なる方の要素をもてるね


# 3.2.9 : insert()によるオフセットを指定した要素の追加
marxes.insert( 3,'gummo' )
print( marxes )


# del による指定したオフセットの要素削除
del marxes[-1]
print( marxes )

print("---------------------------------------------")

# 3.2.11 : remove() による値に基づく要素の削除
marxes.remove( 'gummo' )
print( marxes )


# pop()でオフセットを指定して要素を取り出し、削除する方法
marxes.pop(1)
print(marxes.pop(1))
print( marxes )









