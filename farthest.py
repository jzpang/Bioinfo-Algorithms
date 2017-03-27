import sys
import string
import math


def getPoints(file):
    f=open (file, "r")
    s=f.readline()
    s=s.strip()
    temp=s.split()
    #print temp
    k=int(temp[0])
    m=int(temp[1])
    points=[]
    while True:
        s=f.readline()
        try:
            if len(s)>0:
                s=s.strip()
                #print s
                point=s.split(' ')
                #print point
                point=map(float, point)
                #print point
                points.append(point)
                #genome=''.join([genome, s])
            else:
                break
        except:
            break
    f.close()
    #print points
    return k,m,points

def farthestFirstTraversal(k,m,points):
    centers=[]
    centers.append(points[0])
    del points[0]
    #print len(centers)
    while (len(centers)<k):
        distance=[]
        for l in range(0,len(points)):
            tmp=[]
            for c in range(0,len(centers)):
                sum=0
                for i in range(0,m):
                    sum=sum+((points[l][i]-centers[c][i])**2)
                sq=math.sqrt(sum)
                tmp.append(sq)
            #print tmp
            distance.append(min(tmp))
        pos=distance.index(max(distance))
        centers.append(points[pos])
        del points[pos]
    return centers
                
def out(centers):
    for i in centers:
        for j in i:
            print j,
        print "\r"
                    

def main():
    file1=sys.argv[1]
    (k,m,points)=getPoints(file1)
    centers=farthestFirstTraversal(k,m,points)
    out(centers)
    
    
main()