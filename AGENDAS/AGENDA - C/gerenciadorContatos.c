#include <stdio.h>
#include <string.h>

struct Contact
{
    char name[50];
    char phone[15];
    char address[100];
    char email[50];
    char dateOfBirth[15];
};

void clearBuffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
        ;
}

void addContact(struct Contact contacts[], int *count)
{
    struct Contact newContact;

    printf("Adicionar um novo contato:\n");

    printf("Nome: ");
    fgets(newContact.name, sizeof(newContact.name), stdin);
    newContact.name[strcspn(newContact.name, "\n")] = '\0'; // Remove a quebra de linha

    printf("Telefone: ");
    fgets(newContact.phone, sizeof(newContact.phone), stdin);
    newContact.phone[strcspn(newContact.phone, "\n")] = '\0';

    printf("Endereço: ");
    fgets(newContact.address, sizeof(newContact.address), stdin);
    newContact.address[strcspn(newContact.address, "\n")] = '\0';

    printf("Email: ");
    fgets(newContact.email, sizeof(newContact.email), stdin);
    newContact.email[strcspn(newContact.email, "\n")] = '\0';

    printf("Data de Nascimento: ");
    fgets(newContact.dateOfBirth, sizeof(newContact.dateOfBirth), stdin);
    newContact.dateOfBirth[strcspn(newContact.dateOfBirth, "\n")] = '\0';

    contacts[(*count)++] = newContact;
}

void listContacts(struct Contact contacts[], int count)
{
    printf("Lista de Contatos:\n");
    for (int i = 0; i < count; i++)
    {
        printf("Nome: %s\nTelefone: %s\nEndereço: %s\nEmail: %s\nData de Nascimento: %s\n",
               contacts[i].name, contacts[i].phone, contacts[i].address, contacts[i].email, contacts[i].dateOfBirth);
    }
}

void saveContactsToFile(struct Contact contacts[], int count)
{
    FILE *file = fopen("contactsC.txt", "w");
    if (file == NULL)
    {
        perror("Erro ao abrir o arquivo");
        return;
    }

    for (int i = 0; i < count; i++)
    {
        fprintf(file, "%s\n%s\n%s\n%s\n%s\n", contacts[i].name, contacts[i].phone, contacts[i].address, contacts[i].email, contacts[i].dateOfBirth);
    }

    fclose(file);
    printf("Contatos salvos no arquivo 'contactsC.txt'\n");
}

int loadContactsFromFile(struct Contact contacts[], int *count)
{
    FILE *file = fopen("contatosC.txt", "r");
    if (file == NULL)
    {
        perror("Erro ao abrir o arquivo");
        return 0;
    }

    while (*count < 100 && fscanf(file, " %[^\n]\n %[^\n]\n %[^\n]\n %[^\n]\n %[^\n]\n",
                                  contacts[*count].name, contacts[*count].phone, contacts[*count].address,
                                  contacts[*count].email, contacts[*count].dateOfBirth) == 5)
    {
        (*count)++;
    }

    fclose(file);
    return 1;
}

void editContact(struct Contact contacts[], int count)
{
    char searchPhone[50];
    printf("Digite o número do contato que você deseja editar: ");
    fgets(searchPhone, sizeof(searchPhone), stdin);
    searchPhone[strcspn(searchPhone, "\n")] = '\0';

    int found = 0;
    int i;
    for (i = 0; i < count; i++)
    {
        if (strcmp(contacts[i].phone, searchPhone) == 0)
        {
            found = 1;
            printf("Contato encontrado. Você pode editar as informações:\n");

            printf("Novo nome: ");
            fgets(contacts[i].name, sizeof(contacts[i].name), stdin);
            contacts[i].name[strcspn(contacts[i].name, "\n")] = '\0';

            printf("Novo telefone: ");
            fgets(contacts[i].phone, sizeof(contacts[i].phone), stdin);
            contacts[i].phone[strcspn(contacts[i].phone, "\n")] = '\0';

            printf("Novo Endereço: ");
            fgets(contacts[i].address, sizeof(contacts[i].address), stdin);
            contacts[i].address[strcspn(contacts[i].address, "\n")] = '\0';

            printf("Novo Email: ");
            fgets(contacts[i].email, sizeof(contacts[i].email), stdin);
            contacts[i].email[strcspn(contacts[i].email, "\n")] = '\0';

            printf("Nova Data de Nascimento: ");
            fgets(contacts[i].dateOfBirth, sizeof(contacts[i].dateOfBirth), stdin);
            contacts[i].dateOfBirth[strcspn(contacts[i].dateOfBirth, "\n")] = '\0';

            printf("Contato editado com sucesso!\n");
            break;
        }
    }

    if (!found)
    {
        printf("Contato não encontrado.\n");
    }
}

void removeContact(struct Contact contacts[], int *count)
{
    char searchName[50];
    printf("Digite o nome do contato que deseja remover: ");
    fgets(searchName, sizeof(searchName), stdin);
    searchName[strcspn(searchName, "\n")] = '\0';

    int found = 0;
    for (int i = 0; i < *count; i++)
    {
        if (strcmp(contacts[i].name, searchName) == 0)
        {
            found = 1;

            for (int j = i; j < *count - 1; j++)
            {
                contacts[j] = contacts[j + 1];
            }
            (*count)--;
            printf("Contato removido com sucesso!\n");
            break;
        }
    }

    if (!found)
    {
        printf("Contato não encontrado.\n");
    }
}

void searchContact(struct Contact contacts[], int count)
{
    char searchPhone[15];
    printf("Digite o número de telefone do contato que deseja buscar: ");
    fgets(searchPhone, sizeof(searchPhone), stdin);
    searchPhone[strcspn(searchPhone, "\n")] = '\0';

    int found = 0;
    for (int i = 0; i < count; i++)
    {
        if (strcmp(contacts[i].phone, searchPhone) == 0)
        {
            found = 1;
            printf("Nome: %s\nTelefone: %s\nEmail: %s\nData de Nascimento: %s\n",
                   contacts[i].name, contacts[i].phone, contacts[i].email, contacts[i].dateOfBirth);
            break;
        }
    }

    if (!found)
    {
        printf("Contato não encontrado pelo número de telefone.\n");
    }
}

int main()
{
    struct Contact contacts[100];
    int count = 0;
    int choice;

    // Carregar contatos do arquivo, se existirem
    if (loadContactsFromFile(contacts, &count))
    {
        printf("Contatos carregados do arquivo 'contatosC.txt'\n");
    }

    do
    {
        printf("1. Adicionar Contato\n");
        printf("2. Listar Contatos\n");
        printf("3. Editar contato\n");
        printf("4. Remover Contato\n");
        printf("5. Buscar Contato\n");
        printf("6. Sair\n");
        printf("Escolha: ");
        scanf("%d", &choice);
        clearBuffer(); // Limpar o buffer após a leitura de 'choice'

        switch (choice)
        {
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
            break;
        }

    } while (choice != 6);

    // Salvar contatos no arquivo ao sair
    saveContactsToFile(contacts, count);

    return 0;
}
