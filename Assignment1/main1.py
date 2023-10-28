print("##########Question:1##########")

#a. 10*(90+2)-5
print("The Result of  10*(90+2)-5 = ", 10 * (90 + 2) - 5)
print()
#b.10*90+2-5
print("The Result of  10*90+2-5 = ", 10 * 90 + 2 - 5)
print()
#c.10*90+(2-5)
print("The Result of  10*90+(2-5) = ", 10 * 90 + (2 - 5))
print()
#d.10.0*(90+2)-5
print("The Result of  10.0*(90+2)-5 = ", 10.0 * (90 + 2) - 5)
print()
#e.120/(20+40)-(6-2)/4
print("The Result of  120/(20+40)-(6-2)/4 = ", 120 / (20 + 40) - (6 - 2) / 4)
print()
#f. 5.0/2
print("The Result of  5.0/2 = ", 5.0 / 2)
print()
#g. 5/2
print("The Result of  5/2 = ", 5 / 2)
print()
#h. 5.0/2.0
print("The Result of  5.0/2.0 = ", 5.0 / 2.0)
print()
#i. 5/2.0
print("The Result of  5/2.0 = ", 5 / 2.0)
print()
#j. 678%3*(8-(9/4))
print("The Result of  678%3*(8-(9/4)) = ", 678 % 3 * (8 - (9 / 4)))
print("##########Question:2##########")

#Ask the user to enter his ID,name,date of birth and address and store them.

id, name, dob, address = input(
    "Please put your ID -full name - date of birth(DD/MM/YYYY)- address:"
).split()
#big O(1) for both while loop
while (len(dob) !=10):
  print("Date of birth must be formatted as follows DD/MM/YYYY")
  dob = input("Please enter date of birth in correct formate again: ")

while (dob[2] != "/"):
  print("Date of birth must be formatted as follows DD/MM/YYYY")
  dob = input("Please enter date of birth in correct formate again: ")

print("Your profile - ID: 0{}, name: {}, DOB: {}, Address: {}".format(
  id, name.upper(), dob, address.lower()))

print("##########Question:3##########")

#Ask the user to enter a number and store it
number = input("Please enter a number to count its digit: ")
#create counter
counter = 0
#big O(1)
if number.isdigit():
  #convert into int
  num = int(number)
  #handle the case if number is 0
  if num == 0:
    counter = 1

#count the digits
#big O(N): N is the number that entered by user to count its digits
  while (num > 0):
    counter += 1
    num = num // 10
#Print the result
print("{} has a {} digits.".format(number, counter))

print("##########Question:4##########")
#Ask the user to enter his/her grade
grade = int(input("Please enter your grade: "))
#Big O(1)
if grade >= 97:
  print("{} is equivalent to A+".format(grade))
elif grade >= 93:
  print("{} is equivalent to A".format(grade))
elif grade >= 90:
  print("{} is equivalent to A-".format(grade))
elif grade >= 87:
  print("{} is equivalent to B+".format(grade))
elif grade >= 83:
  print("{} is equivalent to B".format(grade))
elif grade >= 80:
  print("{} is equivalent to B-".format(grade))
elif grade >= 77:
  print("{} is equivalent to C+".format(grade))
elif grade >= 73:
  print("{} is equivalent to C".format(grade))
elif grade >= 70:
  print("{} is equivalent to C-".format(grade))
elif grade >= 67:
  print("{} is equivalent to D+".format(grade))
elif grade >= 63:
  print("{} is equivalent to D".format(grade))
elif grade >= 60:
  print("{} is equivalent to D-".format(grade))
else:
  print("{} is equivalent to F".format(grade))
#nested statements and loops 2nd way to solve


print("##########Question:5##########")

# ask the user to enter a number
num = int(input("Enter a number to draw pattern: "))

#  print the pattern in increasing order
#Big O(N): N is the number that enterd by user
for i in range(1, num + 1):
  print('*' * i)

#  print the pattern in decreasing order
for i in range(num - 1, 0, -1):
  print('*' * i)

print("##########Question:6##########")
num1, num2 = input("Enter two number please : ").split()
#convert to integer
num1 = int(num1)
num2 = int(num2)
#check if num2 greater than num1
#Big O(N): N is the greater number entered by user 
while (num1 > num2):
  print("Second number must be greater than first number ")
  num2 = int(input("please re-enter second number again:"))
#get the even numbers between num1 and num2 and print the results
for i in range(num1, num2+1):
  if i % 2 == 0:
    print(i, end=" ")
