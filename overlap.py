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
    
    
def GetOverlap(pro):
    #s1=pro[0]
    #s2=pro[1]
    dim=min(len(pro[0]),len(pro[1]))
    score=[[0 for q in range(dim)] for p in range(dim)]
    for p in range(dim):
        #print "!!!!!!!!!!"
        for q in range(dim):
            s1=pro[0][-p-1:]
            s2=pro[1][0:q+1]
            #print s1
            ##print s2
            #print "******"
            rows=len(s1)
            cols=len(s2)

            matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
            #record=[[0 for i in range(cols+1)] for j in range(rows+1)]
            for i in range(0,rows+1):
                matrix[i][0]=-2*i
            #    record[i][0]=1
            for j in range(0,cols+1):
                matrix[0][j]=-2*j
            #    record[0][j]=2
            for i in range(1,rows+1):
                for j in range(1,cols+1):
                    m=0
                    if s1[i-1] ==s2[j-1]:
                        m=matrix[i-1][j-1]+1
                    if s1[i-1] != s2[j-1]:
                        m=matrix[i-1][j-1]-2
                    L=[ matrix[i-1][j]-2, matrix[i][j-1]-2,m]
                    matrix[i][j]=max(L)
             #       record[i][j]=L.index(max(L))
               # print matrix[i][j],
        
            score[p][q]=matrix[i][j]    
        
        #maxscore=max(score)
        #pos=score.index(maxscore)
        #print pos;
        #new_s1=pro[0][-pos-1:]
        #new_s2=pro[1][:pos+1]
    largest=0
    d1=0
    d2=0
    for m in range(0,min(len(pro[0]),len(pro[1]))):
        for n in range(0,min(len(pro[0]),len(pro[1]))):
            if score[m][n]>largest:
                largest=score[m][n]
                d1=m
                d2=n
    s1=pro[0][-d1-1:]
    s2=pro[1][:d2+1]
    rows=len(s1)
    cols=len(s2)
    
    matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
    record=[[0 for i in range(cols+1)] for j in range(rows+1)]
    for i in range(0,rows+1):
        matrix[i][0]=-2*i
        record[i][0]=1
    for j in range(0,cols+1):
        matrix[0][j]=-2*j
        record[0][j]=2
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m=0
            if s1[i-1] ==s2[j-1]:
                m=matrix[i-1][j-1]+1
            if s1[i-1] != s2[j-1]:
                m=matrix[i-1][j-1]-2
            L=[ matrix[i-1][j]-2, matrix[i][j-1]-2,m]
            matrix[i][j]=max(L)
            record[i][j]=L.index(max(L))    

    
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
        
        
    return largest,new_s1,new_s2
    #for i in range(0,n+1):


    
def main():
    file1=sys.argv[1]
    protein=GetSequence(file1)
    (score,pro1,pro2)=GetOverlap(protein)
    print score
    print pro1, "\n", pro2
    
main()
