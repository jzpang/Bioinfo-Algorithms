import sys
import string
import math


def getData(file):
    f=open (file, "r")
    s=f.readline()
    s=s.strip()
    temp=s.split()
    #print temp
    k=int(temp[0])
    m=int(temp[1])
    centers=[]
    for i in range(0,k):
        s=f.readline()
        s=s.strip()
        center=s.split(' ')
        center=map(float, center)
        centers.append(center)
    points=[]
    f.readline()
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
    #print centers
    return k,m,centers,points



def distortion(k,m,centers,points):
    distance=[]
    u=0
    for i in range(0,len(points)):
        tmp=[]
        for j in range(0,len(centers)):
            sum=0
            for v in range(0,m):
                sum=sum+(points[i][v]-centers[j][v])**2
            sq=math.sqrt(sum)
            #print sum,"\t",sq
            tmp.append(sq)
        #print tmp
        u=(min(tmp))**2
        #print u
        distance.append(u)
   # print distance
    s=0
    for l in distance:
        s=s+l
    #print s
    dist=s/(1.0*len(points))
    
    
    return dist
        
        
        

def main():
    file1=sys.argv[1]
    (k,m,centers,points)=getData(file1)
    dist=distortion(k,m,centers,points)
    print dist
    
    
main()