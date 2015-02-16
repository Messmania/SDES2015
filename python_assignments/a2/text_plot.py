import math

def plot(x1,y1,wX=80,wY=30):
    """Plots the text based scatter given the two tuples/list x and y, window dimensions are optional"""
    xT,yT=type(x1),type(y1)
    lx,ly=len(x1),len(y1)
    if (xT!=tuple and xT!=list) or (yT!=tuple and yT!=list):
        raise TypeError
    elif lx!=ly or lx==0:
        raise ValueError
    else:
        mapStr=""        
        x,y=scaleToWindow(x1,y1,wX,wY)
        maxY=max(y)
        minY=min(y)
        if maxY>0:
            for i in range(maxY,-1,-1):
                mapStr=posLine(i,x,y,mapStr)+"\n"
        if minY<0:
            for i in range(-1,minY-1,-1):
                mapStr=posLine(i,x,y,mapStr)+"\n"
        return mapStr;
                        
def posLine(i,x,y,mapStr):
    """makes a string for every y value and add"""
    minX=min(x)
    absX=minX
    xVal=[]            
    for k in range(0,len(y)):
        if i==y[k]:
            xVal.append(x[k])
    while len(xVal)>0:
        minXVal=min(xVal)       
        pairX=minXVal-absX
        absX=minXVal+1
        mapStr=mapStr+calPos(pairX)
        xVal.remove(minXVal) 
    #mapStr=mapStr+"\n"
    return mapStr

    
def scaleToWindow(x,y,dimX,dimY):
    """Scales the given values to the size of the window"""         
    maxX,minX=max(x),min(x)
    maxY,minY=max(y),min(y)
    lenX=maxX-minX+1
    lenY=maxY-minY+1
    xS=[]
    yS=[]
    for i in range(0,len(x)):
        xS.append(int((x[i]*dimX)/lenX))
        yS.append(int((y[i]*dimY)/lenY))
    return xS,yS

 
def calPos(x):
    """Return a string with * placed at its absolute horizontal position given as x"""
    curX=""
    for j in range(0,x):
        curX=curX+" "        
    cursor=curX+"*"
    return cursor
            
def plotSine():
    """Plots the sine wave in the default window size in the range 0-2pi"""
    x,y=[],[]
    i=0
    while i<=math.pi*2:
        y.append(math.sin(i))
        x.append(i)
        i=i+math.pi/4
    return plot(x,y)        
            
if __name__=="__main__":
    print plotSine()
