#Question 1
#length of the inpot string
string=("Python is a case sensitive language")
print(len(string))
#reverse the order of string
print(string[::-1])
#slice function
print(string[10:25])
#replacing “a case sensitive” with “object oriented”
new_string=string[0:10]+"object oriented"+string[26:]
print(new_string)
#index of subtracting "a"
index=string.find("a")
print(index)
#removeing white spaces
print(string.replace(" ",""))
print(end='\n''\n')

#Question 2
name="Rasneet Kaur"
SID="21104010"
department="Eelctrical"
CGPA="9.5"
print("Hey, %s Here!"'\n'
      "My SID is %s"'\n'
      "I am from %s department and my cgpa is %s"%(name , SID , department , CGPA))
print(end='\n''\n')

#Question 3
a=56
b=10
#a&b
print(a&b)
#a|b
print(a|b)
#a^b
print(a^b)
#left shift
print(a<<2 , b<<2)
#right shift
print(a>>2 , b>>4)
print(end='\n''\n')

#Question 4
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
 
if (number1 > number2) and (number1 > number3):
   largest = number1
elif (number2 > number1) and (number2 > number3):
   largest = number2
else:
   largest = number3
 
print("The largest number is",largest)
print(end='\n''\n')

#Question 5
word="My name is Rasneet Kaur"
if ('name' in word):
    check='Yes'
else:
    check='No'
print(check)
print(end='\n''\n')

#Question 6
p=21
q=20
r=29
if(p+q>r):
    possibility='Yes'
elif(q+r>p):
    possibility='Yes'
elif(r+p>q):
    possibility='Yes'
else:
    possibility='No'
print(possibility)
