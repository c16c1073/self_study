# 集合
'''
集合は値を放り出してキーだけを残した辞書のようなもの
辞書と同じように個々のキーは一意でなければならない
集合は何かがあるかどうかだけがわかればOK。他のことは知らなくても良い時に使う
キーに何らかの情報を追加したいときに辞書を使う
辞書のキーと同じで、集合の要素に順序はない
'''

# 3.5.1  set()による作成
# set()関数を使うか、波括弧を使う

empty_set=set()
even_numbers={0,2,4,6,8}
odd_numbers={1,3,5,7,9}
print(empty_set,even_numbers, odd_numbers)


# 3.5.2  set()による他のデータ型から集合への変換

# 文字列を集合へ
character_string='letters'
print( set(character_string) )
# eとtは元々複数文字含まれていたので、集合にするとひとつだけになるね

# 次に、リストから集合
list=['dasher','dancer','prancer','mason-dixon']
print( set(list) )

# タプルからリストへ
tuple=('ummagumma','echoes','atom heart mother')
print(tuple)



#3.5.3  in を使った値の有無のテスト
# drinks という辞書をつくる
drinks={ 'martini':{'vodka','vermouth'},
         'black russian':{'vodka','kahlua'},
         'white russian':{'cream','kahlea','vodka'},
         'manhattan':{'rye','vermouth','bitters'},
         'screwdriver':{'orange','juice','vodka'}
         }

# ウォッカを含む辞書の中の集合を検索
for name,contents in drinks.items():
        if 'vodka' in contents:
                print(name)
print()
# # vermonthと cream が入ってないこと
for name, contents in drinks.items():
        if 'vodka'in contents and not('vermonth'in contents or'cream'in contents):
                print(name)


# 3.5.4 組み合わせと計算
# 集合の要素の組み合わせについてチェックしたい時には、、、
# オレンジジュースか





