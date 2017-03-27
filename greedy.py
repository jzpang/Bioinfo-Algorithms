import string 
import sys
import re

def GetSequence(filename):
    f=open (filename, "r")
    genome=''
    while True:
        s=f.readline()
        try:
            if len(s)>0:
                s=s.strip()
                sequences=re.split('[( )]',s)
                #genome=''.join([genome, s])
            else:
                break
        except:
            break
    #sequences=genome.split(' ')
    del sequences[0]
    del sequences[-1]
    #sequences=map(int, sequences)
    f.close()
    #print sequences
    return sequences
    
  
def GreedySorting(P,out):
    for i in range(0,len(P)):
        L=map(int, P)
        L=map(abs, L)
        #print L
        if (abs(int(P[i])) != (i+1)):   
            pos=L.index(i+1)
            tmp= P[i:pos+1]
            tmp.reverse()
            #print tmp
            for j in range(0,len(tmp)):
                if (int(tmp[j])>0):
                    tmp[j]=tmp[j].replace('+','-')
                else:
                    tmp[j]=tmp[j].replace('-','+')
            P[i:pos+1]=tmp
            #P[pos],P[i]=P[i],P[pos]
            #P.insert(i,tmp)
            #del P[pos+1]
            #print "(",repr(P),")"
            s=' '.join(P)
            s=''.join(['(',s,')'])
            out.writelines (s)
            out.writelines ("\n")
        if (int(P[i]) != (i+1)):
            #print 'lllll'
            P[i]=P[i].replace('-','+')
            s=' '.join(P)
            s=''.join(['(',s,')'])
            out.writelines (s)
            out.writelines ("\n")
            
    return P
  
def main():
    file1=sys.argv[1]
    out=open("out.txt","w")

    seq=GetSequence(file1)
    print seq
    P=GreedySorting(seq,out)
    #(Blosumprotein,Blusummatrix)=GetBlosum62(file2)
    #print Blosumprotein, Blusummatrix
    #(maxscore, s1,s2)=getMatrix_Alignment(protein,Blosumprotein,Blusummatrix)
    #print maxscore
    #print s1, "\n", s2
    
main()