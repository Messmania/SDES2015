from text_plot import *
def plot_test():
    """Tests the various functions from the module text_plot"""
    x1,y1=[0,1,2,3,4,5],[0,2,4,6,8,10] 
    x2=[1, 3, 4, 1, 5, 5, 6, 4, 2, 1, 2, 3, 4, -3, -2, -2, -1, -4, -3, -1]
    y2=[0, 1, 0, 3, 2, 0, 0, 2, 3, -3, -2, -2, -3, 4, 4, 3, 3, -2, -2, -2]
    assert calPos(3)=="   *"    
    assert scaleToWindow(x1,y1,12,33)==([0, 2, 4, 6, 8, 10], [0, 6, 12, 18, 24, 30])    
    assert plot(x2,y2,11,8)==' **\n  ** **\n        **\n       *\n     *  ***\n\n** *  **\n     *  *\n'
    
if __name__=="__main__":
    plot_test()
