contacts=[]


while True:
 print("1.Add contact")
 print("2.view contact")
 print("3.search contact")
 print("4.delete contact")
 print("5.exit contact")
 choice=int(input("enter your choice (1-5)"))
 if choice==1:
    name=input("enter your contact name")
    phone=input("enter your contact phone number")
    contact={"name":name,"phone":phone}
    contacts.append(contact)
    print(f"{name}and{phone}added successfully")
 elif choice==2:
    if len(contacts)==0:
        print("no contact found")
    else:
        print("saved contacts")
        for idx ,contact in enumerate(contacts,start=1):
          print(f"{idx}.{contact['name']}and {contact['phone']}")
 elif choice==3:
    search_name=input("enter the name to be searched")
    found=False
    for contact in contacts:
        if contact["name"].lower()==search_name.lower():
             print(f"{contact['name']}and{contact['phone']}")
             found=True
             break
    if not found:
            print("not found")
 elif choice==4:
        delete_name=input("enter the name to be deleted")
        found=False
        for contact in contacts:
            if contact["name"].lower()==delete_name.lower():
                contacts.remove(contact)
                print(f"{contact['name']}and{contact['phone']} deleted successfully")
                found=True
                break
        if not found:
            print("not found, cannot delete")
 elif choice==5:
    print("exiting the contact_book...goodbye")
    break
 else:
      print("invalid choice")







