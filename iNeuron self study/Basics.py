
#-------------=======STRINGS ARE IMMUTABLE ==================
# variables and data types
a = 10
b = 20.5
c = "Hello, iNeuron!"
is_student = True
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(is_student))  # bool



# string  can be written in 3 ways 
str1 = 'Hello'
str2 = "Hello"
str3 = '''Hello'''
print(str1, str2, str3)
print(type(str1), type(str2), type(str3))  # all are str

number = 3 + 4j
print(type(number))
# output        ------- > <class 'complex'>


# imag = imaginory number in the complax number.add.


# TYPE CASTING - (STRONG TYPE CASTING)
# example 

name  = "omkar"
number  = 7019812805
dd = name + str(number)
print(dd)


# lenth of the string can be taken from the len() function 
dumba  =  "sakuraSwrills"
size = len(dumba)
print(size)
print(dumba[ : : -1])


# accessing the string charectsrs 
data = "OMNAMAHSHIVAY"
print(data[2])

# ------- jumping --------
# the third thing in athe slicing

# ex
dumba  =  "sakuraSwrills"
print(dumba[::2])


# IF U DONT GIVBE THE STARTIBNG POINT AND THE ENDING PIINT THEN IT LKL AUTOMATICLY TAKE ATHE STARTING AND ENDING POINTS 
print(dumba[::-1])
# if u dont give  amy direction then itll directly jump and stsrt in the jump direction 


print(dumba[0::-1])




# scalling concept 

# -9 -8 -7 -6 -5 -4 - 3 -2 -1 0 1 2 3 4 5 6 7 8 9
# even though you dont provide the jump value then still by default its gonna be the positive 1 

# if tehre is a aconta diction in the direction and the jumping direrctin then its gonna return the ''empety string. 


# in lists too the same formula will be used for slyciling  


# basicaly when we try to multiplay any string or collection or any dataa into 10 the itsgona multiply it with that amout of number and print it again by that times

# as we do a concatination i our stings  as sowen below

ddr ="dexxa"  + "Trash"
print(ddr)

# as shown in  below

dd = "DEXXA "
print(dd*4)


# with \n we can print the outputs at new lines eatch time.
dd = "DEXXA \n"
print(dd*4)


#   STINGS are immulatble 
# use pass to keep the uncompleted code to rest 



# ===================LIST =============

l1 = []
# lists are written in a square braces []
# you can store any kind of data in the list 
# as shown bellow

l2 = ["DEXXA" , 9878 , True , [4,5,6]]


# same logic is applied in case of the slicing in the lists too 

# ex 

print(l2[3][1])

# to reverse the list 

print(l2[: : -1])

# TAKING USER inPut from the user

a = int(input("ENTER THE N&UM !:"))
b =(input("ENTER THE N&UM !:"))
print(a*b)


# when the input takes any kind of inoput the input will by default take it as a  STRING 

# if want to chnage you have to change manualy  

# we can create a multiple veriables in a sinhle line  as shown bellow 

a = 55
b = 'DEXXA'
c = True
d = [2,3,4]

# anbd this is the equal

a,b,c,d = 55,"DEXXA",True , [2,3,4]




# ===================TUPLES =============

t1 = (2,3,4)


# again tghe all slicing and fetching  willbe the same but the tuples are the imutable 
# you cant just re-write the value opf the tupesd












# ======================================CONTROLE STATEMENTS ======================#


# if statement and ELSE 


dd =input("enter your name !:")
if dd == "DEXXA":
    print("WELLCOME ADMIN ")
else:
    print("WELLOCME USER")



# suppose i have created a asttament ans di dont what to erite anything then i can sue pass

a= 10
if a < 20:
    pass
# this is not going to give us any error 


# LOOPS
# ================= FOR LOOP ==========
    # for with lists
l = [1,2,3,4,5,6,7,8,9,10]
j = 0
for i in l:
    print(f"The {j}th element is {i}")
    j = j+1
    
    
    # for with lists 
    
for n in l :
    if type(n) == list:
        print(n[2]) or   print(n[ : : -1])
        


# for with strings 
s =  "DEXXA TRASH " 

for k in s :
    print(k)
    
    # for with tuplules 
t = (2,3,4,5,6,7,8)
for i in t:
    print(i)
    
    
    
# # pyaramid using the for loop 

# This code snippet is creating a pyramid pattern using nested for loops in Python.
n  = int(input("NUMBER OF STEPS INPYRAMID :"))

for i in range(n):
    for j in range(i+1):
        print(".",end = "_")
    print("")
    
    
# i did it by my self and that good for a day .
n  = int(input("NUMBER OF STEPS in SQUARE  :"))

for i in range(n):
    print("* "*n,end = " ")
    print("")
    
    
    
    
# ================= WHILE LOOP ========== 

i = 1
n =5

while i<n:
    print(i)
    i= i+1
    
# we can se else statemnt in loops too , we can use else in for and we can use else in while loop too in python 



# break in the loop 

x = 1
while x < 10:
    print(x)
    if x  == 5:
        break
    x = x+1
    
    
    
# continue in the loop 

x = 1
while x < 10:
    print(x)
    if  x ==  20:
        break
    if x  == 5:
        continue
    x = x+1
    
# class 18 th sep stamp 
# 
# 3: 15 : 52 seconds 
