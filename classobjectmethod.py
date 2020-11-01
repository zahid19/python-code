# Problem Statement: Write a Python class which take two methods
# get_String and print_String
# get_String accept a string from the user and store the string as upper case
# then print_String print the string in lower case

class Python:
 string = ''
 def get_String(self,userinput):
  self.string = userinput.upper()
 def print_String(self):
  print(self.string.lower())

p1 = Python( )
name = input()
p1.get_String(name)
p1.print_String()
