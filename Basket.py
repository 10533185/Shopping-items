#Global Variables

Rate={'Ball-Red':5,'Ball-White':6,'Pen-Blue':2,'Paper-White':3,'Shirt-Small':5,'Shirt-Med':6,'Watch-med':25,'Watch-small':15}


class Basket:
    
    def __init__(self,b={}):
        self.__Items = b.copy()
        print(self.__Items)
        
    def basketItems(self,sku):
        if sku not in self.__Items:
            return 0
        return self.__Items[sku] 
    
    def addItems(self,sku,qty):
        if qty<0:
            raise ValueError('Negative Quantity is not permitted')
        self.__Items[sku]= self.basketItems(sku)+qty
        print(sku)
        
    def removeItems(self,sku,qty):
        if qty<0:
            raise ValueError('Negative Quantity is not allowed')
        if self.basketItems(sku)<qty:
            raise ValueError('Basket is Empty')
        
        self.__Items[sku]= self.basketItems(sku)-qty
        
    def value(self):
        total=0
        for k,v in self.__Items.items():
            total+=v*Rate[k]
            print(k)
        return total
