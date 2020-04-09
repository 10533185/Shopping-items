class Basket:
    
    def __init__(self,I={}):
        self.__Items = I
        
    def basketItems(self,sku):
        return self.__Items[sku] 
