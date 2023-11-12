#import JSON library
import json
#import Beautifulsoup library
from bs4 import BeautifulSoup
#import requests library used to request info from real websites
import requests
#create empty dictionary
tabs={}
#Open tab function to add tab
def OpenTab():
#Big O(N): Is the number of items entered by user
    while True:
        try:    
         number_tabs = int(input("how many tab do you want to add: "))
         for i in range (number_tabs):
        #Ask user to enter the title of tab
            title_tab = input("Enter the title of tab: ")
        #Ask user to enter the URL of tab
            url_tab = input("Enter the URL: ")
            http_url_tab = 'http://' + url_tab
        #Create tabs key
            tab_id = len(tabs)+1
        #Save user inputs in dictionary
            tabs[tab_id]={'title':title_tab,'URL':http_url_tab,'nest_tabs':{}}
         for key ,value in tabs.items():
            print("A new tab with tab ID {} : title-{} and  url-{} are added sucessfully".format(key,tabs[key].get('title'),tabs[key].get('URL')))
         return tabs
        except ValueError:
             print("Please eneter a numbers only")

def CloseTab():
#BigO(N): N is the number of index entered by user (worst case deleting last tab in dict)
    user_index=input("Enter the index of tab that you want to close or 'leave it empty to close the last opened tab': ")
    if user_index =="":
        close_tab=tabs.pop(len(tabs))
        print("Last tab was colsed...")
    for key in tabs:
          if user_index == key :
            close_tab = tabs.pop(int(user_index))
    print( f"The tab with title {tabs[int(user_index)].get('title')} and url {tabs[int(user_index)].get('URL')} is closed..")
    
    
    

def GetHTMLContent(tabs_url):
    #request html content from online website(https://www.youtube.com/watch?v=XVv6mJpFOb0)
    html_file = requests.get(tabs_url).text
    #used to search tags inside webpage(li , h1,h5,p ,a....)
    #create instance of beauitfulsoup
    soup = BeautifulSoup(html_file,'lxml')
    
    print(soup)

def SwitchTab(tabs):
    #Ask user to enter index of tab
    user_index = input("Enter tab index to switch:")
    if user_index.isalpha():
         while True:
             print("please enter a number or leave it empty..")
             user_index = input("Enter tab index to switch:")
             break
    #if index is empty get the url of last tab
    if user_index == "":
          # Get url of last tab
          tabs_url = tabs[len(tabs)].get('URL')
          GetHTMLContent(tabs_url)
    elif int(user_index) <= len(tabs):
        #Get url of given tab index by user   
        tabs_url = tabs[int(user_index)].get('URL')
        GetHTMLContent(tabs_url)
    else:
         print("No tab found..")
    
def DisplayAllTabs():#BigO(N):N is the lenght of dictionary
      for key in tabs:
        print(tabs[key].get('title'),tabs[key].get('nest_tabs'))
            
def OpenNestedTab(tabs):#BigO(N):N is last index in dictionary(len of dictionary)
      
        #Ask user to enter the index of tab 
        user_index = int(input("Enter the index of tab to be nested : "))
        #Ask user to enter title for nested tab
        nested_title = input("Enter title for nested tab: ")
        #Ask user to enter content for nested tab
        nested_content = input("Enter content of nested tab: ")
        #insert nested tab 
        for key in tabs:
                if user_index == key:
                    tabs[user_index]['nest_tabs']= {'nested_title':nested_title,'nested_content':nested_content}
        print(tabs)

def ClearAllTabs(tabs):#BigO(N):N is the len of dictionary
      #clear method of dictionary to remove all elements of dictionary (w3schools.com)
      tabs.clear()
      print("All tabs are cleared....")                  

def SaveTabs(tabs):#BigO(N):N is the length of dumped dictionary
        #create json file (https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/)
        with open('tabs.json','w') as file:
            json.dump(tabs,file)  
        print("JSON file created successfully...")      
def  ImpotTabs():
      #open json file (https://www.geeksforgeeks.org/read-json-file-using-python/)
      with open('tabs.json') as file:
      #import json file data
        print( json.load(file))         

#Create function to greet user and display the menu
def main():
    
   #greeting statment
    print("Welcome to our program")
   #Display the menu
    print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
    #Ask user to choose from menu 
    while True:
            try:
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
                            SwitchTab(tabs)
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                    elif user_choice==4:
                            DisplayAllTabs()
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                    elif user_choice==5:
                            OpenNestedTab(tabs)
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                    elif user_choice==6:
                            ClearAllTabs(tabs)
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                    elif user_choice==7:
                            SaveTabs(tabs)
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                    elif user_choice==8:
                            ImpotTabs()
                            print("\n1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
                            user_choice = int(input("Choose number from the menu above (1-9): "))
                if  user_choice==9:
                        print("You have exit the menu...")  
                        break 
            except ValueError:
                  print("please enter number not letter") 
            
                        
    

  
main()