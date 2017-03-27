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
    
  
def BreakpointsNum(P):
    L=map(int, P)
    points=0
    if ((L[0]-0) != 1):
        points+=1
    for i in range(1,len(P)):
        if (L[i]-L[i-1] != 1):
            points+=1
    #print len(P),L[-1]
    if (len(P)+1-L[-1] != 1):
        points+=1
    
    return points
  
def main():
    file1=sys.argv[1]
    #out=open("out.txt","w")

    seq=GetSequence(file1)
    #print seq
    num=BreakpointsNum(seq)
    print num
    #P=GreedySorting(seq,out)

    
main()