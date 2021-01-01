class Fruit:
    Total_order=0
    def __init__(self, Order_ID, weight):
        self.Order_ID=Order_ID
        self.weight=weight
        Fruit.Total_order=Fruit.Total_order+1
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)

class Mango(Fruit, object):
    def __init__(self,Order_ID,weight,type,price):
        super(Mango,self).__init__(Order_ID,weight)
        self.type=type
        self.price=price
        #Fruit.Total_order=Fruit.Total_order+1
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)+ ", Variety: " + str(self.type) + ", Total Price: "+str(self.price * self.weight )
    def __add__(self, other):
        temp = 'The total price of the orders are: ' + str((self.price* self.weight) + (other.price* other.weight))                    
        return temp

class JackFruit(Fruit, object):
    def __init__(self,Order_ID,weight,price):
        super(JackFruit,self).__init__(Order_ID,weight)
        self.price=price
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)+ ", Total Price: "+str(self.price* self.weight)
    def __add__(self, other):
        temp = 'The total price of the orders are: ' + str((self.price* self.weight) + (other.price* other.weight))           
        return temp

m1=Mango("Order Id 1", 5,"GopalVog",250)
print(m1)
m2=Mango("Order Id 2", 5,"HariVanga", 230)
print(m2)
j1=JackFruit("Order Id 3", 5,250)
print(j1)
j2=JackFruit("Order Id 4", 4,210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print( m1 + m2 )
print("==================")
print(j1+j2)



#𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝟎𝟎𝟑:
#Write the 𝐌𝐚𝐧𝐠𝐨 and 𝐉𝐚𝐜𝐤𝐟𝐫𝐮𝐢𝐭  classes which are derived from the 𝐅𝐫𝐮𝐢𝐭 
#class with the required methods to give the following outputs as shown.
#[𝐇𝐢𝐧𝐭: 𝐭𝐨𝐭𝐚𝐥 𝐩𝐫𝐢𝐜𝐞=𝐰𝐞𝐢𝐠𝐡𝐭 * 𝐮𝐧𝐢𝐭 𝐩𝐫𝐢𝐜𝐞]
#
#𝐂𝐨𝐝𝐞:
## Do not change the following lines of code.
#Class Fruit:
#     Total_order=0
#
#     def __init__(self, Order_ID, weight):
#         self.Order_ID=Order_ID
#         self.weight=weight
#         Fruit.Total_order=Fruit.Total_order+1
#
#     def __str__(self):
#         return self.Order_ID+", Weight: "+str(self.weight)
#
#class Mango(Fruit):
#      #write your code here
#
#
#
#class JackFruit(Fruit):
#       #write your code here
#
#
#m1=Mango("Order Id 1", 5,"GopalVog",250)
#print(m1)
#m2=Mango("Order Id 2", 5,"HariVanga", 230)
#print(m2)
#j1=JackFruit("Order Id 3", 5,250)
#print(j1)
#j2=JackFruit("Order Id 4", 4,210)
#print(j2)
#print("Total number of Orders: "+str(Fruit.Total_order))
#print("==================")
#print(m1+m2)
#print("==================")
#print(j1+j2)
#
#𝐎𝐮𝐭𝐩𝐮𝐭:
#Order Id 1, Weight: 5, Variety: GopalVog, Total Price: 1250
#Order Id 2, Weight: 5, Variety: HariVanga, Total Price: 1150
#Order Id 3, Weight: 5, Total Price: 1250
#Order Id 4, Weight: 4, Total Price: 840
#Total number of Orders: 4
#==================
#The total Price of the orders are: 2400
#==================
#The total Price of the orders are: 2090