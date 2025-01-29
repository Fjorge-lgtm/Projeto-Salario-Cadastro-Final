import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Application:
    def __init__(self):
        # Criação da janela principal
        self.root = Tk()
        self.tela()
        self.frames_da_tela() # Cria  dois frames (quadros) para organizar os elementos da tela
        self.widgets_frames1() # Adiciona widgets (elementos de interface) no frame superior, como logo, titulo, botões de ação e campos de entrada de dados
        self.lista_frame2() # Cria a Lista (tabela) para exibir os dados dos empregados cadastrados, utilizano o widget Treeview.
        self.conecta_bd()  # Conecta ao banco de dados ao iniciar
        self.atualiza_lista()  # Atualiza a tabela com os dados do banco
        self.root.mainloop()

    def tela(self):
        self.root.title("Sistema de Cadastro de Empregados")
        self.root.configure(background="#FA8072")
        self.root.geometry("1200x900")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        # Frame superior
        self.frame_1 = Frame(self.root, bd=4, bg="#005B1E", highlightbackground="#778899", highlightthickness=8)
        self.frame_1.place(relx=0.01, rely=0.008, relwidth=0.98, relheight=0.65)

        # Frame inferior
        self.frame_2 = Frame(self.root, bd=4, bg="#87CEFA", highlightbackground="#778899", highlightthickness=8)
        self.frame_2.place(relx=0.01, rely=0.66, relwidth=0.98, relheight=0.32)

    def widgets_frames1(self):
        # Adicionar a logo no frame_1
        try:
            self.logo = PhotoImage(file="logo.png")  # Verificar "logo.png" pelo caminho da sua imagem
            self.logo_label = Label(self.frame_1, image=self.logo, bg="#005B1E")
            self.logo_label.place(relx=0.0012, rely=0.0012, relwidth=0.12, relheight=0.42)
        except:
            print("Erro ao carregar a imagem. Certifique-se de que o arquivo 'logo.png' permanece no mesmo diretório.")

        # Título
        self.titulo_label = Label(self.frame_1, text="Sistema de Cadastro de Empregados",
                                  font=("Verdana", 16, "bold"), bg="#005B1E", fg="white")
        self.titulo_label.place(relx=0.15, rely=0.01, relwidth=0.7, relheight=0.1)

        # Botões
        self.bt_limpar = Button(self.frame_1, text="Limpar", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                command=self.limpar_campos)
        self.bt_limpar.place(relx=0.14, rely=0.15, relwidth=0.1, relheight=0.14)

        self.bt_buscar = Button(self.frame_1, text="Buscar", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                command=self.buscar_dados)
        self.bt_buscar.place(relx=0.26, rely=0.15, relwidth=0.1, relheight=0.14)

        self.bt_salvar = Button(self.frame_1, text="Salvar", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                command=self.salvar_dados)
        self.bt_salvar.place(relx=0.5, rely=0.15, relwidth=0.1, relheight=0.14)

        self.bt_alterar = Button(self.frame_1, text="Alterar", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                 command=self.alterar_dados)
        self.bt_alterar.place(relx=0.62, rely=0.15, relwidth=0.1, relheight=0.14)

        self.bt_apagar = Button(self.frame_1, text="Apagar", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                command=self.apagar_dados)
        self.bt_apagar.place(relx=0.74, rely=0.15, relwidth=0.1, relheight=0.14)

        self.bt_imprimir = Button(self.frame_1, text="Imprimir", bg="#1E90FF", fg="white", font=("verdana", 10, "bold"),
                                  command=self.imprimir_listagem)
        self.bt_imprimir.place(relx=0.86, rely=0.15, relwidth=0.1, relheight=0.14)

        # Labels e Entradas
        self.lb_codigo = Label(self.frame_1, text="Código", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_codigo.place(relx=0.02, rely=0.35, relwidth=0.1, relheight=0.1)
        self.input_codigo = Entry(self.frame_1)
        self.input_codigo.place(relx=0.02, rely=0.45, relwidth=0.1, relheight=0.1)

        self.lb_nome = Label(self.frame_1, text="Nome", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_nome.place(relx=0.15, rely=0.35, relwidth=0.1, relheight=0.1)
        self.input_nome = Entry(self.frame_1)
        self.input_nome.place(relx=0.15, rely=0.45, relwidth=0.2, relheight=0.1)

        self.lb_fone = Label(self.frame_1, text="Telefone", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_fone.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.1)
        self.input_fone = Entry(self.frame_1)
        self.input_fone.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)

        self.lb_email = Label(self.frame_1, text="Email", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_email.place(relx=0.65, rely=0.35, relwidth=0.1, relheight=0.1)
        self.input_email = Entry(self.frame_1)
        self.input_email.place(relx=0.65, rely=0.45, relwidth=0.3, relheight=0.1)

        self.lb_cpf = Label(self.frame_1, text="CPF", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_cpf.place(relx=0.02, rely=0.6, relwidth=0.1, relheight=0.1)
        self.input_cpf = Entry(self.frame_1)
        self.input_cpf.place(relx=0.15, rely=0.6, relwidth=0.15, relheight=0.1)

        self.lb_cargo = Label(self.frame_1, text="Cargo", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_cargo.place(relx=0.35, rely=0.6, relwidth=0.1, relheight=0.1)
        self.input_cargo = Entry(self.frame_1)
        self.input_cargo.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.1)

        self.lb_data = Label(self.frame_1, text="Data Admissão", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_data.place(relx=0.75, rely=0.6, relwidth=0.1, relheight=0.1)
        self.input_data = Entry(self.frame_1)
        self.input_data.place(relx=0.88, rely=0.6, relwidth=0.1, relheight=0.1)

        self.lb_salario = Label(self.frame_1, text="Salário", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_salario.place(relx=0.02, rely=0.75, relwidth=0.1, relheight=0.1)
        self.input_salario = Entry(self.frame_1)
        self.input_salario.place(relx=0.15, rely=0.75, relwidth=0.15, relheight=0.1)

        self.lb_endereco = Label(self.frame_1, text="Endereço", font=("verdana", 10, "bold"), bg="#1E90FF", fg="white")
        self.lb_endereco.place(relx=0.35, rely=0.75, relwidth=0.1, relheight=0.1)
        self.input_endereco = Entry(self.frame_1)
        self.input_endereco.place(relx=0.5, rely=0.75, relwidth=0.45, relheight=0.1)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaCli.heading("#1", text="COD")
        self.listaCli.heading("#2", text="NOME")
        self.listaCli.heading("#3", text="TELEFONE")
        self.listaCli.heading("#4", text="EMAIL")
        self.listaCli.heading("#5", text="CPF")
        self.listaCli.heading("#6", text="CARGO")
        self.listaCli.heading("#7", text="DATA")
        self.listaCli.heading("#8", text="SALÁRIO")
        self.listaCli.heading("#9", text="ENDEREÇO")
        self.listaCli["show"] = "headings"
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=120)
        self.listaCli.column("#4", width=120)
        self.listaCli.column("#5", width=100)
        self.listaCli.column("#6", width=155)
        self.listaCli.column("#7", width=110)
        self.listaCli.column("#8", width=80)
        self.listaCli.column("#9", width=280)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def conecta_bd(self):
        self.conn = sqlite3.connect("cadastro.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro (codigo INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT NOT NULL,
            cargo TEXT NOT NULL,
            data_admissao TEXT NOT NULL,
            salario REAL NOT NULL,
            endereco TEXT NOT NULL)""")
        self.conn.commit()

    def salvar_dados(self):
        codigo = self.input_codigo.get()
        nome = self.input_nome.get()
        telefone = self.input_fone.get()
        email = self.input_email.get()
        cpf = self.input_cpf.get()
        cargo = self.input_cargo.get()
        data = self.input_data.get()
        salario = self.input_salario.get()
        endereco = self.input_endereco.get()

        if all([codigo, nome, telefone, email, cpf, cargo, data, salario, endereco]):
            self.cursor.execute("""
            INSERT INTO cadastro (codigo, nome, telefone, email, cpf, cargo, data_admissao, salario, endereco)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (codigo, nome, telefone, email, cpf, cargo, data, salario, endereco))
            self.conn.commit()
            self.atualiza_lista()
            self.limpar_campos()
        else:
            messagebox.showinfo("Erro", "Preencha todos os campos!")

    def buscar_dados(self):
        nome_busca = self.input_nome.get()
        self.cursor.execute("SELECT * FROM cadastro WHERE nome LIKE ?", (f"%{nome_busca}%",))
        resultados = self.cursor.fetchall()
        self.listaCli.delete(*self.listaCli.get_children())
        for row in resultados:
            self.listaCli.insert("", "end", values=row)

    def alterar_dados(self):
        item_selecionado = self.listaCli.selection()
        if item_selecionado:
            valores = self.listaCli.item(item_selecionado, "values")
            codigo = valores[0]
            nome = self.input_nome.get()
            telefone = self.input_fone.get()
            email = self.input_email.get()
            cpf = self.input_cpf.get()
            cargo = self.input_cargo.get()
            data = self.input_data.get()
            salario = self.input_salario.get()
            endereco = self.input_endereco.get()

            self.cursor.execute("""UPDATE cadastro SET nome = ?, telefone = ?, email = ?, cpf = ?, cargo = ?, data_admissao = ?, salario = ?, endereco = ?
            WHERE codigo = ?""", (nome, telefone, email, cpf, cargo, data, salario, endereco, codigo))
            self.conn.commit()
            self.atualiza_lista()
            self.limpar_campos()
        else:
            messagebox.showinfo("Erro", "Selecione um registro para alterar!")

    def apagar_dados(self):
        item_selecionado = self.listaCli.selection()
        if item_selecionado:
            valores = self.listaCli.item(item_selecionado, "values")
            codigo = valores[0]
            self.cursor.execute("DELETE FROM cadastro WHERE codigo = ?", (codigo,))
            self.conn.commit()
            self.atualiza_lista()
        else:
            messagebox.showinfo("Erro", "Selecione um registro para apagar!")

    def atualiza_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.cursor.execute("SELECT * FROM cadastro")
        for row in self.cursor.fetchall():
            self.listaCli.insert("", "end", values=row)

    def limpar_campos(self):
        self.input_codigo.delete(0, END)
        self.input_nome.delete(0, END)
        self.input_fone.delete(0, END)
        self.input_email.delete(0, END)
        self.input_cpf.delete(0, END)
        self.input_cargo.delete(0, END)
        self.input_data.delete(0, END)
        self.input_salario.delete(0, END)
        self.input_endereco.delete(0, END)

    def imprimir_listagem(self):
        self.cursor.execute("SELECT * FROM cadastro")
        registros = self.cursor.fetchall()
        if registros:
            with open("listagem.txt", "w") as arquivo:
                arquivo.write("Listagem de Cadastro\n")
                arquivo.write("=" * 50 + "\n")
                for registro in registros:
                    linha = (f"Código: {registro[0]} | Nome: {registro[1]} | Telefone: {registro[2]} | "
                             f"Email: {registro[3]} | CPF: {registro[4]} | Cargo: {registro[5]} | "
                             f"Data: {registro[6]} | Salário: {registro[7]} | Endereço: {registro[8]}\n")
                    arquivo.write(linha)
                arquivo.write("=" * 50 + "\n")
            messagebox.showinfo("Imprimir", "Listagem exportada com sucesso para 'listagem.txt'.")
        else:
            messagebox.showwarning("Imprimir", "Não há registros para exportar.")


Application()