class Hotel:
    def __init__(self,name):
        self.name = name
        self.stuffs = []
        self.stuffs_age = []
        self.stuffs_phone = []
        self.guest = []
        self.guest_age = []
        self.guest_phone = []
    def addGuest(self,guest,guest_age,guest_phone="000"):
        self.guest.append(guest)
        self.guest_age.append(guest_age)
        self.guest_phone.append(guest_phone)   
        print("Guest With ID " + str(len(self.guest)) + " is created")             

    def printAllStuffs(self):
        print("All Staffs:")        
        print("Number of Stuff: " + str(len(self.stuffs)))
        temp = ''
        for i in range(len(self.stuffs)):
            temp +="Staff ID: " + str(i+1) + " Name: " + self.stuffs[i] + " Age: " + str(self.stuffs_age[i]) + " Phone no: " + self.stuffs_phone[i]
        return temp
            #print( self.stuffs[i] )        
    def printAllGuest(self):
        print("All Guest:")
        print("Number of Guest: " + str(len(self.guest)))
        temp = ''
        for i in range(len(self.guest)):
            temp += "Guest ID: " + str(i+1) + " Name: " + self.guest[i] + " Age: " + str(self.guest_age[i]) + " Phone no.: " + self.guest_phone[i] 
            if i < len(self.guest)-1:
                temp += "\n"
        return temp

    def addStuff(self,staff,age, stuff_phone="000"):
        self.stuffs.append(staff)
        self.stuffs_age.append(age)
        self.stuffs_phone.append(stuff_phone)
        print("Staff With ID " + str(len(self.stuffs)) + " us added")

    


h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.printAllStuffs())
print("=================================")
h.addGuest("Carol",35,"123")
print("=================================")
print(h.printAllGuest())
print("=================================")
h.addGuest( "Diana", 32, "431")
print("=================================")
print(h.printAllGuest())



#𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝟎𝟐:
#Write the 𝐇𝐨𝐭𝐞𝐥 class with the required methods to give the following 
#outputs upon executing the following code:
#𝐂𝐨𝐝𝐞:
## Write your codes here.
#
## Do not change the following lines of code.
#h = Hotel("Lakeshore")
#h.addStuff( "Adam", 26)
#print("=================================")
#print(h.printAllStuffs())
#print("=================================")
#h.addGuest(“Carol”,35,”123”)
#print("=================================")
#print(h.printAllGuest())
#print("=================================")
#h.addGuest( "Diana, 32, “431”)
#print("=================================")
#print(h.printAllGuest())

#𝐎𝐮𝐭𝐩𝐮𝐭:
#Staff With ID 1 is added
#=================================
#All Staffs:
#Number of Staff:  1
#Staff ID: 1 Name: Adam Age: 26 Phone no: 000
#=================================
#Guest With ID 1 is created
#=================================
#All Guest:
#Number of Guest:  1
#Guest  ID: 1 Name: Carol Age: 35 Phone no.: 123
#=================================
#Guest With ID 2 is created
#=================================
#All Guest:
#Number of Guest:  2
#Guest  ID: 1 Name: Carol Age: 35 Phone no.: 123
#Guest  ID: 2 Name: Dianal Age: 32 Phone no.: 431
#