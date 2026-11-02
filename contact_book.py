# Aaron Walker
# Contact Book


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone.isdigit():
        print("Invalid phone number. Digits only.")
        return

    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phones": [phone],
        "email": email,
        "address": address
    }

    print(f"{name} added successfully.")


def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("Contact list is empty.")
        return

    print("\n===== CONTACT LIST =====")

    for name in sorted(contacts):
        print(f"\nName: {name}")
        print("Phone Number(s):", ", ".join(contacts[name]["phones"]))
        print("Email:", contacts[name]["email"])
        print("Address:", contacts[name]["address"])


def search_contact(contacts):
    """Search for a contact."""
    search = input("Enter a name to search: ").strip().lower()

    found = False

    for name, info in contacts.items():
        if search in name.lower():
            found = True

            print("\nContact Found")
            print("---------------------")
            print("Name:", name)
            print("Phone Number(s):", ", ".join(info["phones"]))
            print("Email:", info["email"])
            print("Address:", info["address"])

    if not found:
        print("No matching contacts found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")


def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    while True:
        print("\nUpdate Menu")
        print("1. Add Phone Number")
        print("2. Update Email")
        print("3. Update Address")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            phone = input("Enter new phone number: ").strip()

            if phone.isdigit():
                contacts[name]["phones"].append(phone)
                print("Phone number added.")
            else:
                print("Invalid phone number.")

        elif choice == "2":
            email = input("Enter new email address: ").strip()
            contacts[name]["email"] = email
            print("Email updated.")

        elif choice == "3":
            address = input("Enter new address: ").strip()
            contacts[name]["address"] = address
            print("Address updated.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def main():
    """Main program loop."""
    contacts = {}

    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                add_contact(contacts)

            elif choice == 2:
                view_contacts(contacts)

            elif choice == 3:
                search_contact(contacts)

            elif choice == 4:
                delete_contact(contacts)

            elif choice == 5:
                update_contact(contacts)

            elif choice == 6:
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        except Exception as error:
            print("An unexpected error occurred:", error)


# Start the program
main()
