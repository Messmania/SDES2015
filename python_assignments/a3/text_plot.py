import math

class MyPlot():
    
    def __init__(self,x1,y1,wX=80,wY=30):
        """Initializes the class variables to be used in subsequent methods"""
        
        self.xT,self.yT=type(x1),type(y1)
        self.lx,self.ly=len(x1),len(y1)
        if (self.xT!=tuple and self.xT!=list) or (self.yT!=tuple and self.yT!=list):
            raise TypeError
        elif self.lx!=self.ly or self.lx==0 or self.ly==0 or wX==0 or wY==0:
            raise ValueError
        else:    
            self.x,self.y = x1,y1
            self.wX,self.wY = wX,wY        
            self.maxX,self.minX=max(self.x),min(self.x)
            self.maxY,self.minY=max(self.y),min(self.y)
            self.mapStr=""
        
    def plotXY(self):
        """Plots the text based scatter given the two tuples/list x and y, window dimensions are optional
        It first scans the plot from top to bottom and left to write, checks for every possible x,y value in lists and keeps
        making string by adding the present element to their correct position"""
              
        self.scaleToWindow()
        if self.maxY>=0:
            for i in range(self.maxY,-1,-1):
                self.posLine(i)
                self.mapStr=self.mapStr+"\n"
        if self.minY<0:
            for i in range(-1,self.minY-1,-1):
                self.posLine(i)
                self.mapStr=self.mapStr+"\n"
                        
    def posLine(self,i):
        """makes a string for every y value or horizontal line with * placed at position
        and adds to original string"""
        absX=self.minX
        xVal=[]            
        for k in range(0,len(self.y)):
            if i==self.y[k]:
                xVal.append(self.x[k])
        while len(xVal)>0:
            minXVal=min(xVal)       
            pairX=minXVal-absX
            absX=minXVal+1
            self.mapStr=self.mapStr+self.calPos(pairX)
            xVal.remove(minXVal)

        
    def scaleToWindow(self):
        """Scales the given lists to the size of the given window dimensions""" 
        xS=[]
        yS=[]
        self.lx=self.maxX-self.minX+1
        self.ly=self.maxY-self.minY+1
        for i in range(0,len(self.x)):
            xS.append(int((self.x[i]*self.wX)/self.lx))
            yS.append(int((self.y[i]*self.wY)/self.ly))
        self.x,self.y = xS,yS
        "change to variables to contain info about new scaled lists"
        self.maxX,self.minX=max(xS),min(xS)
        self.maxY,self.minY=max(yS),min(yS)
        self.lx=self.maxX-self.minX+1
        self.ly=self.maxY-self.minY+1

     
    def calPos(self,x):
        """Return a string with * placed at its absolute horizontal position given by x"""
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
    a= MyPlot(x,y,80,30)
    a.plotXY()
    return a.mapStr       


def plot(x,y,sX=80,sY=30):
    a = MyPlot(x,y,sX,sY)
    a.plotXY()
    return a.mapStr      
    
       
if __name__=="__main__":
    print plotSine()
