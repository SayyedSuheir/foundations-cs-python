def main():
    while True:
    #Display menu to user
        print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
    #Let User choose
        user_choice = int(input("Please choose number from 1 to 7: "))
    #check user input
        if user_choice ==1:
            print(AddMatrices())
        elif user_choice == 2:
            print(CheckRotation())
        elif user_choice == 3 :
            print(InvertDictionary())
        elif user_choice == 4:
            print(ConvertMatrixToDictionary())
        elif user_choice == 5:
            print(CheckPalindrome())
        elif user_choice == 6:
            print(SearchElementMergeSort())
        elif user_choice == 7:
             exit
    else:
        print("Please enter vailed number from menu (1-7)")


main()