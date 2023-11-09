#empty global tabs list
tabs=[]
#Open tab function to add tab
def OpenTab(tabs):
#Ask user to enter the title of tab
    title_tab = input("Enter the title of tab: ")
#Ask user to enter the URL of tab
    url_tab = input("Enter the URL: ")
#Save user inputs in dictionary
    tab_open={'title':title_tab,'URL':url_tab}
#add the dictionary to list
    tabs.append(tab_open)
    print("A new tab added sucessfully")

def CloseTab(tabs,i):
    #make sure if there is opened tabs
    #if not tabs:
       # print("there is no tab is open")
       # return
    if i is None:
        close_tab = tabs.pop()
        print("last tab has been closed...")
    elif i >=1 or i < len(tabs):
        #close tab at specific index (i-1 since the index of lists counts from 0)
        close_tab = tabs.pop(i-1)
        print("The tab at index {} is closed".format(close_tab))
    else:
        print("Invaild index no tab is closed...")

#Create function to greet user and display the menu
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
    while user_choice !=9:
       
        if user_choice==1:
                OpenTab(tabs)
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==2:
               user_index=int(input("Enter the index of tab that you want to close or leave it empty to close the last opened tab: "))
               CloseTab(tabs,user_index)
               print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
               user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==3:
                SwitchTab()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==4:
                DisplayAllTabs()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==5:
                OpenNestedTab()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==6:
                ClearAllTabs()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==7:
                SaveTabs()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==8:
                ImpotTabs()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
    if  user_choice==9:
               print("You have exit the menu...")
    
        
    
    
def main():
  #call function show menu 
  ShowMenu()
  
main()