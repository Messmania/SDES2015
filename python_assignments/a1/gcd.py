def gcd(x,y):
    """Finds the gcd of two given positive numbers"""
    xt=type(x)
    yt=type(y)
    try:
        if x<0 or y<0:
            raise ValueError
        elif (xt!=int and xt!=long) or (yt!=int and yt!=long):
            raise TypeError
        else:
            while y:
                x,y=y,x%y
            return x
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
        
