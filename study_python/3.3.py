#  タプル：タプルはリストと同様に任意の要素を集めたシーケンスである。タプルはリストと違いイミュータブル（定義したあとで要素を追加、削除、変更を’できない’）である。つまり、タプルは’定数リスト’と言える

# 3.3.1   p.67    <　（）を使ったタプルの作成　>
#まずは空タプルを作る
empty_tuple=()
print(  )


one_marx='groucho', # 最期に’、’をつけてタプルになる
one_marz='groucho'
print(one_marx)
print(one_marz)

marx_tuple=('groucho','chico','harpo')# ()で囲むとタプルであるとわかりやすい。複数の時最期に','はいらない
print(marx_tuple)

print( "タプルを使うと一度に複数の変数を代入できる。" )
a,b,c=marx_tuple
print( "a=%s\nb=%s\nc=%s" % (a,b,c) )

# タプルを使うと一時変数を使わずに一つの文で変数を入れ替えられる
password='swordfish'
icecream='tuttifrutti'
password,icecream=icecream,password
print( "password:%s\nicecream:%s\n" % (password,icecream) )

# 変換関数tuple()を使うと他のモノからタプルを作れる
marx2_list=['groucho','chico','harpo']
print( tuple(marx2_list) )




# 3.3.2  タプルとリストの比較
'''
タプルは、消費スペースが小さい
タプルの要素は誤って書き換える危険がない
タプルは辞書のキーとして使える
名前付きタプルはオブジェクトの単純な代用品として使える
関数の引数はタプルとして渡される
'''












