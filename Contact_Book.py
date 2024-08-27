class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self):
        query = input("Enter name or phone number to search: ")
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone_number]
        if not results:
            print("No contacts found.")
        else:
            print("Search Results:")
            for i, contact in enumerate(results, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def update_contact(self):
        self.view_contact_list()
        try:
            choice = int(input("Enter the contact number to update: ")) - 1
            if choice < 0 or choice >= len(self.contacts):
                print("Invalid choice.")
            else:
                contact = self.contacts[choice]
                print("Enter new details (press Enter to skip):")
                contact.name = input(f"Name ({contact.name}): ") or contact.name
                contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
                contact.email = input(f"Email ({contact.email}): ") or contact.email
                contact.address = input(f"Address ({contact.address}): ") or contact.address
                print("Contact updated successfully!")
        except ValueError:
            print("Invalid input.")

    def delete_contact(self):
        self.view_contact_list()
        try:
            choice = int(input("Enter the contact number to delete: ")) - 1
            if choice < 0 or choice >= len(self.contacts):
                print("Invalid choice.")
            else:
                del self.contacts[choice]
                print("Contact deleted successfully!")
        except ValueError:
            print("Invalid input.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                contact_book.add_contact()
            elif choice == 2:
                contact_book.view_contact_list()
            elif choice == 3:
                contact_book.search_contact()
            elif choice == 4:
                contact_book.update_contact()
            elif choice == 5:
                contact_book.delete_contact()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
