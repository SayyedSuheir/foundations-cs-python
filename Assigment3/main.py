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
    for row in result:
     print(row)

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
    test=True
    if row1*col1 == row2*col2 and row1==col2:
       for i in range(row1) :
            
            for l in range(col2):
          
             if  matrix1[i][l]==matrix2[l][i]:
                
                  test=True
             else:
                 test = False
    else:
        test = False            
    return test

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
            print(ConvertMatrixToDictionary())
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