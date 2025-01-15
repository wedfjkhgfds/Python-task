class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        """Add a contact to the contact book."""
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = phone
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """View all contacts in the contact book."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts in your contact book:")
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            print(f"Contact found: Name: {name}, Phone: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """Delete a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contact_book = ContactBook()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "5":
            print("Exiting the contact book program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
