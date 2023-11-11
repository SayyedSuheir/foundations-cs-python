#import Beautifulsoup library
from bs4 import BeautifulSoup
#import requests library used to request info from real websites
import requests
#create empty dictionary
tabs={}
#Open tab function to add tab
def OpenTab():

        
        number_tabs = int(input("how many tab do you want to add: "))
        for i in range (number_tabs):
        #Ask user to enter the title of tab
            title_tab = input("Enter the title of tab: ")
        #Ask user to enter the URL of tab
            url_tab = input("Enter the URL: ")
        #Create tabs key
            tab_id = len(tabs)+1
        #Save user inputs in dictionary
            tabs[tab_id]={'title':title_tab,'URL':url_tab,'nest_tabs':{}}
        
        print("A new tab with tab ID {} : title-{} and  url-{} are added sucessfully".format(tab_id,title_tab,url_tab))
        return tabs

def CloseTab():
    user_index=input("Enter the index of tab that you want to close or 'leave it empty to close the last opened tab': ")
    if user_index =="":
        close_tab=tabs.pop(len(tabs))
        print("Last tab was colsed...")
    for key in tabs:
          if user_index == key :
            close_tab = tabs.pop(int(user_index))
    print( f"The tab with title {tabs[int(user_index)].get('title')} and url {tabs[int(user_index)].get('URL')} is closed..")
    
    
    

def GetHTMLContent(tabs_url):
    #request html content from real website
    html_file = requests.get(tabs_url).text
    #used to search tags inside webpage(li , h1,h5,p ,a....)
    #create instance of beauitfulsoup
    soup = BeautifulSoup(html_file,'lxml')
    jobs = soup.find_all('li')

def SwitchTab(tabs):
    tabs_url=[]
    tabs_dict = tabs[0]
    print(tabs_url.append(tabs_dict.get('url')))
    
   # GetHTMLContent(tabs_url)

#Create function to greet user and display the menu
def ShowMenu():
    tabs={}
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
                tabs = OpenTab()
                print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                user_choice = int(input("Choose number from the menu above (1-9): "))
        elif user_choice==2:
               
               CloseTab()
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