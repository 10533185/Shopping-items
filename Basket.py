class Basket:
    
    def __init__(self,I={}):
        self.__Items = I.copy()
        
    def basketItems(self,sku):
        if sku not in self.__Items:
            return 0
        return self.__Items[sku]
