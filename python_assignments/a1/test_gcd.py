from gcd import gcd
def gcd_test():
    assert gcd(20,30)==10
    assert gcd(-20,-30)== "ValueError"
    assert gcd(20.30,30) == "TypeError"
    
if __name__=="__main__":
    gcd_test()
