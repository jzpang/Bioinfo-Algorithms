import string 
import sys
import re

  
def main():
    filename=sys.argv[1]
    f=open (filename, "r")
    genome=[]
    while True:
        s=f.readline()
        try:
            if len(s)>0:
                s=s.strip()
                #print s
                #sequences=re.split('[( )]',s)
                genome.append(s)
            else:
                break
        except:
            break
    #out=open("out.txt","w")
    print genome[0]
    #print genome[1]
    #print genome[2]
    print len(genome)

    #print seq
    #num=BreakpointsNum(seq)
    #print num
    #P=GreedySorting(seq,out)

    
main()