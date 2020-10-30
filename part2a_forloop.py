# FIND ANWSER FOR THIS SERIES:
# 1 ^3 + 2 ^3 + 4 ^3 + 8 ^3 + 16 ^3 + 32 ^3 + 64 ^3 + 128 ^3 + 256 ^3 + 512 ^3 + 1024 ^3 + 
# OUTPUT:
# 1 ^3 + 2 ^3 + 4 ^3 + 8 ^3 + 16 ^3 + 32 ^3 + 64 ^3 + 128 ^3 + 256 ^3 + 512 ^3 + 1024 ^3 + 
# Total Sum=  1227133513

sum=0
n =11
for num in range(0,n):
 print(2**num,"^3", end=" + ")
 base = 2**num
 result = base**3
 sum= sum + result
print() 
print("Total Sum= ",sum)
