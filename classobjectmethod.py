class Python:
 stringName = ""
 def get_String(self,userinput):
  self.stringName = userinput.upper()
 def print_String(self):
  print(self.stringName.lower())

p1 = Python()
name = input()
p1.get_String(name)
p1.print_String()
