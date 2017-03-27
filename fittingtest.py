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
    return sequences
    
    
def GetFitting(pro):
    tmp=pro[0]
    s2=pro[1]
    score=[0]*(len(pro[0])-len(s2)+1)
    for n in range(0,len(pro[0])-len(s2)+1):
        s1=tmp[n:]
        rows=len(s1)
        cols=len(s2)

        matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
        record=[[0 for i in range(cols+1)] for j in range(rows+1)]
        for i in range(0,rows+1):
            matrix[i][0]=-1*i
            record[i][0]=1
        for j in range(0,cols+1):
            matrix[0][j]=-1*j
            record[0][j]=2
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                m=0
                if s1[i-1] ==s2[j-1]:
                    m=matrix[i-1][j-1]+1
                if s1[i-1] != s2[j-1]:
                    m=matrix[i-1][j-1]-1
                L=[ matrix[i-1][j]-1, matrix[i][j-1]-1,m]
                matrix[i][j]=max(L)
                record[i][j]=L.index(max(L))
               # print matrix[i][j],
        j=cols
        maxcols=[]
        for i in range(0,rows+1):
            maxcols.append(matrix[i][j])
        score[n]=max(maxcols)

    maxscore=max(score)
    i=score.index(maxscore)
    
    s1=tmp[i:]
    rows=len(s1)
    cols=len(s2)
    #print rows,cols
    matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
    record=[[0 for i in range(cols+1)] for j in range(rows+1)]
    for i in range(0,rows+1):
        matrix[i][0]=-1*i
        record[i][0]=1
    for j in range(0,cols+1):
        matrix[0][j]=-1*j
        record[0][j]=2
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m=0
            if s1[i-1] ==s2[j-1]:
                m=matrix[i-1][j-1]+1
            if s1[i-1] != s2[j-1]:
                m=matrix[i-1][j-1]-1
            L=[ matrix[i-1][j]-1, matrix[i][j-1]-1,m]
            matrix[i][j]=max(L)
            record[i][j]=L.index(max(L))    
    j=cols
    maxcols=[]
    for i in range(0,rows+1):
        maxcols.append(matrix[i][j])
    i=maxcols.index(max(maxcols))
    
    new_s1=''
    new_s2=''

    while (i !=0 or j != 0):
        if i==0:
            while j!=0:
                new_s1=''.join(['-',new_s1])
                new_s2=''.join([s2[j-1],new_s2])
                j=j-1
            break
        if j==0:
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
    return maxscore,new_s1,new_s2

    
def main():
    file1=sys.argv[1]
    protein=GetSequence(file1)
    (score,pro1,pro2)=GetFitting(protein)
    print score
    print pro1, "\n", pro2
    
main()
