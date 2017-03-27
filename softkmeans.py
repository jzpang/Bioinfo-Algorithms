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
    s=f.readline()
    s=s.strip()
    beta=float(s)
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
    return k,m,beta,points
  

def SoftKmeans(k,m,beta,points):
    centers=points[0:k]
    
    for i in range(0,100):
        HM=HiddenMatrix(centers,points,k,m,beta)
        centers=generateCenters(k,m,points,HM)
    return centers



def generateCenters(k,m,points,HM):
    centers=[]
    for i in range(0,k):
        center=[]
        for j in range (0,m):
            upsum=0
            downsum=0
            for l in range(0, len(points)):            
                upsum=upsum+HM[i][l]*points[l][j]
                downsum=downsum+HM[i][l]
            xij=upsum/downsum
            center.append(xij)
        centers.append(center)
    return centers

def HiddenMatrix(centers,points,k,m,beta):
    HM=[[0 for i in range(0,len(points))] for j in range(0,k)]
    for i in range(0,k):
        for j in range(0,len(points)):
            d=dist(points[j],centers[i])
            HM[i][j]=math.exp(-beta*d)
    sumallcent=sumallcenter(HM)
    for i in range(0,k):
        for j in range(0,len(points)):
            HM[i][j]=HM[i][j]*1.0/sumallcent[j]
    return HM



def sumallcenter(matrix):
    sumvector=[]
    for j in range(0,len(matrix[0])):
        summ=0
        for i in range(0,len(matrix)):
            summ=summ+matrix[i][j]
        sumvector.append(summ)
    return sumvector
            
            
def dist(point,center):
    summ=0
    for i in range(0,len(point)):
        summ=summ+(point[i]-center[i])**2
    d=math.sqrt(summ)
    return d











def out(centers):
    for i in centers:
        for j in i:
            print ('%0.3f' % j),
        print "\r"

  
def main():
    file1=sys.argv[1]
    (k,m,beta,points)=getPoints(file1)
    centers=SoftKmeans(k,m,beta,points)
    out(centers)
    
    
main()
    