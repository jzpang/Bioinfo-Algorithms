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
    
def getMatrix_Alignment(s):
    s1=s[0]
    s2=s[1]
    rows=len(s[0])
    cols=len(s[1])
    #print rows,cols
    matrix=[[0 for i in range(cols+1)] for j in range(rows+1)]
    for i in range(0,rows+1):
        matrix[i][0]=1*i
    for j in range(0,cols+1):
        matrix[0][j]=1*j
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            m=0
            if s1[i-1] ==s2[j-1]:
                m=matrix[i-1][j-1]+0
            if s1[i-1] != s2[j-1]:
                m=matrix[i-1][j-1]+1
            L=[ matrix[i-1][j]+1, matrix[i][j-1]+1,m]
            matrix[i][j]=min(L)

    return matrix[-1][-1]
                  
            
            
def main():
    file1=sys.argv[1]
    protein=GetSequence(file1)
    score=getMatrix_Alignment(protein)
    print score
    
main()

