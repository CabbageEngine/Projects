import json
from pathlib import Path



# Simple Contact Book
'''Allow user to store and retrieve contact names and numbers using
a Python Dictionary. 
- Add new contacts
- View all contacts
- Search by name
- Save to a .txt or .json file
- Add basic input validation (ex. no duplicate names)'''

'''
# Code where the contact information is given
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def lookup_contact(name):
    return contacts.get(name, "Contact not found.")

# Test
add_contact("Alice", "555-1234")
add_contact("Bob", "555-5678")

print(lookup_contact("Alice"))  # Should return 555-1234
print(lookup_contact("Eve"))    # Should return Contact not found.
'''

# Takes User Input, Add / Delete / Edit Contacts, Export to a file

# Load contacts from file if available
def load_contacts(filename=Path("Simple_Contact_Book/contacts.json")):
    try:
        with filename.open("r") as file:
            return json.load(file)
    # Error if file not found or error if file is corrupted or empty
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

# Save contacts to a file
def save_contacts(filename=Path("Simple_Contact_Book/contacts.json")):
    # Check to make sure folder exists
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "w") as file:
        json.dump(contacts, file, indent =4)

def add_contact(full_name, number):
    contacts[full_name] = number
    print(f"Added {full_name} with number {number}.")

def lookup_contact(full_name):
    return contacts.get(full_name, "Contact not found.")

def edit_contact(full_name):
    if full_name in contacts:
        new_number = input(f"Enter a new number for {full_name}: ").strip()
        contacts[full_name] = new_number
        print(f"Updated {full_name}'s number to {new_number}.")
    else:
        print("Contact not found.")

def delete_contact(full_name):
    if full_name in contacts:
        del contacts[full_name]
        print(f"{full_name} has been deleted.")
    else:
        print("Contact not found.")

# Load existing contacts if file exists
contacts = load_contacts()

# Menu loop
while True:
    print("""
Simple Contact Book
1. Add a contact
2. Look up a contact
3. Edit a contact
4. Delete a contact
5. Quit and save """
          )
    
    choice = input("\nChoose an option (1 - 5): ")

    # Add contact
    if choice == '1':
        first = input("First name: ").strip().title()
        last = input("Last name: ").strip().title()
        number = input("Phone number: ").strip()
        full_name = f"{first} {last}"
        add_contact(full_name, number)

    # Look-up contact
    elif choice == '2':
        first = input("First name: ").strip().title()
        last = input("Last name: ").strip().title()
        full_name = f"{first} {last}"
        result = lookup_contact(full_name)
        print(f"{full_name}: {result}")

    # Edit contact
    elif choice == '3':
        first = input("First name: ").strip().title()
        last = input("Last name: ").strip().title()
        full_name = f"{first} {last}"
        edit_contact(full_name)

    # Delete contact
    elif choice == '4':
        first = input("First name: ").strip().title()
        last = input("Last name: ").strip().title()
        full_name = f"{first} {last}"
        delete_contact(full_name)
    
    # Save and Quit
    elif choice == '5':
        save_contacts()
        print("Contacts saved. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number between 1 and 5.")