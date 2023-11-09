#create function to display greet user and display the menu
def ShowMenu():
   #greeting statment
    print("Welcome to our program")
   #Display the menu
    print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
    #Ask user to choose from menu 
    user_choice = int(input("Choose number from the menu above (1-9): "))
    while user_choice > 9 or user_choice <= 0:
        print(user_choice," is Invaild number please choose number from menu (1 to 9) ")
        print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
        user_choice = int(input("Choose number from the menu above (1-9): "))
    if user_choice==1:
            OpenTab()
    elif user_choice==2:
            CloseTab()
    elif user_choice==3:
            SwitchTab()
    elif user_choice==4:
            DisplayAllTabs()
    elif user_choice==5:
            OpenNestedTab()
    elif user_choice==6:
            ClearAllTabs()
    elif user_choice==7:
            SaveTabs()
    elif user_choice==8:
            ImpotTabs()
    elif user_choice==9:
            print("You have exit the menu...")
    
        
    
    
def main():
  #call function show menu 
  ShowMenu()
  
main()