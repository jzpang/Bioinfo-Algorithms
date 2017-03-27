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
                genome=''.join([genome, '+'])
                genome=''.join([genome, s])
            else:
                break
        except:
            break
    sequences=genome.split('+')
    del sequences[0]
    f.close()
    #print sequences
    return sequences
    
def GetBlosum62(filename):
    f=open (filename, "r")
    scorematrix=[]
    s=f.readline()
    s=s.strip()
    pro=re.split(' +',s)
    while True:
        s=f.readline()
        seq=''
        try:
            if len(s)>0:
                s=s.strip()
                seq=re.split(' +',s)
                del seq[0]
                seq=map(int, seq)
                scorematrix.append(seq)
            else:
                break
        except:
            break
    f.close()
    
    return pro,scorematrix
    
    
    
def getMatrix_Alignment(s, pro_order,blosum):
    s1=s[0]
    s2=s[1]
    rows=len(s[0])
    cols=len(s[1])
    #print rows,cols
    matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
    record=[[0 for i in range(cols+1)] for j in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m=0
            m=matrix[i-1][j-1]+blosum[pro_order.index(s1[i-1])][pro_order.index(s2[j-1])]
            L=[m, matrix[i-1][j]-5, matrix[i][j-1]-5,0]
            matrix[i][j]=max(L)
            if matrix[i][j]==0:
                record[i][j]=3
            else:
                record[i][j]=L.index(max(L))
            
    
    new_s1=''
    new_s2=''
    tmpmax=[]
    tmpmaxrecord=[]
    for i in range(0,rows+1):
        tmp=max(matrix[i])
        tmpmax.append(tmp)
        tmpmaxrecord.append(matrix[i].index(tmp))
    tmp=max(tmpmax)
    i=tmpmax.index(tmp)
    j=tmpmaxrecord[i]
    #print i,j,tmp
    while (i !=0 and j != 0 and record[i][j]!=3):
        #print i,j
        if (record[i][j]==0):       
            new_s1=''.join([s1[i-1],new_s1])
            new_s2=''.join([s2[j-1],new_s2])
            i=i-1
            j=j-1
        elif record[i][j]==1:
            new_s1=''.join([s1[i-1],new_s1])
            new_s2=''.join(['-',new_s2])
            i=i-1
        elif record[i][j]==2:
            new_s1=''.join(['-',new_s1])
            new_s2=''.join([s2[j-1],new_s2])
            j=j-1
        else:
            print "Wrong",record[i][j]
            break
            
    return tmp, new_s1, new_s2
                  
            
            
def main():
    file1=sys.argv[1]
    file2=sys.argv[2]

    protein=GetSequence(file1)
    print protein
    (Blosumprotein,Blusummatrix)=GetBlosum62(file2)
    print Blosumprotein, Blusummatrix
    (maxscore, s1,s2)=getMatrix_Alignment(protein,Blosumprotein,Blusummatrix)
    print maxscore
    print s1, "\n", s2
    
main()