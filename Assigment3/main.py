def main():
    #Display menu to user
    print("Please choose from menu below:\n1.Add Matrices\n2.Check Rotation\n3.Invert Dictionary\n4.Convert Matrix to Dictionary\n5.Check Palindrome\n6.Search for an Element & Merge Sort\n7.Exit\n")
    #Let User choose
    user_choice = int(input("Please choose number from 1 to 7: "))
    
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