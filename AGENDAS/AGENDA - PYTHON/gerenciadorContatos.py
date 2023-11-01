import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address, date):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.dateOfBirth = date

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_date_of_birth(self):
        return self.dateOfBirth

class ContactList:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    contact_info = line.strip().split(',')
                    name, phone, email, address, date = contact_info
                    self.contacts.append(Contact(name, phone, email, address, date))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contactsPython.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email},{contact.address},{contact.dateOfBirth}\n")

    def add_contact(self, name, phone, email, address, date):
        new_contact = Contact(name, phone, email, address, date)
        self.contacts.append(new_contact)
        self.save_contacts()

    def remove_contact_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    def edit_contact(self, index, name, phone, email, address, date):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = Contact(name, phone, email, address, date)
            self.save_contacts()
            return True
        return False

    def search_contact_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
        return None

class ContactController:
    def __init__(self, contact_list, view):
        self.contact_list = contact_list
        self.view = view

    def add_contact(self, name, phone, email, address, date):
        self.contact_list.add_contact(name, phone, email, address, date)

    def remove_contact_by_phone(self, phone):
        return self.contact_list.remove_contact_by_phone(phone)

    def edit_contact(self, index, name, phone, email, address, date):
        return self.contact_list.edit_contact(index, name, phone, email, address, date)

    def search_contact_by_phone(self, phone):
        return self.contact_list.search_contact_by_phone(phone)
    
