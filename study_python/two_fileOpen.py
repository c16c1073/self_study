def par( file_name1, file_name2 ):
    file1=open( file_name1 )
    file2=open( file_name2 )
    list=file1.read().split( "\n" )
    width=max( map(len, list) )# map(適用関数、対象リスト)
    list=[ n.ljust(width)  for n in list ]

    

    output( list,width,file2.read().split("\n") )

    file1.close()
    file2.close()


def output(llist,lwidth,rlist):
    llen,rlen=len(llist),len(rlist)
    print(llist)
    print()
    print(rlist)
    print()
   
    n=""*lwidth
    for i in range( max(llen,rlen) ):
            if i<llen:
                    print( llist[i],end="" )
                    if i<rlen:
                            print( "| %s" % rlist[i])
                    else:
                            print("|")
            else:
                    print( "%s| %s" % (llist[llen-1], rlist[i]) )





if __name__=="__main__":
        import sys
        if len(sys.argv)!=3:
                print( "usage; python par.py filel file2" )
        else:
                par( sys.argv[1],sys.argv[2] )
