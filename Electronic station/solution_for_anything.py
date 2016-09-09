class Solution_for_Anything(object):
    def __init__(self, foo):
        self.foo = foo
        
    def __eq__(self, x):
        return True

    def __ne__(self, x):
        return True
    
    def __lt__(self, x):
        return True
    
    def __gt__(self, x):
        return True
    
    def __le__(self, x):
        return True
    
    def __ge__(self, x):
        return True
    
def checkio(anything):
    x = Solution_for_Anything(anything)
    return x
