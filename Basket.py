class Basket:
    
    def __init__(self,I={}):
        self.__Items = I.copy()
        
    def basketItems(self,sku):
        if sku not in self.__Items:
            return 0
        return self.__Items[sku]
    
    def addItems(self,sku,qty):
        if qty<0:
            raise ValueError('Negative Quantity is not allowed')
        self.__Items[sku]= self.basketItems(sku)+qty
        
    def removeItems(self,sku,qty):
        if qty<0:
            raise ValueError('Negative Quantity is not allowed')
        if self.basketItems(sku)<qty:
            raise ValueError('Basket is Empty')
        
        self.__Items[sku]= self.basketItems(sku)-qty
