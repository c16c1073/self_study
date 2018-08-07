def mapconcat( fn,seq,sep ):
    
    seq2=map( fn,seq )#
    seq3=[ str(i) for i in seq2  ]

   # return sep.join(seq)
    return sep.join( seq3 ) # join は文字列めゾッド


seq=[1,2,3,4,5,6,7,8,9]
#seq=["asd","qwe","zxc"]
sep="+"

fn=( lambda x : x+10 )

print(mapconcat( fn,seq,sep ))


