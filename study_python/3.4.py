#  p.69   辞書



# 空の辞書
empty_dict={}
print( empty_dict )

bierce={ "day":"A period of twenty-four hours, mostly misspent",
         "positive":"mistaken at the top of one's voice",
         "misfortune":"the kind of fortune that never misses",
         }
print( bierce )



# 3.4.2
print( "dict()を使った変数" )
'''
dict()を使うと2つの値のシーケンスを辞書に変換できる。
シーケンスの先頭要素がキー、第二要素が値
'''
# まずは、2要素リストのリストを使った簡単な例を見る
lol=[ ['a','b'],['c','d'],['e','f'] ]
print(dict(lol))
# に要素のシーケンスを含むものなら何でも使える
print("に要素のタプルのリスト")
lot=[('a','b'),('c','d'),('e','f')]
print( dict( lot ) )
print("に要素のリストのタプル")
tol=( ['a','b'],['c','d'],['e','f'] )
print( dict(tol) )
print("に文字の文字列リスト")
los=['ab','cd','ef']
print( dict(los) )
print("2文字の文字列タプル")
tos=('ab','cd','ef')
print( dict(tos) )



# 3.4.3
print("[key]による要素の追加、変更")
'''
辞書に要素を追加するのは簡単
キーを使って要素を参照し、値を代入すれば良い
辞書にそのキーがすでにある場合には、既存の値が新しい値に置き換えられる
キーがまだない場合には、値ともども辞書に追加される。
リストとは違い、範囲外のインデックス（キー）を指定したために代入中に例外が投げられる心配わない
'''
pythons={ 'chapman':'graham',
          'cleese':'john',
          'idle':'eric',
          'jones':'terry',
          'palin':'michael',
          }
print(pythons)
# メンバーを追加したい、terry gilliam を追加したいが、名前を間違えたところを示している
pythons['gilliam']='gerry'
print(pythons)
# 次のコードはふたとおりの意味でパイソニック（pythonらしいシンプルで読みやすいコードの書き方）な別のプログラマーが書いた修復コードだ
# 'filliam'という同じキーを使って'gerry'という元の値を'terry'に置き換える
pythons['gilliam']='terry'
print(pythons)
# 辞書のキーは一意(重複しないよ)でなければならない。
# 名がterryのメンバーが二人いる。キーを複数回使った場合、最期の値が辞書に残る
some_pythons={'graham':'chapman',
             'john':'cleese',
             'eric':'idle',
             'terry':'gilliam',
             'michael':'palin',
             'terry':'jones',
             }
print(some_pythons)


print("#3.4.4  update()による辞書の結合")
# update()を使うと辞書のキーと価を別の辞書にコピーすることができる
others={ 'marx':'groucho',
         'howard':'moe',
         }
pythons.update(others)
print(pythons)


print("第二の辞書が第一の辞書に含まれているのと同じキーが含まれていたら、第二の辞書の値が残る")
first={'a':'1',
       'b':'2'}
second={'b':'platypus'}
first.update(second)
print(first)


# 3.4.5  delによる指定したキーを持つ要素の削除
# 最期の二人のメンバーの追加を取り消そう
del pythons['marx']
print(pythons)

del pythons['howard']
print(pythons)

# 3.4.6　　clear()による全ての要素の削除
pythons.clear()
print(pythons)
# あるいは、空辞書を辞書名に代入する


# 3.4.7  in を使ったキーの有無のテスト
pythons={'chapman':'graham',
              'cleese':'john',
              'jones':'terry',
              'palon':'michael',
              }
print('chapman'in pythons)
print('gilliam'in pythons)


# 3.4.8  [key] による要素の取得
# 辞書の最も一般的な使い方である。
# 辞書とキーを指定して、対応する値を取り出すのである
print(pythons['cleese'])
# 2つ目のやり方は、辞書専用の関数 get()関数を使う。辞書、キー、オプション値を渡し、キーがあればその値が返される
print( pythons.get('cleese') )
# キーがないときは、指定したオプション値が返される
print( pythons.get('marx','naiyo!') )
print( pythons.get('marx') )


# 3.4.9   keys() による全てのキーの取得
# keys()を使えば、辞書の全てのキーを取得できる
signals={ 'green':'go',
          'yellow':'go faster',
          'red':'smile for the camera'}
print( signals.keys() )
'''
イテレーション可能な構造をイテラブルといいます。
ではイテレーションとは何かと言われれば「繰り返すこと」「次要素にアクセスすること」と言えるでしょうか。
簡単に言うのであればfor文で回せるオブジェクト。厳密にいうのであればイテレータにできるオブジェクトかな。
'''
# dict_keys([])オブジェクトをリストに変換するためには、list()を呼びださなければならない
print(  list( signals.keys() )  )




# values() による,辞書の全ての値の取得
print(  signals.values()  )
# リストに変換するにはlist()を使う
print(  list( signals.values() )  )



# 3.4.11  items() による全てのキー/値ペアの取得      個々のキー/値ペアはタプル形式で返される
print(  list( signals.items() )  )


#3.4.12　 '=' による代入と copy() によるコピー
# リストの場合と同様に、辞書に変更を加えると、その辞書を参照している全ての名前に影響が及ぶ
print("---------------------------------------------------------")
print( signals )
save_signals=signals
signals['blue']='confuse everyone'
print(signals)
original_signals=signals.copy()
signals['black']='makkura'
print(signals)
print(original_signals)


