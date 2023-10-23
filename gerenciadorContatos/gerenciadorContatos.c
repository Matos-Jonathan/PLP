#include <stdio.h>
#include <string.h>
struct Contact {
  char name[50];
  char phone[15];
  char address[100]; // Aumentei o tamanho do campo do endereço
  char email[50];    // Aumentei o tamanho do campo do email
  char dateOfBirth[15];
};

void clearBuffer() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF);
}

void addContact(struct Contact contacts[], int *count) {
  struct Contact newContact;
  
  printf("Adicionar novo contato:\n");
  
  printf("Nome: ");
  fgets(newContact.name, sizeof(newContact.name), stdin);
  newContact.name[strcspn(newContact.name, "\n")] = '\0'; // Remover a quebra de linha
  
  printf("Telefone: ");
  fgets(newContact.phone, sizeof(newContact.phone), stdin);
  newContact.phone[strcspn(newContact.phone, "\n")] = '\0'; // Remover a quebra de linha
  
  printf("Endereço: ");
  fgets(newContact.address, sizeof(newContact.address), stdin);
  newContact.address[strcspn(newContact.address, "\n")] = '\0'; // Remover a quebra de linha
  
  printf("Email: ");
  fgets(newContact.email, sizeof(newContact.email), stdin);
  newContact.email[strcspn(newContact.email, "\n")] = '\0'; // Remover a quebra de linha
  
  printf("Data de Nascimento: ");
  fgets(newContact.dateOfBirth, sizeof(newContact.dateOfBirth), stdin);
  newContact.dateOfBirth[strcspn(newContact.dateOfBirth, "\n")] = '\0'; // Remover a quebra de linha
  
  contacts[(*count)++] = newContact;
}

void listContacts(struct Contact contacts[], int count) {
  printf("Lista de Contatos:\n");
  for (int i = 0; i < count; i++) {
    printf("Nome: %s\n Telefone: %s\n Endereço: %s\n Email: %s\n Data de Nascimento: %s\n", contacts[i].name, contacts[i].phone, contacts[i].address, contacts[i].email, contacts[i].dateOfBirth );
  }
}

void editContact(struct Contact contacts[], int count){
  char searchPhone[50];
  printf("Digite o número do contato que você deseja editar: ");
  scanf("%s", searchPhone);

  int found = 0;
  int i;
  for(i = 0; i < count; i++){
    if(strcmp(contacts[i].phone, searchPhone) == 0){
      found = 1;
      printf("Novo nome: ");
      scanf("%s", contacts[i].name);
      printf("Novo telefone: ");
      scanf("%s", contacts[i].phone);
      printf("Novo Endereço: ");
      scanf("%s", contacts[i].address);
      printf("Novo Email: ");
      scanf("%s", contacts[i].email);
      printf("Nova Data de Nascimento: ");
      scanf("%s", contacts[i].dateOfBirth);
      printf("Contato editado com sucesso!\n");
      break;
    }
  }

  if(!found){
    printf("Contato não encontrado.\n");
  }
}

void removeContact(struct Contact contacts[], int *count) {
  char searchName[50];
  printf("Digite o nome do contato que deseja remover: ");
  scanf("%s", searchName);

  int found = 0;
  for (int i = 0; i < *count; i++) {
    if (strcmp(contacts[i].name, searchName) == 0) {
      found = 1;

      for (int j = i; j < *count - 1; j++) {
        contacts[j] = contacts[j + 1];
      }
      (*count)--;
      printf("Contato removido com sucesso!\n");
      break;
    }
  }

  if (!found) {
    printf("Contato não encontrado.\n");
  }
}

void searchContact(struct Contact contacts[], int count) {
  char searchPhone[15];
  printf("Digite o número de telefone do contato que deseja buscar: ");
  scanf("%s", searchPhone);

  int found = 0;
  for (int i = 0; i < count; i++) {
    if (strcmp(contacts[i].phone, searchPhone) == 0) {
      found = 1;
      printf("Nome: %s\n", contacts[i].name);
      printf("Telefone: %s\n", contacts[i].phone);
      printf("Email: %s\n", contacts[i].email);
      printf("Data de Nascimento: %s\n", contacts[i].dateOfBirth);
      break;
    }
  }

  if (!found) {
    printf("Contato não encontrado pelo número de telefone.\n");
  }
}


int main() {
  struct Contact contacts[100];
  int count = 0;
  int choice;

  do {
    printf("1. Adicionar Contato\n");
    printf("2. Listar Contatos\n");
    printf("3. Editar contato\n");
    printf("4. Remover Contato\n");
    printf("5. Buscar Contato\n");
    printf("6. Sair\n");
    printf("Escolha: ");
    scanf("%d", &choice);

    switch (choice) {
    case 1:
      addContact(contacts, &count);
      break;
    case 2:
      listContacts(contacts, count);
      break;
    case 3:
      editContact(contacts, count);
      break;
    case 4:
     removeContact(contacts, &count);
     break;
    case 5:
      searchContact(contacts, count);
    }
  } while (choice != 6);

  return 0;
}
