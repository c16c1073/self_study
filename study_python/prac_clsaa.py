class Spam:
    val=100
    def ham(self):
        self.egg( 'call method' )

    def egg(self,msg): # クラス名の先頭は大文字
        print( "{0}".format(msg) )
        print( "{0}".format(self.val) )


spam=Spam()
spam.ham()

"""
a=10
b=5
class Calc:
    def prin(self,a,b):
        a=50
        print( a )
calc=Calc()
calc.prin(2,2)
"""

class Spam2:
    def __init__(self,ham,egg):
        self.ham=ham
        self.egg=egg

    def output(self):
        sum=self.ham+self.egg
        print( "{0}".format(sum) )

spam=Spam2(5,10)
spam.output()


#--------------  継承   ---------------------
class Base:
    basevalue="base"
    
    def spam(self):
        print( "Base.spam()" )

    def ham(self):
        print( "ham" )

class Derived(Base):
    def spam(self):
        print( "Derived.spam()" )
        self.ham()
"""
class added:
    ad="added"
    def A(self,Base):
   """     


derived=Derived()
print( "{0}".format( derived.basevalue ) )
derived.ham()


#----------------多重継承--------------------

class A:
    def method(self):
        print("class A")

class B:
#    def method(self):
        pass
#        print("class B")

class C(A):
    def method(self):
        print("class C")

class D(B,C):
    pass

d=D()
d.method()

#-----------  private public  -------------










