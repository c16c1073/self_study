






























# 3.2.13  p.62  
print("index()で要素の値からその要素のオフセット(何番目か)を知る")
marxes=[ 'groucho','chico','harpo','zeppo' ]
print( marxes.index('chico') )

# 3.2.14
print("in を使った値の有無のテスト")
print( 'groucho'in marxes )
print( 'asd'in marxes )

print( "リストの中に同じ値が複数あったら、true を返す" )
A=[ 'asd','dsa','qwe','asd' ]
print( 'asd'in A )

# 3.2.15
print( "count()を使った値の個数の計算" )
print( A.count('asd') )
print( A.count('qwe') )
print( A.count('zxc') )

#3.2.16
print("join()による文字列への変換")
print("join()は文字列メゾッドでありリストメゾッドではないのから、marxes.join(',')じゃないのか？\njoin()の引数は文字列か文字列のイテラブルシーケンス（リスト含）で、出力は文字列である。\njoin()がただのリストメゾッドなら、タプルや文字列などの他のイテラブル型では使えない\njoin()はsplit()の逆　と覚える")
friends=[ 'harry','hermione','ron' ]
separator='*'
joined=separator.join(friends)
print(joined)

separated=joined.split(separator)
print(separated)

# 3.2.17
print("sort による要素の並びかえ")
print("リスト関数のsort()は’その場で’リスト自体をソートする\n汎用関数のsorted()は、ソートされたリストのコピーを返す。")
sorted_marxes=sorted(marxes)
print(sorted_marxes)
print(marxes)
marxes.sort()
print(marxes)
# もちろん全ての要素が同じ型のの時sort()は正しく動作する。しかし、型が混ざっていても良い場合もある
numbers=[2,1,4.0,3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)


# 3.2.18 
print(" len()による長さの取得 ")
# len()はリスト内の要素数を返す
print( len(marxes) )



# 3.2.19 
print("'='による代入とcopy()によるコピー")
a=[1,2,3]
b=a
print( "a= %s\nb=%s " % (a,b)  )
a[0]='surprise'
print( "a=%s\nb=%s" % (a,b) )

print( "リストの値を独立の新しいリストにコピーすることができる" )
c=a.copy()
d=list(a)
e=a[:]
print( "c=%s\nd=%s,\ne=%s" % (c,d,e) )
a[0]="asdf"
print("a=%s" % a)













