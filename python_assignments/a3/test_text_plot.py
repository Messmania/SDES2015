from text_plot import *
import unittest
"For testing correct functionalities"
x1,y1=[0,1,2,3,4,5],[0,2,4,6,8,10] 
x2=[1, 3, 4, 1, 5, 5, 6, 4, 2, 1, 2, 3, 4, -3, -2, -2, -1, -4, -3, -1]
y2=[0, 1, 0, 3, 2, 0, 0, 2, 3, -3, -2, -2, -3, 4, 4, 3, 3, -2, -2, -2]

"For testing errors"
x3,y3="Test1","Test2"
x4,y4=[1,2,3],[1,2,3,4]
w1,w2 = 0,0


obj = MyPlot(x1,y1,12,33)

class TestMyPlot(unittest.TestCase): 
    """Tests the various functions from the module text_plot"""
    def test_TypeError(self):        
        self.assertRaises(TypeError,MyPlot,x3,y3)
    def test_ValueError_len(self):        
        self.assertRaises(ValueError,MyPlot,x4,y4)
    def test_ValueError_dim(self):
        self.assertRaises(ValueError,MyPlot,x1,y1,w1,w2)
    def test_calPos(self):        
        self.assertEqual(obj.calPos(3),"   *")          
    def test_scaleToWindow(self):
        obj.scaleToWindow()
        self.assertEqual((obj.x,obj.y),([0, 2, 4, 6, 8, 10], [0, 6, 12, 18, 24, 30])) 
    def test_plotSine(self):
        self.assertEqual(plotSine(),'                 *\n\n\n        *                *\n\n\n\n\n\n\n*                                 *                                  *\n\n\n\n\n\n\n                                           *                *\n\n\n                                                   *\n')    
    def test_plotXY(self):
        obj = MyPlot(x2,y2,11,8)
        obj.plotXY()
        self.assertEqual(obj.mapStr," **\n  ** **\n        **\n       *\n     *  ***\n\n** *  **\n     *  *\n")
    def test_plot(self):
        plotStr = plot(x2,y2,11,8)
        self.assertEqual(plotStr," **\n  ** **\n        **\n       *\n     *  ***\n\n** *  **\n     *  *\n")
    
if __name__=="__main__":
    unittest.main()
