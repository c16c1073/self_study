#  p.11
# man というクラスが、m というインスタンス（オブジェクト）を生成。

class Man:                                       # class 変数名():
    def __init__( self, name ):                  # def __init__( self, 引数, ...  )    コンストラクタ
        self.name = name
        print( "initialized!" )

    def hello(self):                              # def メゾッド名( self, 引数, ...   )   メゾッド1
        print( "hello"+self.name+"!" )

    def goodbye(self):
        print( "good-by" + self.name + "!" )


m=Man( "david" )
m.hello()
m.goodbye()

