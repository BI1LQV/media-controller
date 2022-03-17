from numpy import Inf, Infinity


def preProcess(list):
    res=[]
    for img in list:
        if img == None:
            continue
        xmax=-1
        xmin=10000
        ymax=-1
        ymin=10000
        zmax=-1
        zmin=10000
        for (x,y,z) in img:
            xmax=max(x,xmax)
            xmin=min(x,xmin)
            ymax=min(y,ymax)
            ymin=min(y,ymin)
            zmax=min(z,zmax)
            zmin=min(z,zmin)
        for line in img:
            line[0]=(line[0]-xmin)/(xmax-xmin)
            line[1]=(line[1]-ymin)/(ymax-ymin)
            line[2]=(line[2]-zmin)/(zmax-zmin)
        res.append(img)
    return res