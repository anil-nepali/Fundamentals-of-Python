print("------------------------------------------------------------")
print("             Simple Contact Book                  ")
print("------------------------------------------------------------")

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter any choice (1, 2, 3, 4, 5): ")

    if choice == "1":
        print("\n---------------- Adding Contact -------------------------")
        name = input("Enter Name: ")
        contact_number = input("Enter Phone Number: ")
        email = input("Enter Email ID: ")

        contact = {
            "Name": name,
            "Phone": contact_number,
            "Email": email
        }

        contacts.append(contact)
        print(f"\nContact  added successfully!")

    elif choice == "2":
        print("\n--------------- View All Contacts ---------------------------")
        if not contacts:
            print("No contacts found!")
        else:
            count =1
            for contact in contacts:
                print(f"{count}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
                count +=1
        print("\n--------------- View All Contacts ------------------------------")
    elif choice == "3":
        print("\n--------------- Search Contacts --------------------------------")
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact['Name'].lower() == search_name.lower():
                print("\nContact Found!")
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
                found = True
                break
        if not found:
            print("Contact not found!")

    elif choice == "4":
        print("\n-------------------- Delete Contacts ------------------------------")
        delete_name = input("Enter name to delete: ")
        deleted = False
        for contact in contacts:
            if contact['Name'].lower() == delete_name.lower():
                contacts.remove(contact)
                print(f"\nContact '{delete_name}' deleted successfully!")
                deleted = True
                break
        if not deleted:
            print("Contact not found!")
        print("\n-------------------- Delete Contacts ------------------------------")

    elif choice == "5":
        print("Exiting the program... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
