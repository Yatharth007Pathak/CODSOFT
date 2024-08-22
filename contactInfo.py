import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.contacts = {}
        
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("500x400")
        
        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Add Contact Button
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)
        
        # View Contacts Button
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=10)
        
        # Update Contact Button
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=10)
        
        # Search Contact Button
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=10)
        
        # Delete Contact Button
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")
        
        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        else:
            messagebox.showwarning("Error", "Name and phone number are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return
        
        contact_list = "Contacts:\n\n"
        for name, details in self.contacts.items():
            contact_list += f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n"
        
        messagebox.showinfo("Contact List", contact_list)

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:")
            email = simpledialog.askstring("Input", "Enter new email address:")
            address = simpledialog.askstring("Input", "Enter new address:")
            
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        else:
            messagebox.showwarning("Error", "Contact not found.")

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        result = []
        
        for name, details in self.contacts.items():
            if search_term in name or search_term in details['phone']:
                result.append(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
        
        if result:
            messagebox.showinfo("Search Results", "\n".join(result))
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        else:
            messagebox.showwarning("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()