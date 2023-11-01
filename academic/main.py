import tkinter as tk
from tkinter import messagebox
from ementa import Ementa
from disciplina import Disciplina
from curso import Curso

class GerenciadorCursos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Cursos")
        self.cursos = []
        self.current_frame = None

        self.menu_frame = self.create_menu_frame()
        self.show_frame(self.menu_frame)

    def create_menu_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()
        
        menu_label = tk.Label(frame, text="MENU", font=("Arial", 20))
        menu_label.pack()

        adicionar_curso_button = tk.Button(frame, text="1. Adicionar Curso", width=40, command=self.show_add_curso_frame)
        remover_curso_button = tk.Button(frame, text="2. Remover Curso", width=40, command=self.show_remove_curso_frame)
        listar_cursos_button = tk.Button(frame, text="3. Listar Cursos", width=40, command=self.show_list_cursos_frame)
        add_disciplina_button = tk.Button(frame, text="4. Adicionar Disciplina a um Curso", width=40, command=self.show_add_disciplina_frame)
        remove_disciplina_button = tk.Button(frame, text="5. Remover Disciplina de um Curso", width=40, command=self.show_remove_disciplina_frame)
        list_disciplinas_button = tk.Button(frame, text="6. Listar Disciplinas de um Curso", width=40, command=self.show_list_disciplinas_frame)

        adicionar_curso_button.pack()
        remover_curso_button.pack()
        listar_cursos_button.pack()
        add_disciplina_button.pack()
        remove_disciplina_button.pack()
        list_disciplinas_button.pack()

        return frame

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        frame.pack()
        self.current_frame = frame

    def show_add_curso_frame(self):
        frame = self.create_add_curso_frame()
        self.show_frame(frame)

    def create_add_curso_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        codigo_label = tk.Label(frame, text="Código do Curso:")
        nome_label = tk.Label(frame, text="Nome do Curso:")
        codigo_entry = tk.Entry(frame)
        nome_entry = tk.Entry(frame)
        salvar_button = tk.Button(frame, text="Salvar", width=40, command=lambda: self.save_curso(codigo_entry.get(), nome_entry.get()))

        codigo_label.pack()
        codigo_entry.pack()
        nome_label.pack()
        nome_entry.pack()
        salvar_button.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def save_curso(self, codigo, nome):
        curso = Curso(codigo, nome)
        self.cursos.append(curso)
        tk.messagebox.showinfo("Sucesso", f"Curso {curso} adicionado com sucesso.")
        self.show_frame(self.menu_frame)

    def show_remove_curso_frame(self):
        frame = self.create_remove_curso_frame()
        self.show_frame(frame)

    def create_remove_curso_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        codigo_label = tk.Label(frame, text="Digite o código do curso que deseja remover:")
        codigo_entry = tk.Entry(frame)
        remover_button = tk.Button(frame, text="Remover", width=40, command=lambda: self.remove_curso(codigo_entry.get()))

        codigo_label.pack()
        codigo_entry.pack()
        remover_button.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def remove_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                self.cursos.remove(curso)
                tk.messagebox.showinfo("Sucesso", f"Curso {curso} removido com sucesso.")
                self.show_frame(self.menu_frame)
                return
        tk.messagebox.showerror("Erro", f"Curso com código {codigo} não encontrado.")

    def show_list_cursos_frame(self):
        frame = self.create_list_cursos_frame()
        self.show_frame(frame)

    def create_list_cursos_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        if not self.cursos:
            cursos_label = tk.Label(frame, text="Nenhum curso registrado.")
        else:
            cursos_label = tk.Label(frame, text="Cursos registrados:")
            cursos_listbox = tk.Listbox(frame)
            for curso in self.cursos:
                cursos_listbox.insert(tk.END, str(curso))

        cursos_label.pack()
        if self.cursos:
            cursos_listbox.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def show_add_disciplina_frame(self):
        frame = self.create_add_disciplina_frame()
        self.show_frame(frame)

    def create_add_disciplina_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        cursos_label = tk.Label(frame, text="Cursos registrados:")
        cursos_listbox = tk.Listbox(frame)
        for curso in self.cursos:
            cursos_listbox.insert(tk.END, str(curso))
        curso_label = tk.Label(frame, text="Digite o código do curso para adicionar a disciplina:")
        codigo_disciplina_label = tk.Label(frame, text="Digite o código da disciplina:")
        nome_disciplina_label = tk.Label(frame, text="Digite o nome da disciplina:")
        tipo_disciplina_label = tk.Label(frame, text="Digite o tipo da disciplina:")
        periodo_disciplina_label = tk.Label(frame, text="Digite o período:")
        carga_horaria_disciplina_label = tk.Label(frame, text="Digite a carga horária:")
        ementa_disciplina_label = tk.Label(frame, text="Digite a descrição da ementa:")
        codigo_disciplina_entry = tk.Entry(frame)
        nome_disciplina_entry = tk.Entry(frame)
        tipo_disciplina_entry = tk.Entry(frame)
        periodo_disciplina_entry = tk.Entry(frame)
        carga_horaria_disciplina_entry = tk.Entry(frame)
        ementa_disciplina_entry = tk.Entry(frame)

        adicionar_disciplina_button = tk.Button(frame, text="Adicionar Disciplina", width=40, command=lambda: self.add_disciplina(
            cursos_listbox.get(cursos_listbox.curselection()[0]),
            codigo_disciplina_entry.get(),
            nome_disciplina_entry.get(),
            tipo_disciplina_entry.get(),
            periodo_disciplina_entry.get(),
            carga_horaria_disciplina_entry.get(),
            ementa_disciplina_entry.get()
        ))

        cursos_label.pack()
        cursos_listbox.pack()
        curso_label.pack()
        codigo_disciplina_label.pack()
        codigo_disciplina_entry.pack()
        nome_disciplina_label.pack()
        nome_disciplina_entry.pack()
        tipo_disciplina_label.pack()
        tipo_disciplina_entry.pack()
        periodo_disciplina_label.pack()
        periodo_disciplina_entry.pack()
        carga_horaria_disciplina_label.pack()
        carga_horaria_disciplina_entry.pack()
        ementa_disciplina_label.pack()
        ementa_disciplina_entry.pack()
        adicionar_disciplina_button.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def add_disciplina(self, curso_str, codigo, nome, tipo, periodo, carga_horaria, ementa):    
        if curso_str:
            try:
                curso = self.find_curso_by_string(curso_str)
                disciplina = Disciplina(codigo, nome, tipo, periodo, carga_horaria, ementa)
                curso.adicionar_disciplina(disciplina)
                tk.messagebox.showinfo("Sucesso", f"Disciplina {disciplina} adicionada ao curso {curso}.")
                self.show_frame(self.menu_frame)
            except ValueError:
                tk.messagebox.showerror("Erro", "Selecione um curso válido.")
        else:
            tk.messagebox.showerror("Erro", "Selecione um curso para adicionar a disciplina.")

    def find_curso_by_string(self, curso_str):
        for curso in self.cursos:
            if str(curso) == curso_str:
                return curso
        raise ValueError("Curso não encontrado.")

    def show_remove_disciplina_frame(self):
        frame = self.create_remove_disciplina_frame()
        self.show_frame(frame)

    def create_remove_disciplina_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        cursos_label = tk.Label(frame, text="Cursos registrados:")
        cursos_listbox = tk.Listbox(frame)
        for curso in self.cursos:
            cursos_listbox.insert(tk.END, str(curso))
        curso_label = tk.Label(frame, text="Digite o código do curso para remover a disciplina:")
        codigo_disciplina_label = tk.Label(frame, text="Digite o código da disciplina:")
        codigo_disciplina_entry = tk.Entry(frame)
        
        remover_disciplina_button = tk.Button(frame, text="Remover Disciplina", width=40, command=lambda: self.remove_disciplina(
            cursos_listbox.get(cursos_listbox.curselection()),
            codigo_disciplina_entry.get()
        ))

        cursos_label.pack()
        cursos_listbox.pack()
        curso_label.pack()
        codigo_disciplina_label.pack()
        codigo_disciplina_entry.pack()
        remover_disciplina_button.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def remove_disciplina(self, curso_str, codigo_disciplina):
        try:
            curso = self.find_curso_by_string(curso_str)
            for disciplina in curso.listar_disciplinas():
                if disciplina.codigo == codigo_disciplina:
                    curso.remover_disciplina(disciplina)
                    tk.messagebox.showinfo("Sucesso", f"Disciplina {disciplina} removida do curso {curso}.")
                    self.show_frame(self.menu_frame)
                    return
            tk.messagebox.showerror("Erro", f"Disciplina com código {codigo_disciplina} não encontrada.")
        except ValueError:
            tk.messagebox.showerror("Erro", "Selecione um curso válido.")

    def show_list_disciplinas_frame(self):
        frame = self.create_list_disciplinas_frame()
        self.show_frame(frame)

    def create_list_disciplinas_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()

        cursos_label = tk.Label(frame, text="Cursos registrados:")
        cursos_listbox = tk.Listbox(frame)
        for curso in self.cursos:
            cursos_listbox.insert(tk.END, str(curso))
        
        cursos_label.pack()
        cursos_listbox.pack()

        listar_disciplinas_button = tk.Button(frame, text="Listar Disciplinas", width=40, command=lambda: self.show_disciplinas(
            cursos_listbox.get(cursos_listbox.curselection())
        ))

        listar_disciplinas_button.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame

    def show_disciplinas(self, curso_str):
        try:
            curso = self.find_curso_by_string(curso_str)
            disciplinas = curso.listar_disciplinas()
            frame = self.create_disciplinas_frame(curso, disciplinas)
            self.show_frame(frame)
        except ValueError:
            tk.messagebox.showerror("Erro", "Selecione um curso válido.")

    def create_disciplinas_frame(self, curso, disciplinas):
        frame = tk.Frame(self.root)
        frame.pack()

        if not disciplinas:
            disciplinas_label = tk.Label(frame, text=f"Nenhuma disciplina registrada para {curso}.")
        else:
            disciplinas_label = tk.Label(frame, text=f"Disciplinas registradas para {curso}:")

            disciplinas_listbox = tk.Listbox(frame)
            for disciplina in disciplinas:
                disciplinas_listbox.insert(tk.END, str(disciplina))

        disciplinas_label.pack()
        if disciplinas:
            disciplinas_listbox.pack()

        voltar_button = tk.Button(frame, text="Voltar para o MENU", width=40, command=lambda: self.show_frame(self.menu_frame))
        voltar_button.pack()

        return frame


if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorCursos(root)
    root.geometry("800x600")
    root.mainloop()

