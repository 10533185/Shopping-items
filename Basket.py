#Global Variables

Rate={'EUR':1,'USD':1.09,'CAD':1.53,'GBP':0.88}

Products={'Ball-Red':{'Description':'High Bouncing Ball','Seller':'Amazon traders','price':4,'Currency':'EUR'},
          'Shirt-small':{'Description':'Slim fit-made for men','Seller':'John','price':3,'Currency':'CAD'},
          'Watch-med':{'Description':'Stylish Design-made for men','Seller':'Andrew','price':1,'Currency':'USD'}}

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
        print("Contents in the Basket after Adding Item: ")
        for k,v in list(self.__Items.items()):
            if v==0:
                del self.__Items[k]
            
            print(k,v)                     
          
        
    def removeItems(self,sku,qty):
        for k,v in list(self.__Items.items()):
            if v==0:
                del self.__Items[k] 
            
        if qty<0:
            raise ValueError('Negative Quantity is not allowed')
            
        if self.basketItems(sku)<qty:
            raise ValueError(sku +' is removed from the basket')
        
        
        self.__Items[sku]= self.basketItems(sku)-qty
        
        print("Contents in the Basket after Removing Item: ")
        for k,v in list(self.__Items.items()):
            
            print(k,v)
        
        
        
        
    def value(self):
        total=0
        EUR=Rate['EUR']
        USD=Rate['USD']
        CAD=Rate['CAD']
        GBP=Rate['GBP']
        
        for k,v in self.__Items.items():
            if Products[k]['Currency'] == 'EUR':
                total+=EUR*v*Products[k]['price']
            if Products[k]['Currency'] == 'USD':
                total+=USD*v*Products[k]['price']
            if Products[k]['Currency'] == 'CAD':
                total+=CAD*v*Products[k]['price']
            if Products[k]['Currency'] == 'GBP':
                total+=GBP*v*Products[k]['price']
            
        return total
    
    def basketContents(self):
        for k,v in list(self.__Items.items()):
            print(k,v)
    
    
