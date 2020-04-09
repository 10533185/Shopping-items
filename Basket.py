class Basket:
    
    def __init__(self,I={}):
        self.__Items = I
        
    def getItems(self,sku):
        return self.__Items[sku]
