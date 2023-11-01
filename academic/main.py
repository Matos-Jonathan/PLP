from ementa import Ementa
from disciplina import Disciplina
from curso import Curso


def criar_ementa(descricao):
    return Ementa(descricao)


def criar_disciplina():
    codigo = input("Digite o código da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    tipo = input("Digite o tipo da disciplina: ")
    #pre_requisitos = input("Digite os pré-requisitos (separados por vírgula): ").split(",")
    periodo = int(input("Digite o período: "))
    carga_horaria = int(input("Digite a carga horária: "))
    ementa = input("Digite a descrição da ementa: ")
    ementa = criar_ementa(ementa)
    return Disciplina(codigo, nome, tipo, periodo, carga_horaria, ementa)


def criar_curso():
    codigo = input("Digite o código do curso: ")
    nome = input("Digite o nome do curso: ")
    return Curso(codigo, nome)


def listar_disciplinas(curso):
    print(f"Disciplinas do curso {curso}:")
    for disciplina in curso.listar_disciplinas():
        print(disciplina)


def main():
    cursos = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Curso")
        print("2. Remover Curso")
        print("3. Listar Cursos")
        print("4. Adicionar Disciplina a um Curso")
        print("5. Remover Disciplina de um Curso")
        print("6. Listar Disciplinas de um Curso")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            curso = criar_curso()
            cursos.append(curso)
            print(f"Curso {curso} adicionado com sucesso.")

        elif escolha == "2":
            codigo_curso = input("Digite o código do curso que deseja remover: ")
            for curso in cursos:
                if curso.codigo == codigo_curso:
                    cursos.remove(curso)
                    print(f"Curso {curso} removido com sucesso.")
                    break
            else:
                print(f"Curso com código {codigo_curso} não encontrado.")

        elif escolha == "3":
            print("\nCursos:")
            for curso in cursos:
                print(curso)

        elif escolha == "4":
            codigo_curso = input("Digite o código do curso para adicionar a disciplina: ")
            for curso in cursos:
                if curso.codigo == codigo_curso:
                    disciplina = criar_disciplina()
                    curso.adicionar_disciplina(disciplina)
                    print(f"Disciplina {disciplina} adicionada ao curso {curso}.")
                    break
            else:
                print(f"Curso com código {codigo_curso} não encontrado.")

        elif escolha == "5":
            codigo_curso = input("Digite o código do curso para remover a disciplina: ")
            for curso in cursos:
                if curso.codigo == codigo_curso:
                    listar_disciplinas(curso)
                    codigo_disciplina = input("Digite o código da disciplina que deseja remover: ")
                    for disciplina in curso.listar_disciplinas():
                        if disciplina.codigo == codigo_disciplina:
                            curso.remover_disciplina(disciplina)
                            print(f"Disciplina {disciplina} removida do curso {curso}.")
                            break
                    else:
                        print(f"Disciplina com código {codigo_disciplina} não encontrada.")
                    break
            else:
                print(f"Curso com código {codigo_curso} não encontrado.")

        elif escolha == "6":
            codigo_curso = input("Digite o código do curso para listar as disciplinas: ")
            for curso in cursos:
                if curso.codigo == codigo_curso:
                    listar_disciplinas(curso)
                    break
            else:
                print(f"Curso com código {codigo_curso} não encontrado.")

        elif escolha == "7":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
