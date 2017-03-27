import sys
import string
import math


def getPoints(file):
    f=open (file, "r")
    s=f.readline()
    s=s.strip()
    temp=s.split()
    k=int(temp[0])
    m=int(temp[1])
    points=[]
    while True:
        s=f.readline()
        try:
            if len(s)>0:
                s=s.strip()
                point=s.split(' ')
                point=map(float, point)
                points.append(point)
            else:
                break
        except:
            break
    f.close()
    return k,m,points
  

def Lloyd(k,m,points):
    centers=points[0:k]
    
    for c in range(1,2000):
        lable=[]
        for i in range(0,len(points)):
            tmp=[]
            for j in range(0,len(centers)):
                sum=0
                for v in range(0,m):
                    sum=sum+(points[i][v]-centers[j][v])**2
                sq=math.sqrt(sum)
            #print sum,"\t",sq
                tmp.append(sq)
            pos=tmp.index(min(tmp))
            lable.append(pos)
        #print len(points)
        #print len(lable)
        cluster=[[] for t in range(0,k)]
        for i in range(0, len(lable)):
            for j in range(0,k):
                if lable[i]==j:
                    #print points[i]
                    cluster[j].append(points[i])
        for j in range(0, len(cluster)):
            add=[0 for o in range (0,m)]
            for p in range(0,len(cluster[j])):
                for q in range(0,m):
                    add[q]=add[q]+cluster[j][p][q]
            for q in range(0,m):
                add[q]=add[q]/(1.0*len(cluster[j]))
            centers[j]=add
    
    
    return centers

def out(centers):
    for i in centers:
        for j in i:
            print ('%0.3f' % j),
        print "\r"

  
def main():
    file1=sys.argv[1]
    (k,m,points)=getPoints(file1)
    centers=Lloyd(k,m,points)
    out(centers)
    
    
main()
    
    