#GitHub:https://github.com/10533185/Shopping-items.git

#Global Variables Rate

Rate={'EUR':1,'USD':1.09,'CAD':1.53,'GBP':0.88}

#Global Variables Products

Products={'Ball-Red':{'Name':'Cosco Ball','Description':'High Bouncing Ball','Seller':'Amazon traders','price':4,'Currency':'EUR'},
          'Shirt-small':{'Name':'Puma T Shirt','Description':'Slim fit-made for men,Higly Attractive Design','Seller':'John','price':3,'Currency':'CAD'},
          'Watch-med':{'Name':'Titan Watch','Description':'Stylish,Analog,Design-made for men','Seller':'Andrew','price':1,'Currency':'USD'}}

#Basket Class

class Basket:
    
    def __init__(self,b={}):
        self.__Items = b.copy()
        
        
#Method to check product Quantity in the basket:

    def basketItems(self,sku):
        if sku not in self.__Items:
            return 0       
                
        return self.__Items[sku]
    
#Method to addItems in the basket:

    def addItems(self,sku,qty):
        if qty<0:
            raise ValueError('Negative Quantity is not permitted')
        
        self.__Items[sku]= self.basketItems(sku)+qty
        print("Contents in the Basket after Adding Item: \n")
        print(self.basketContents())

#Method to removeItems from the basket:

    def removeItems(self,sku,qty):
        for k,v in list(self.__Items.items()):
            if v==0:
                del self.__Items[k] 
            
        if qty<0:
            raise ValueError('Negative Quantity is not allowed')
            
        if self.basketItems(sku)<qty:
            raise ValueError(sku +' is removed from the basket')
        
        
        self.__Items[sku]= self.basketItems(sku)-qty
        
        print("Contents in the Basket after Removing Item: \n")
        print(self.basketContents())
        
#Method to value the basket in Euro:  

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
            Value=Products['Ball-Red']['Currency']
            txt="Total Value of Items in the Basket [ in {} ] :"
            
        return print(txt.format(Value),total)
    
#Method to show basket contents:
    
    def basketContents(self):
        print("Basket Items : \n")
        for k,v in list(self.__Items.items()):
            val=v
            txt="Quantity : {}"
            Key=k
            txt6="SKU : {}"
            Desc=Products[k]['Description']
            txt5="Description: {} \n"
            Price=Products[k]['price']
            txt4="Price : {}"
            Curr=Products[k]['Currency']
            txt3="{}"
            seller=Products[k]['Seller']
            txt2="Seller : {}"
            Name=Products[k]['Name']
            txt1="Name : {}"
            
            print(txt6.format(Key))
            print(txt1.format(Name))
            print(txt4.format(Price),txt3.format(Curr))                      
            print(txt.format(val))
            print(txt2.format(seller))
            print(txt5.format(Desc))
                
                
        
            
                
        
            
            
        
                       
            
        
