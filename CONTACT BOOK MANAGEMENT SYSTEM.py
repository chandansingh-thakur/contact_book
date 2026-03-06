#--------------------------------------------------------
#I am going to make a contact book with file handling.
#--------------------------------------------------------

## There will be 6 options
  # 1.Adding Contact
  # 2.View saved or existing Contact
  # 3.Search contact by name
  # 4.Search contact by email
  # 5.deleting contact
  # 6.Exit  """if we don't exit the loop would be continue of 1,2,3,4,5"""
import os 
Contact_file = "contact-record2.txt" 
   
#define adding conatct
def adding_contact():
    name = input("Enter a name :").strip()
    phone_no = int(input("Enter the phone number :").strip())
    email = input("enter your email as example@gmail.com :").strip()
    
    if not name or not phone_no or not email:   #if empty then it will show error
        print("Name, phone number and email cannot be empty.")
        return
    if "@gmail.com"  not in email:
        print("You are entering wrong gmail format,enter your email as example@gmail.com :")
        return
    with open(Contact_file,"a") as file:   #appending the contact in contact book
        file.write(f" {name}  | {phone_no}  | {email} \n")
    print("contact added in contact file. ")
    print("------------------------------------")

#define viewing contact    
def view_contact():
    if not os.path.exists(Contact_file):
          print("File does not exist.")
          return
    with open(Contact_file,"r") as file:
          lines = file.readlines()        #firstly reading the whole file
    
    if not lines:
        print("No cantact saved yet.") #If file exists but contains no contacts.
        return
    
    print("\n--------ALL CONTACTS-------") 
    for line in lines:
        line = line.strip()  #when we read lines then it removes \n
        if not line:
            continue    #if line is blank skipiing it
        part = line.split("|")
        if len(part) != 3:
            continue
        name,phone,email = part
        print(f"Name : {name} , Phone-number : {phone} and email : {email}")
    print("--------------------------------------------")

#define searching conatcts
def search_contacts_by_name():
    searching_name = input("Enter name to search :").strip().lower() #i have done uppercase of words that i can match in equalling.
    find = False
    
    if not os.path.exists(Contact_file): #i used this for error correction except try and except
            print("No contacts saved yet.")
            return
                   
    with open(Contact_file,"r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            name , phone , email = parts
            if searching_name in name.lower(): #i have alraedy done input in uppercase so to match that name also should be in uppercase.
                print(f"Named as {searching_name} is present as : name: {name} , phone number :{phone} , email : {email}")
                find = True
    
    if not find:
        print("No contact found of that name. ")
print("---------------------------------")

def search_by_email_only():
    email_search = input("Enter email to search: ").strip().lower()
    find = False

    if not os.path.exists(Contact_file):
           print("No contacts saved yet.")
           return
    with open(Contact_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                    continue
            name, phone, email = parts
            if email_search in email.lower():
                print(f"email as {email_search} is present as : name: {name} ,  phone number :{phone} , email : {email}")
        
                find = True
    if not find:
        print("No contact found with that email.")
#deleting contact
def delete_all_contacts():
    if not os.path.exists(Contact_file):
        print("No contact file found.")
        return

    confirm = input("Are you sure you want to delete ALL contacts? (yes/no): ").strip().lower()
    
    if confirm != "yes":
        print("It means that you don't want to delete contacts.")
        return
    
    with open(Contact_file, "w") as file: # Opening file in write mode to clear all contents
        pass   # file cleared

    print("All contacts have been deleted successfully.\n")
                    
#main content
def main_content():
    while True:  #menu keeps showing until user chooses exit.
        print("\n What do you want to do in contact Book.")
        print("-------------------------------")
        print("---Here are the options----")
        #giving options to user
        print("[press 1] : Add contact")
        print("[press 2] : View contact")
        print("[press 3] : Search conatct by name")
        print("[press 4] : search contact by email")
        print("[press 5] : Delete all contact") 
        print("[press 6] : To exit") 
        choice = int(input("Enter a choice: ").strip())
        
        if choice == 1:
            adding_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contacts_by_name()
        elif choice ==4:
            search_by_email_only()
        elif choice ==5:
            delete_all_contacts()
        elif choice == 6:
            print("---------Exiting-----")
            break
        else:
            print("please enter the number between 1 to 6...")

#now calling main_content .
main_content()       