class ContactView:
    def __init__(self, root, controller):
        self.root = root if root else tk.Tk()
        self.controller = controller
        if not self.controller:
            self.controller = ContactController(ContactList(), self)
        self.root.title("Lista de Contatos")
        self.root.geometry("600x400") 

        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Menu Principal", font=('Helvetica', 18))
        label.pack(pady=10)

        add_button = tk.Button(self.root, text="Adicionar Contato", command=self.show_add_contact)
        add_button.pack(pady=5)

        list_button = tk.Button(self.root, text="Listar Contatos", command=self.show_contact_list)
        list_button.pack(pady=5)

        search_button = tk.Button(self.root, text="Buscar Contato", command=self.show_search_contact)
        search_button.pack(pady=5)

    def show_add_contact(self):
        self.clear_screen()
        self.root.title("Adicionar Contato")

        name_label = tk.Label(self.root, text="Nome:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        phone_label = tk.Label(self.root, text="Telefone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        address_label = tk.Label(self.root, text="Endereço:")
        address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        date_label = tk.Label(self.root, text="Data de Nascimento:")
        date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        save_button = tk.Button(self.root, text="Salvar", command=self.add_contact)
        save_button.pack(pady=5)

        cancel_button = tk.Button(self.root, text="Cancelar", command=self.main_menu)
        cancel_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        date = self.date_entry.get()

        self.controller.add_contact(name, phone, email, address, date)
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso.")
        self.main_menu()

    def show_contact_list(self):
        self.clear_screen()
        self.root.title("Lista de Contatos")

        back_button = tk.Button(self.root, text="Voltar para o Menu", command=self.main_menu)
        back_button.pack(pady=5)

        if not self.controller.contact_list.contacts:
            label = tk.Label(self.root, text="Lista de contatos vazia", font=('Helvetica', 12))
            label.pack(pady=10)
        else:
            self.listbox = tk.Listbox(self.root, width=100)
            for contact in self.controller.contact_list.contacts:
                self.listbox.insert(tk.END, f"Nome: {contact.name}, Telefone: {contact.phone}, Email: {contact.email}, Endereço: {contact.address}, Data de Nascimento: {contact.dateOfBirth}")
            self.listbox.pack(pady=10)

            edit_button = tk.Button(self.root, text="Editar Contato", command=self.show_edit_contact)
            edit_button.pack(pady=5)

            remove_button = tk.Button(self.root, text="Remover Contato", command=self.confirm_remove_contact)
            remove_button.pack(pady=5)

    def show_edit_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            contact = self.controller.contact_list.contacts[index]
            self.edit_window(contact, index)

    def edit_window(self, contact, index):
        self.clear_screen()
        self.root.title("Editar Contato")

        name_label = tk.Label(self.root, text="Nome:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.insert(0, contact.name)
        self.name_entry.pack()

        phone_label = tk.Label(self.root, text="Telefone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.insert(0, contact.phone)
        self.phone_entry.pack()

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.insert(0, contact.email)
        self.email_entry.pack()

        address_label = tk.Label(self.root, text="Endereço:")
        address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.insert(0, contact.address)
        self.address_entry.pack()

        date_label = tk.Label(self.root, text="Data de Nascimento:")
        date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.insert(0, contact.dateOfBirth)
        self.date_entry.pack()

        save_button = tk.Button(self.root, text="Salvar", command=lambda: self.save_contact(index))
        save_button.pack(pady=5)

        cancel_button = tk.Button(self.root, text="Cancelar", command=self.show_contact_list)
        cancel_button.pack(pady=5)

    def save_contact(self, index):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        date = self.date_entry.get()

        if self.controller.edit_contact(index, name, phone, email, address, date):
            messagebox.showinfo("Sucesso", "Contato editado com sucesso.")
            self.show_contact_list()
        else:
            messagebox.showerror("Erro", "Índice de contato inválido.")

    def confirm_remove_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            confirmation = messagebox.askyesno("Confirmar Remoção", "Tem certeza que deseja remover o contato selecionado?")
            if confirmation:
                index = int(selected_index[0])
                phone = self.controller.contact_list.contacts[index].phone
                if self.controller.remove_contact_by_phone(phone):
                    messagebox.showinfo("Sucesso", "Contato removido com sucesso.")
                    self.show_contact_list()
                else:
                    messagebox.showerror("Erro", "Contato não encontrado.")

    def show_search_contact(self):
        self.clear_screen()
        self.root.title("Buscar Contato")

        phone_label = tk.Label(self.root, text="Telefone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        search_button = tk.Button(self.root, text="Buscar", command=self.search_contact)
        search_button.pack(pady=5)

        cancel_button = tk.Button(self.root, text="Cancelar", command=self.main_menu)
        cancel_button.pack(pady=5)

    def search_contact(self):
        phone = self.phone_entry.get()
        contact = self.controller.search_contact_by_phone(phone)
        if contact:
            self.clear_screen()
            self.root.title("Contato Encontrado")
            label = tk.Label(self.root, text=f"Nome: {contact.name}, Telefone: {contact.phone}, Email: {contact.email}, Endereço: {contact.address}, Data de Nascimento: {contact.dateOfBirth}")
            label.pack(pady=10)

            edit_button = tk.Button(self.root, text="Editar Contato", command=lambda: self.show_edit_contact_for_search(contact))
            edit_button.pack(pady=5)

            remove_button = tk.Button(self.root, text="Remover Contato", command=lambda: self.confirm_remove_contact_for_search(contact))
            remove_button.pack(pady=5)

            back_button = tk.Button(self.root, text="Voltar para o Menu", command=self.main_menu)
            back_button.pack(pady=5)
        else:
            messagebox.showerror("Erro", "Contato não encontrado.")

    def show_edit_contact_for_search(self, contact):
        self.clear_screen()
        self.root.title("Editar Contato")

        name_label = tk.Label(self.root, text="Nome:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.insert(0, contact.name)
        self.name_entry.pack()

        phone_label = tk.Label(self.root, text="Telefone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.insert(0, contact.phone)
        self.phone_entry.pack()

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.insert(0, contact.email)
        self.email_entry.pack()

        address_label = tk.Label(self.root, text="Endereço:")
        address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.insert(0, contact.address)
        self.address_entry.pack()

        date_label = tk.Label(self.root, text="Data de Nascimento:")
        date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.insert(0, contact.dateOfBirth)
        self.date_entry.pack()

        save_button = tk.Button(self.root, text="Salvar", command=lambda: self.save_contact_for_search(contact))
        save_button.pack(pady=5)

        cancel_button = tk.Button(self.root, text="Cancelar", command=self.show_search_contact)
        cancel_button.pack(pady=5)

    def save_contact_for_search(self, contact):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        date = self.date_entry.get()

        if self.controller.edit_contact(self.controller.contact_list.contacts.index(contact), name, phone, email, address, date):
            messagebox.showinfo("Sucesso", "Contato editado com sucesso.")
            self.show_search_contact()
        else:
            messagebox.showerror("Erro", "Índice de contato inválido.")

    def confirm_remove_contact_for_search(self, contact):
        confirmation = messagebox.askyesno("Confirmar Remoção", "Tem certeza que deseja remover o contato selecionado?")
        if confirmation:
            if self.controller.remove_contact_by_phone(contact.phone):
                messagebox.showinfo("Sucesso", "Contato removido com sucesso.")
                self.show_search_contact()
            else:
                messagebox.showerror("Erro", "Contato não encontrado.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

def main():
    root = tk.Tk()
    contact_list = ContactList()
    contact_view = ContactView(root, ContactController(contact_list, None))
    contact_view.main_menu()
    root.mainloop()

if __name__ == "__main__":
    main()
