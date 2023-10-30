def AddMatrices():
    #size of matrices
    row =int(input("Enter the number of rows: "))
    col=int(input("Enter the number of columns: "))
    #Enter values of first Matrix
    print("Enter the values of first matrix")
    matrix1=InputMatrixElemtens(row,col)
    #Enter values of Second Matrix
    print("Enter the values of Second Matrix")
    matrix2=InputMatrixElemtens(row,col)
    result = SumMatrices(matrix1, matrix2)
    print("The sum of the two matrices is:")
    #for row in result:
    return  result

def InputMatrixElemtens(rows,col):
    #create empty matrix
    matrix =[]
    #Add elements
    #O(N): N is the number of row enetered by user
    for i in range(rows):
        row=[]
    #O(N): N is the number of column enetered by user
        for j in range(col):
           element= eval(input(f"Enter element of row {i+1},column {j+1}: "))
           row.append(element)
           matrix.append(row)
    return matrix

def SumMatrices(matrix1,matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def CheckRotation():
    #create first matrix
    row1= int(input("Enter the number of rows for first matrix M1: "))
    col1= int(input("Enter the number of cols for first matrix M1: "))
    
    matrix1=[]
    for i in range(row1):
      mat1=[]
      for j in range(col1):
        elements = int(input("Enter the values of first matrix: "))
        mat1.append(elements)
    matrix1.append(mat1)
    #create second matrix
    row2= int(input("Enter the number of rows for first matrix M2: "))
    col2= int(input("Enter the number of cols for first matrix M2: "))
    
    matrix2=[]
    for i in range(row2):
        mat2=[]
        for j in range(col2):
            elements = int(input("Enter the values of second matrix: "))
            mat2.append(elements)
    matrix2.append(mat2)
    #Test if they are rotation for each other
    test=bool
    if row1*col1 == row2*col2 and row1 == col2 and row2 == col1:
        for i in range(row1):
            for j in range(col2):
                test = matrix1[i][j] == matrix2[j][i]
    else:
         test = False
    return test

def InvertDictionary():
    #creating Dictionary by user
    value_number = int(input("Enter the number of items in the dictionary: "))
    user_dict = {}

    for i in range(value_number):

        value = input("Enter value: ")
        user_dict[i] = value

    print("Before inverting:")
    print(user_dict)
    #invertred given Dictionary
    inverted_dict = {}

    for key, value in user_dict.items():
      if value in inverted_dict:
          if isinstance(inverted_dict[value], list):
              inverted_dict[value].append(key)
          else:
              inverted_dict[value] = [inverted_dict[value], key]
      else:
          inverted_dict[value] = key
          
    print("After inverting:")
    return inverted_dict
   

def ConvertMatrixToDict():
  matrix = []
  n = int(input("Enter the number of users: "))

  for i in range(n):
      first_name = input("Enter First Name: ")
      last_name = input("Enter Last Name: ")
      user_id = "ID"+str(i)
      job_title = input("Enter Job Title: ")
      company = input("Enter Company: ")

      user_data = [first_name, last_name, user_id, job_title, company]
      matrix.append(user_data)
  user_dict = {}
  for user_data in matrix:
      user_id = user_data[2]  # ID is at index 2 in the user data list
      user_info = [user_data[0], user_data[1], user_data[3], user_data[4]]  # Extracting first name, last name, job title, and company
      user_dict[user_id] = user_info
  
  return user_dict

def CheckPalindrome() :
    word = input("Enter a string: ")
    result = is_palindrome(word)
    if result:
     return  print(f"The string '{word}' is a palindrome.")
    else:
     return print(f"The string '{word}' is not a palindrome.")

def is_palindrome(s):
  s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
  if len(s) <= 1:
      return True
  else:
      if s[0] == s[-1]:
          return is_palindrome(s[1:-1])
      else:
          return False

# Recursive function to check if a string is a palindrome
def SearchElementMergeSort():
        #Ask user to create list
    user_list = []
    number_values = int(input("Enter the number of values: "))
    for i in range(number_values):#bigO(N):N is the number of values entered by user
        elements = int(input("Enter values of list elements: "))
        user_list.append(elements)

    print(user_list)

    #search for element will use linear search
    searched_value=int(input("Enter number to search for: "))
    index = -1
    ind_lst=[]
    for i in range(number_values):
        if user_list[i] == searched_value:
            index = i
            ind_lst.append(index)
    if len(ind_lst) >=1:    
        print(f"{searched_value} is at index {ind_lst}")
    else:  
        print(f"This number {searched_value} does not exits")
        
    #Sort using MergeSort
    return "unsorted list is: ",user_list,"\nSorted list is : ",MergeSort(user_list)
                                                    
    
def MergeSort(lst):
  #divid list to single elements
  #BigO(lgN):N is the len of list
    if len(lst) > 1:
        mid = len(lst) // 2
        left_list = lst[:mid]
        right_list = lst[mid:]
        
        MergeSort(left_list)
        MergeSort(right_list)
        #conquer element in sorted way
        i = j = k = 0
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                lst[k] = left_list[i]
              
                i += 1
            else:
                lst[k] = right_list[j]
                j += 1
                
            k += 1

        while i < len(left_list):
            lst[k] = left_list[i]
            i += 1
            k += 1
            
        while j < len(right_list):
            lst[k] = right_list[j]
            j += 1
            k += 1

    return lst

def main():
    #Display menu to user
    print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
    #Let User choose
    user_choice = int(input("Please choose number from 1 to 7: "))
    # O(1):Constant 
    while user_choice > 0 and user_choice <=7 :
    
    #check user input
        if user_choice ==1:
            print(AddMatrices())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
        #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 2:
            print(CheckRotation())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
            #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 3 :
            print(InvertDictionary())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
            #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 4:
            print(ConvertMatrixToDict())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
            #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 5:
            print(CheckPalindrome())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
            #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 6:
            print(SearchElementMergeSort())
            #Display menu to user
            print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
             #Let User choose
            user_choice = int(input("Please choose number from 1 to 7: "))
        elif user_choice == 7:
             break
    else:
        print("Please enter vailed number from menu (1-7)")
        main()


main()