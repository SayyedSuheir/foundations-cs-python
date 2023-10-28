

def Reverse(s,i):
  
 return s[::-1]*i
  

def RearrangeUpper(s):
   upper_char=""
   lower_char=""
   #Big O(N):N is the len of string
   for char in s:
    
     if char.isupper():
       upper_char += char 
     else:
       lower_char += char
       
   return upper_char + lower_char

def Reorder(s1,s2):
  
    # Remove spaces and convert both strings to lowercase 
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if the sorted strings are equal
    return sorted(s1) == sorted(s2)
          
def GetMax(list):
  max= list[0]
  max_index=0
  #Big O(N): N is the len of list
  for i in  range(1,len(list)):
    if list[i]>max:
     max=list[i]
     max_index = i
    else:
      max = max
  print("The max is {} at postion {}".format(max,max_index)) 
def GetMin(list):
  min = list[0]
  min_index = 0
  #Big O(N): N is the len of list
  for i in range(1,len(list)):
    if min > list[i]:
      min =list[i]
      min_index = i
    else:
      min = min
  print ("The smallest number is {} at position {}".format(min, min_index))
def SumDigits(number):
  sum = 0
  #Big O(N): N is the number of digits
  while(number%10 !=0):
    sum = sum + number%10
    number= number//10
  return sum
def RemoveDuobledLetters(string):
  #base case is string contains one character or empty
  if len(string) < 2:
    return string

  # Recursive case:
  if string[0] == string[1]:
  # If the first two characters are the same, skip the first character and call the function on the rest of the string.
    return RemoveDuobledLetters(string[1:])
  else:
  # If the first two characters are different, keep the first character and call the function on the rest of the string.
    return string[0] + RemoveDuobledLetters(string[1:])#Big O(N): N is the len of string


def ReverseNumber(n,reversed_n=0):
  
  # Base case: If n is 0, we have reversed the integer, so return the reversed result.
  if n == 0:
      return reversed_n
  else:
  # Extract the last digit of n.
   last_digit = n % 10

  # Update the reversed integer by adding the last digit.
   reversed_n = reversed_n * 10 + last_digit

  # Recursively call the function with the remaining digits of n.
  return ReverseNumber(n // 10,reversed_n)
    
    




def main():
  print("#####Question1#####")
  word = input("Enter a string to be reversed :")
  number = int(input("Enter an integer: "))
  print("The reversed word is :",Reverse(word,number))
  print("\n#####Question2#####")
  rearrange_word = input("Enter string to be rearranged : ")
  print("The rearranged word is : ", RearrangeUpper(rearrange_word).replace(" ",""))
  print("\n#####Question3#####")
  string1, string2=input("Enter two strings to compare:").split()
  print("Is string one is reorder of string 2 : ",Reorder(string1,string2))
  print("\n#####Question4#####")
 
  list = input('Enter list of numbers sparated by space: ')
  list_numbers= [float(num) for num in list.split()]
  
  GetMax(list_numbers)
  GetMin(list_numbers)
  print("\n#####Question5#####")
  number = int(input("Enter any integer number to add its digits: "))
  print("The sum of {} is {}".format(number,SumDigits(number)))
  print("\n#####Question6#####")
  string_s = input("Enter a string to remove doubled letters : ").lower()
  print("Your origin string is {} and the removed double is {} ".format(string_s,RemoveDuobledLetters(string_s)))
  print("\n#####Question7#####")
  number = int(input("Enter a number to be reversed: "))
  reversed_n= ReverseNumber(number)
  print("Your number is {} and its reversed version is {}".format(number,reversed_n))


main()





  