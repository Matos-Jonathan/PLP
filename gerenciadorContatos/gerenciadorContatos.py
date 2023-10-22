class Contact:

  def __init__(self, name, phone):
    self.name = name
    self.phone = phone


class ContactList:

  def __init__(self):
    self.contacts = []

  def add_contact(self, name, phone):
    new_contact = Contact(name, phone)
    self.contacts.append(new_contact)

  def list_contacts(self):
    print("Lista de Contatos:")
    for contact in self.contacts:
      print(f"Nome: {contact.name}, Telefone: {contact.phone}")


def main():
  contact_list = ContactList()

  while True:
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    choice = int(input("Escolha: "))

    if choice == 1:
      name = input("Nome: ")
      phone = input("\nTelefone: ")
      contact_list.add_contact(name, phone)
    elif choice == 2:
      contact_list.list_contacts()
    elif choice == 3:
      break


if __name__ == "__main__":
  main()
