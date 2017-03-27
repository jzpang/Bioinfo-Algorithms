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
    #print pro

    while True:
        s=f.readline()
        seq=''
        try:
            if len(s)>0:
                s=s.strip()
                seq=re.split(' +',s)
                #print seq
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
    for i in range(0,rows+1):
        matrix[i][0]=-5*i
        record[i][0]=1
    for j in range(0,cols+1):
        matrix[0][j]=-5*j
        record[0][j]=2
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m=0
            m=matrix[i-1][j-1]+blosum[pro_order.index(s1[i-1])][pro_order.index(s2[j-1])]
            L=[ matrix[i-1][j]-5, matrix[i][j-1]-5,m]
            matrix[i][j]=max(L)
            record[i][j]=L.index(max(L))
            
    
    new_s1=''
    new_s2=''

    i=rows
    j=cols
    while (i !=0 or j != 0):
        if i==0:
            while j!=0:
                new_s1=''.join(['-',new_s1])
                new_s2=''.join([s2[j-1],new_s2])
                j=j-1
            break
        if j==0:
            while i!=0:
                new_s1=''.join([s1[i-1],new_s1])
                new_s2=''.join(['-',new_s2])
                i=i-1
            break
        if record[i][j]==0:
            new_s1=''.join([s1[i-1],new_s1])
            new_s2=''.join(['-',new_s2])
            i=i-1
        elif record[i][j]==1:
            new_s1=''.join(['-',new_s1])
            new_s2=''.join([s2[j-1],new_s2])
            j=j-1
        elif (record[i][j]==2 ):
            new_s1=''.join([s1[i-1],new_s1])
            new_s2=''.join([s2[j-1],new_s2])
            i=i-1
            j=j-1
       
        else:
            print "Wrong",record[i][j]
            break
    print matrix
    return matrix[-1][-1], new_s1, new_s2
                  
            
            
def main():
    file1=sys.argv[1]
    file2=sys.argv[2]

    protein=GetSequence(file1)
    #print protein
    (Blosumprotein,Blusummatrix)=GetBlosum62(file2)
    #print Blosumprotein, Blusummatrix
    (score,s1,s2)=getMatrix_Alignment(protein,Blosumprotein,Blusummatrix)
    
    out=file('out.txt','a+')
    out.write(str(score))
    out.write("\n")
    out.write(s1)
    out.write("\n")
    out.write(s2)
    
main()