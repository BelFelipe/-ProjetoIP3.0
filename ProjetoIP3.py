from tkinter import *
import sqlite3
from tkinter import messagebox

class interface:
    def __init__(self, master):
        #=====================================FRAME PRINCIPAL==============================
        self.frame_principal = Frame(master, width=800, height=600)
        self.frame_principal.place(x=0, y=0)
        self.frame_principal['bg'] = 'azure2'
        Label(self.frame_principal, font=25, text='Menu Principal', bg='azure2', fg='grey20').place(x=350, y=0)
        #=====================================FRAME ALUNO===================================
        self.frame_aluno = Frame(master, width=800, height=600)
        self.frame_aluno.place(x=0, y=3000)
        self.frame_aluno['bg'] = 'azure2'
        self.lb_menu_aluno = Label(self.frame_aluno, text='Menu Aluno(s)', fg='grey20', bg='azure2', font=25).place(x=350, y=0)
        #=====================================FRAME PROFESSOR==================================
        self.frame_professor = Frame(master, width=800, height=600)
        self.frame_professor.place(x=0, y=3000)
        self.frame_professor['bg'] = 'azure2'
        Label(self.frame_professor, text='Menu do Professor', fg='grey20', bg='azure2', font=25).place(x=350, y=0)
        #=====================================FRAME DE TODOS ALUNOS============================
        self.frame_disciplina = Frame(master, width=800, height=600)
        self.frame_disciplina.place(x=0, y=3000)
        self.frame_disciplina['bg'] = "azure2"
        Label(self.frame_disciplina, text='Menu de Disciplina', fg='grey20', bg='azure2', font=25).place(x=350, y=0)
        #=====================================FRAME DE TURMAS=================================
        self.frame_turmas = Frame(master, width=800, height=600)
        self.frame_turmas.place(x=0, y=3000)
        self.frame_turmas['bg'] = "azure2"
        Label(self.frame_turmas, text='Menu de Turmas', fg= "grey20", bg="azure2", font=25).place(x=350, y=0)

        btn0  = Button(self.frame_principal,  width=15, height=2, text='Aluno(s)',        fg='black', command=self.troca_frame_aluno).place(x=10, y=50)  # redirecionamento para frame ALUNO
        btn1  = Button(self.frame_principal,  width=15, height=2, text='Professor',       fg='black', command=self.troca_frame_professor).place(x=10, y=100)
        btn2  = Button(self.frame_aluno,      width=15, height=2, text='Voltar',          fg='black', command=self.voltar_principalA).place(x=10,y=10)  # Botão para voltar Menu Principal
        btn3  = Button(self.frame_professor,  width=15, height=2, text='Voltar',          fg='black', command=self.voltar_principalP).place(x=10, y=10)  # Botão para voltar Menu Principal
        btnv  = Button(self.frame_disciplina, width=15, height=2, text="Voltar",          fg='black', command=self.voltar_principalD).place(x=10, y=10)
        btnvt = Button(self.frame_turmas,     width=15, height=2, text="Voltar",          fg="black", command=self.voltar_principalT).place(x=10, y=10)
        btn6  = Button(self.frame_aluno,      width=15, height=2, text='Modificar',       fg='black', command=self.Modificar_aluno).place(x=10,y=200)  # Modificação de Aluno
        btn7  = Button(self.frame_aluno,      width=15, height=2, text='Adicionar',       fg='black', command=self.cadastro_aluno).place(x=10,y=150)  # Cadastrar aluno
        btn8  = Button(self.frame_aluno,      width=15, height=2, text='Exclusão',        fg='black', command=self.exclusao_aluno).place(x=10, y=250)
        btn9  = Button(self.frame_aluno,      width=15, height=2, text='Buscar',          fg='black', command=self.buscar_aluno).place(x=10, y=100)
        btn10 = Button(self.frame_professor,  width=15, height=2, text='Modificar',       fg='black', command=self.Modificar_professor).place(x=10,y=200)  # Modificação de Professor
        btn11 = Button(self.frame_professor,  width=15, height=2, text='Adicionar',       fg='black', command=self.cadastro_professor).place(x=10,y=150)  # Cadastrar Professor
        btn12 = Button(self.frame_professor,  width=15, height=2, text='Exclusão',        fg='black', command=self.exclusao_professor).place(x=10, y=250)  #Exclusão de Professores
        btn13 = Button(self.frame_professor,  width=15, height=2, text='Buscar',          fg='black', command=self.buscar_professor).place(x=10, y=100)   #Busca de dados de professores
        btnD  = Button(self.frame_principal,  width=15, height=2, text="Disciplina",      fg='black', command=self.troca_frame_disciplina).place(x=10, y=150)
        btn14 = Button(self.frame_disciplina, width=15, height=2, text='Modificar',       fg='black', command=self.painel_mod_disciplina).place(x=10, y=200)  # Modificação de disciplina
        btn15 = Button(self.frame_disciplina, width=15, height=2, text='Adicionar',       fg='black', command=self.cadastro_disciplina).place(x=10, y=150)  # Cadastrar disciplina
        btn16 = Button(self.frame_disciplina, width=15, height=2, text='Exclusão',        fg='black', command=self.exclusao_disciplina).place(x=10, y=250)  # Exclusão de disciplina
        btn17 = Button(self.frame_disciplina, width=15, height=2, text='Buscar',          fg='black', command=self.buscar_disciplina).place(x=10, y=100)  # Busca de dados de disciplina
        btnT  = Button(self.frame_principal,  width=15, height=2, text="Turmas",          fg='black', command=self.troca_frame_turma).place(x=10, y=200)
        btn18 = Button(self.frame_turmas,     width=15, height=2, text='Modificar',       fg='black', command=self.inicio_modificar_turmas).place(x=10, y=250)  # Modificação de disciplina
        btn19 = Button(self.frame_turmas,     width=15, height=2, text='Adicionar',       fg='black', command=self.cadastro_turmas).place(x=10, y=150)  # Cadastrar disciplina
        btn20 = Button(self.frame_turmas,     width=15, height=2, text='Exclusão',        fg='black', command=self.exclusao_turmas).place(x=10, y=300)  # Exclusão de disciplina
        btn21 = Button(self.frame_turmas,     width=15, height=2, text='Buscar',          fg='black', command=self.buscar_turmas).place(x=10, y=100)
        Button(self.frame_turmas,             width=15, height=2, text="Adicionar Aluno", fg='black', command=self.cadastrar_aluno_turma).place(x=10, y=200)

    def confirmacao_aluno(self):  #FUNÇÃO PARA COMPILAR OS DADOS DOS CAMPOS E ENTREGAR UMA LISTA PARA ARMAZENAMENTO OU EXCLUSÃO
        nome = self.nome.get()
        cpf = self.cpf.get()
        dados = [cpf, nome]
        verificar_cpf_aluno(dados)
    def confirmacao_aluno_exclusao(self):
        cpf = self.cpf.get()
        dados = cpf
        verificarEexclusao_cpf_aluno(dados)

    #Alteração de Frames, Entrada em MENUS
    def troca_frame_turma(self):
        self.frame_turmas.place(x=0,y=0)
        self.frame_principal.place(x=0, y=3000)
    def troca_frame_aluno(self):
        self.frame_principal.place(x=0, y=3000)
        self.frame_aluno.place(x=0,y=0)
    def troca_frame_professor(self):
        self.frame_principal.place(x=0,y=3000)
        self.frame_professor.place(x=0,y=0)
    def troca_frame_disciplina(self):
        self.frame_disciplina.place(x=0, y=0)
        self.frame_principal.place(x=0, y=3000)
    def voltar_principalA(self):
        Label(self.frame_aluno, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        self.frame_aluno.place(x=0,y=3000)
        self.frame_principal.place(x=0,y=0)
    def voltar_principalP(self):
        Label(self.frame_professor, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        self.frame_professor.place(x=0, y=3000)
        self.frame_principal.place(x=0,y=0)
    def voltar_principalD(self):
        Label(self.frame_disciplina, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        self.frame_disciplina.place(x=0, y=3000)
        self.frame_principal.place(x=0, y=0)
    def voltar_principalT(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        self.frame_principal.place(x=0, y=0)
        self.frame_turmas.place(x=0, y=3000)

    #MODIFICAÇÃO PARA ALUNO
    def Modificar_aluno(self):
        Label(self.frame_aluno, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_aluno, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_aluno, text='CPF:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.cpf_busca_mod = Entry(self.frame_aluno, width=15)
        self.cpf_busca_mod.place(x=255, y=70)
        Button(self.frame_aluno, text="Buscar", width=15, height=1, command=self.confirm_modificar).place(x=400, y=66)
    def nova_entrada_aluno(self):
        global cpf_mod
        Label(self.frame_aluno,bg='azure2',fg='grey20', text="Nome:").place(x=200,y=190)
        self.novo_nome_aluno = Entry(self.frame_aluno, width=30)
        self.novo_nome_aluno.place(x=250, y=190)
        cpf_mod = self.cpf_busca_mod.get()
        Label(self.frame_aluno, text="CPF:", bg='azure2', fg='grey20').place(x=200, y=160)
        Label(self.frame_aluno,text="{}".format(cpf_mod)).place(x=250, y=160)
        Button(self.frame_aluno, text="Alterar", fg='grey20', bg='azure2', command=self.recebe_novo_nome_aluno).place(x=390, y=160)
    def recebe_novo_nome_aluno(self):
        novo_nome = self.novo_nome_aluno.get()
        connect = sqlite3.connect('Database.db')
        cursor = connect.cursor()
        cursor.execute("update aluno set Nome = '{}' where CPF = '{}'".format(novo_nome, cpf_mod))
        messagebox.showinfo("Informativo", "Atualização feita com sucesso!")
        cursor.close()
        connect.commit()
        connect.close()
    def confirm_modificar(self):
        cpf = self.cpf_busca_mod.get()
        modificar_dados(cpf)
    #==========================================
    #BUSCA ALUNO E MOSTRAR TODOS NA ABA DE BUSCA
    def buscar_aluno(self):
        Label(self.frame_aluno, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_aluno, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_aluno, text='CPF:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.listbox = Listbox(self.frame_aluno, width=95, height=26)
        self.listbox.place(x=180, y=130)
        self.cpf_busca = Entry(self.frame_aluno, width=15)
        self.cpf_busca.place(x=255, y=70)
        Button(self.frame_aluno,text="Buscar" , width=15, height=1, command=self.click_da_busca).place(x=400, y=66)
        Button(self.frame_aluno,text="mostrar todos", width=15, height=1, command=self.mostrar_todos).place(x=530, y=66)
    def click_da_busca(self):
        cpf = str(self.cpf_busca.get())
        self.Database_buscas = cpf
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from aluno where CPF = '{}'".format(cpf))
        Database = cursor.fetchone()
        self.listbox.delete(0, END)
        self.listbox.insert(END, Database)
        cursor.close()
        conexao.close()
    def mostrar_todos(self):
        self.listbox.delete(0, END)
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from aluno")
        Database = cursor.fetchall()
        self.listbox.insert(END, "       CPF         | Nome")
        for x in Database:
            self.listbox.insert(END, x)
        cursor.close()
        conexao.close()
    def cadastro_aluno(self):
        Label(self.frame_aluno, width=600, height=550, bg='azure2').place(x=140,y=35) #Da clear na função anterior na tela
        Label(self.frame_aluno, relief=SUNKEN, width=80, height=7, bg='azure2').place(x=190, y=80)
        Label(self.frame_aluno, text='Adicionar Aluno', font=15, bg='azure2', fg='grey20').place(x=410, y=61)
        Label(self.frame_aluno, text='Nome:', bg='azure2', fg='grey20').place(x=200, y=90)
        Label(self.frame_aluno, text='CPF:', bg='azure2', fg='grey20').place(x=200, y=120)
        Label(self.frame_aluno, text='O CPF deve conter 11 números;\nNenhuma letra nem caracteres invalidos.', bg='gray80',fg='grey20').place(x=520, y=120)
        self.nome = Entry(self.frame_aluno, width=40)
        self.nome.place(x=245, y=90)
        self.cpf = Entry(self.frame_aluno, width=15)
        self.cpf.place(x=245, y=120)
        Button(self.frame_aluno, width=8, height=1, text='Confirmar', command=self.confirmacao_aluno).place(x=250, y=150)
    def exclusao_aluno(self):
        Label(self.frame_aluno, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_aluno, relief=SUNKEN, width=80, height=3, bg='azure2').place(x=190, y=80)
        Label(self.frame_aluno, text='Exclusão de Aluno', font=15, bg='azure2', fg='grey20').place(x=400, y=61)
        Label(self.frame_aluno, text='CPF:', bg='azure2', fg='grey20').place(x=200, y=95)
        self.cpf = Entry(self.frame_aluno, width=15)
        self.cpf.place(x=245, y=97)
        Button(self.frame_aluno, width=8 ,height=1, text='Confirmar',command=self.confirmacao_aluno_exclusao).place(x=350, y=95)
    #FUNÇÕES MENU DE PROFESSOR
    def Modificar_professor(self):  #Informativo na hora de mudar os dados
        Label(self.frame_professor, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_professor, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_professor, text='CPF:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.cpf_prof_mod = Entry(self.frame_professor, width=15)
        self.cpf_prof_mod.place(x=255, y=70)
        Button(self.frame_professor, text="Buscar", width=15, height=1, command=self.modificar_dados_prof).place(x=400, y=66)
    def modificar_dados_prof(self):
        cpf = str(fun.cpf_prof_mod.get())
        if len(cpf) != 11 or cpf.isnumeric() == False:
            messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
            return
        connect = sqlite3.connect('Database.db')
        cursor = connect.cursor()
        cursor.execute("select * from professor where CPF = '{}'".format(cpf))
        Database = cursor.fetchone()
        if Database != None:
            Label(fun.frame_professor, bg='azure2', fg='grey20', text="Nome:").place(x=200, y=190)
            Label(fun.frame_professor, bg='azure2', fg='grey20', text="Depart.").place(x=200, y=220)
            self.novo_nome_prof = Entry(fun.frame_professor, width=30)
            self.novo_nome_prof.place(x=250, y=190)
            self.novo_dep = Entry(fun.frame_professor, width=15)
            self.novo_dep.place(x=250, y=220)
            Label(fun.frame_professor, text="CPF:", bg='azure2', fg='grey20').place(x=200, y=160)
            Label(fun.frame_professor, text="{}".format(cpf)).place(x=250, y=160)
            Button(fun.frame_professor, text="Alterar", fg='grey20', bg='azure2', command=self.update_prof).place(x=390, y=160)
        else:
            messagebox.showinfo("Aviso", "Nenhum cadastro feito com esse CPF!")
        cursor.close()
        connect.close()
    def update_prof(self):
        cpf = str(fun.cpf_prof_mod.get())
        nome = self.novo_nome_prof.get()
        dep = self.novo_dep.get()
        connect = sqlite3.connect("Database.db")
        cursor = connect.cursor()
        cursor.execute("update professor set Nome = '{}', Departamento = '{}'  where CPF = '{}'".format(nome,dep,cpf))
        messagebox.showinfo("Aviso!", "Dados alterados com sucesso!")
        connect.commit()
        cursor.close()
        connect.close()
    def cadastro_professor(self):
        Label(self.frame_professor, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_professor, relief=SUNKEN, width=80, height=7, bg='azure2').place(x=190, y=80)
        Label(self.frame_professor, text='Adicionar Professor', font=15, bg='azure2', fg='grey20').place(x=410, y=61)
        Label(self.frame_professor, text='Nome:', bg='azure2', fg='grey20').place(x=200, y=90)
        Label(self.frame_professor, text='CPF:', bg='azure2', fg='grey20').place(x=200, y=120)
        Label(self.frame_professor, text="Departamento:", bg='azure2', fg='grey20').place(x=200, y=150)
        Label(self.frame_professor, text='O CPF deve conter 11 números;\nNenhuma letra nem caracteres invalidos.',bg='gray80', fg='grey20').place(x=520, y=120)
        self.nome_prof = Entry(self.frame_professor, width=40)
        self.nome_prof.place(x=285, y=90)
        self.cpf_prof = Entry(self.frame_professor, width=15)
        self.cpf_prof.place(x=285, y=120)
        self.departamento = Entry(self.frame_professor, width=20)
        self.departamento.place(x=285, y=150)
        Button(self.frame_professor, width=8, height=1, text='Confirmar', command=adicionar_professor_db).place(x=440,y=148)
    def exclusao_professor(self):
        Label(self.frame_professor, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_professor, relief=SUNKEN, width=80, height=3, bg='azure2').place(x=190, y=80)
        Label(self.frame_professor, text='Exclusão de Professor', font=15, bg='azure2', fg='grey20').place(x=400, y=61)
        Label(self.frame_professor, text='CPF:', bg='azure2', fg='grey20').place(x=200, y=95)
        self.cpf_exclusao = Entry(self.frame_professor, width=15)
        self.cpf_exclusao.place(x=245, y=97)
        Button(self.frame_professor, width=8, height=1, text='Confirmar', command=exclusao_professor).place(x=350, y=95)
    def buscar_professor(self):
        Label(self.frame_professor, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_professor, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_professor, text='CPF:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.listbox_prof = Listbox(self.frame_professor, width=95, height=26)
        self.listbox_prof.place(x=180, y=130)
        self.cpf_busca_prof = Entry(self.frame_professor, width=15)
        self.cpf_busca_prof.place(x=255, y=70)
        Button(self.frame_professor, text="Buscar", width=15, height=1, command=mostrarBusca_cpf_professor).place(x=400, y=66)
        Button(self.frame_professor, text="mostrar todos", width=15, height=1, command=self.mostrar_tudo_prof).place(x=530,y=66)
    def mostrar_tudo_prof(self):
        self.listbox_prof.delete(0, END)
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from professor")
        Database = cursor.fetchall()
        if Database == []:
            messagebox.showinfo("Erro", "Não há nenhum dado cadastrado!")
        self.listbox_prof.insert(END, "CPF  | Nome | Departamento")
        for x in Database:
            self.listbox_prof.insert(END, x)
    #FUNÇÕES MENU DISCIPLINA
    def cadastro_disciplina(self):
        Label(self.frame_disciplina, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_disciplina, relief=SUNKEN, width=80, height=7, bg='azure2').place(x=190, y=80)
        Label(self.frame_disciplina, text='Adicionar Disciplina', font=15, bg='azure2', fg='grey20').place(x=410, y=61)
        Label(self.frame_disciplina, text='Nome:', bg='azure2', fg='grey20').place(x=200, y=90)
        Label(self.frame_disciplina, text='Código:', bg='azure2', fg='grey20').place(x=200, y=120)
        self.nome_disciplina = Entry(self.frame_disciplina, width=40)
        self.nome_disciplina.place(x=285, y=90)
        self.codigo_disciplina = Entry(self.frame_disciplina, width=15)
        self.codigo_disciplina.place(x=285, y=120)
        Button(self.frame_disciplina, width=8, height=1, text='Confirmar', command=adicionar_disciplina_db).place(x=440,y=148)
    def buscar_disciplina(self):
        Label(self.frame_disciplina, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_disciplina, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_disciplina, text='Codigo:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.listbox_disci = Listbox(self.frame_disciplina, width=95, height=26)
        self.listbox_disci.place(x=180, y=130)
        self.codigo_disciplina_bus = Entry(self.frame_disciplina, width=15)
        self.codigo_disciplina_bus.place(x=255, y=70)
        Button(self.frame_disciplina, text="Buscar", width=15, height=1, command=mostrarBuscar_codigo_dis).place(x=400,y=66)
        Button(self.frame_disciplina, text="mostrar todos", width=15, height=1, command=self.mostrar_todos_dis).place(x=530, y=66)
    def mostrar_todos_dis(self):
        self.listbox_disci.delete(0, END)
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from disciplina")
        Database = cursor.fetchall()
        if Database == []:
            messagebox.showinfo("Erro", "Não há nenhum dado cadastrado!")
        self.listbox_disci.insert(END, "       Nome        | Codigo")
        for x in Database:
            self.listbox_disci.insert(END, x)
    def painel_mod_disciplina(self):
        Label(self.frame_disciplina, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_disciplina, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_disciplina, text='Codigo:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.codigo_disciplina_mod = Entry(self.frame_disciplina, width=15)
        self.codigo_disciplina_mod.place(x=255, y=70)
        Button(self.frame_disciplina, text="Buscar", width=15, height=1, command=self.modificar_dados_disciplina).place(x=400,y=66)
    def modificar_dados_disciplina(self):
        codigo = str(self.codigo_disciplina_mod.get())
        connect = sqlite3.connect('Database.db')
        cursor = connect.cursor()
        cursor.execute("select * from disciplina where Codigo = '{}'".format(codigo))
        Database = cursor.fetchone()
        if Database != None:
            Label(self.frame_disciplina, bg='azure2', fg='grey20', text="Nome:").place(x=200, y=190)
            self.novo_nome_depar_dis = Entry(self.frame_disciplina, width=30)
            self.novo_nome_depar_dis.place(x=250, y=190)
            Label(self.frame_disciplina, text="Codigo:", bg='azure2', fg='grey20').place(x=200, y=160)
            Label(self.frame_disciplina, text="{}".format(codigo)).place(x=250, y=160)
            Button(self.frame_disciplina, text="Alterar", fg='grey20', bg='azure2', command=self.update_disciplina).place(x=390,y=160)
        else:
            messagebox.showinfo("Aviso", "Esse codigo não esta cadastrado!")
        cursor.close()
        connect.close()
    def update_disciplina(self):
        codigo = str(self.codigo_disciplina_mod.get())
        nome = self.novo_nome_depar_dis.get()
        connect = sqlite3.connect("Database.db")
        cursor = connect.cursor()
        cursor.execute("update disciplina set Nome = '{}'  where Codigo = '{}'".format(nome, codigo))
        messagebox.showinfo("Aviso!", "Dados alterados com sucesso!")
        connect.commit()
        cursor.close()
        connect.close()
    def exclusao_disciplina(self):
        Label(self.frame_disciplina, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_disciplina, relief=SUNKEN, width=80, height=3, bg='azure2').place(x=190, y=80)
        Label(self.frame_disciplina, text='Exclusão de Disciplina', font=15, bg='azure2', fg='grey20').place(x=400, y=61)
        Label(self.frame_disciplina, text='Codigo:', bg='azure2', fg='grey20').place(x=200, y=95)
        self.codigo_exclusao = Entry(self.frame_disciplina, width=15)
        self.codigo_exclusao.place(x=250, y=97)
        Button(self.frame_disciplina, width=8, height=1, text='Confirmar', command=exclusao_disciplina).place(x=355, y=95)
    #FUNÇÕES MENU TURMAS
    def cadastro_turmas(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_turmas, relief=SUNKEN, width=80, height=9, bg='azure2').place(x=190, y=80)
        Label(self.frame_turmas, text='Criar Turmas', font=15, bg='azure2', fg='grey20').place(x=410, y=61)
        Label(self.frame_turmas, text='Codigo:', bg='azure2', fg='grey20').place(x=200, y=90)
        Label(self.frame_turmas, bg="grey20", fg="azure2", text="No maximo 6 caracteres!").place(x=380, y=90)
        Label(self.frame_turmas, text='Periodo:', bg='azure2', fg='grey20').place(x=200, y=120)
        Label(self.frame_turmas, text='CPF(prof):', bg='azure2', fg='grey20').place(x=200, y=150)
        Label(self.frame_turmas, text='Cod. Disc.:', bg='azure2', fg='grey20').place(x=200, y=180)
        self.codigo_turmas = Entry(self.frame_turmas, width=8)
        self.codigo_turmas.place(x=285, y=90)
        self.periodo = Entry(self.frame_turmas, width=8)
        self.periodo.place(x=285, y=120)
        self.cpf_prof_turmas = Entry(self.frame_turmas, width=15)
        self.cpf_prof_turmas.place(x=285, y=150)
        self.cod_disc_turmas = Entry(self.frame_turmas, width=15)
        self.cod_disc_turmas.place(x=285, y=180)
        Button(self.frame_turmas, width=8, height=2, text='Confirmar', command=criar_turmas_db).place(x=440,y=148)
        pass
    def cadastrar_aluno_turma(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_turmas, relief=SUNKEN, width=80, height=5, bg='azure2').place(x=180, y=50)
        Label(self.frame_turmas, bg="azure2", fg="grey20", text="CPF Aluno:").place(x=200, y=85)
        Label(self.frame_turmas, bg="azure2", fg="grey20",text="Codigo da turma:").place(x=400, y=85)
        Label(self.frame_turmas, bg="azure2", fg="grey20", text="Alunos", font=40).place(x=270,  y=170)
        Label(self.frame_turmas, bg="azure2", fg="grey20", text="Turmas", font=40).place(x=560,  y=170)
        self.cpf_aluno_add_turma = Entry(self.frame_turmas, width=15)
        self.cpf_aluno_add_turma.place(x=270, y=85)
        self.codigo_turma_add = Entry(self.frame_turmas, width=8)
        self.codigo_turma_add.place(x=500, y=85)
        #==================================================
        self.listbox_add_aluno = Listbox(self.frame_turmas, width=40, height=24)
        self.listbox_add_aluno.place(x=180, y=200)
        self.listbox_add_aluno.delete(0, END)
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from aluno")
        Database = cursor.fetchall()
        for x in Database:
            self.listbox_add_aluno.insert(END, x)
        # ==================================================
        self.listbox_turmas_add = Listbox(self.frame_turmas, width=52, height=24)
        self.listbox_turmas_add.place(x=430, y=200)
        self.listbox_turmas_add.delete(0, END)
        cursor.execute("select * from info_turmas")
        Database = cursor.fetchall()
        for x in Database:
            self.listbox_turmas_add.insert(END, x)
        Button(self.frame_turmas, width=15, text='Adicionar', command=adicionar_aluno_turma_db).place(x=600, y=81)
        cursor.close()
        conexao.close()

        pass
    def buscar_turmas(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_turmas, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_turmas, text='Codigo:', bg='azure2', fg='grey20').place(x=200, y=50)
        Label(self.frame_turmas, text='CPF Aluno:', bg='azure2', fg='grey20').place(x=200, y=80)
        self.listbox_turmas = Listbox(self.frame_turmas, width=95, height=26)
        self.listbox_turmas.place(x=180, y=130)
        self.codigo_turmas_bus = Entry(self.frame_turmas, width=15)
        self.codigo_turmas_bus.place(x=275, y=50)
        self.aluno_em_turma = Entry(self.frame_turmas, width=15)
        self.aluno_em_turma.place(x=275, y=80)
        Button(self.frame_turmas, text="Buscar", width=15, height=1, command=mostrarBuscar_codigo_turma).place(x=400,y=48)
        Button(self.frame_turmas, text="mostrar todas as turmas", width=19, height=1, command=self.mostrar_todas_turmas).place(x=530, y=48)
        Button(self.frame_turmas, text="Buscar Aluno", width=15, height=1, command=buscar_aluno_turma).place(x=400, y=76)
        pass
    def mostrar_todas_turmas(self):
        self.listbox_turmas.delete(0, END)
        conexao = sqlite3.connect('Database.db')
        cursor = conexao.cursor()
        cursor.execute("select * from info_turmas")
        Database = cursor.fetchall()
        if Database == []:
            messagebox.showinfo("Aviso", "Não há nenhum dado cadastrado!")
        self.listbox_turmas.insert(END, "    ID    |Periodo|  CPF professor | Cod. Disciplina")

        for x in Database:
            self.listbox_turmas.insert(END, x)
        pass
    def inicio_modificar_turmas(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_turmas, relief=SUNKEN, width=81, height=5, bg='azure2').place(x=180, y=35)
        Label(self.frame_turmas, text='Codigo:', bg='azure2', fg='grey20').place(x=210, y=70)
        self.codigo_turma_mod = Entry(self.frame_turmas, width=15)
        self.codigo_turma_mod.place(x=255, y=70)
        Button(self.frame_turmas, text="Buscar", width=15, height=1, command=self.modificar_dados_turmas).place(x=410, y=66)
        pass
    def modificar_dados_turmas(self):
        codigo = str(self.codigo_turma_mod.get())
        connect = sqlite3.connect('Database.db')
        cursor = connect.cursor()
        cursor.execute("select * from info_turmas where Codigo = '{}'".format(codigo))
        Database = cursor.fetchone()
        if Database != None:
            Label(self.frame_turmas, bg='azure2', fg='grey20', text="Periodo:").place(x=200, y=190)
            Label(self.frame_turmas, bg='azure2', fg='grey20', text="CPF Prof:").place(x=200, y=220)
            Label(self.frame_turmas, bg='azure2', fg='grey20', text="Disciplina:").place(x=200, y=250)
            self.novo_periodo = Entry(self.frame_turmas, width=30)
            self.novo_periodo.place(x=250, y=190)
            self.novo_prof_responsavel = Entry(self.frame_turmas, width=15)
            self.novo_prof_responsavel.place(x=250,y=220)
            self.novo_cod_disciplina = Entry(self.frame_turmas, width=15)
            self.novo_cod_disciplina.place(x=250, y=250)
            Label(self.frame_turmas, text="Codigo:", bg='azure2', fg='grey20').place(x=200, y=160)
            Label(self.frame_turmas, text="{}".format(codigo)).place(x=250, y=160)
            Button(self.frame_turmas, text="Alterar", fg='grey20', bg='azure2',command=self.update_turmas).place(x=390, y=160)
        else:
            messagebox.showinfo("Aviso", "Esse codigo não esta cadastrado!")
        cursor.close()
        connect.close()
        pass
    def update_turmas(self):
        codigo = str(self.codigo_turma_mod.get())
        periodo = self.novo_periodo.get()
        cpf_prof = self.novo_prof_responsavel.get()
        cod_disc = self.novo_cod_disciplina.get()
        connect = sqlite3.connect("Database.db")
        cursor = connect.cursor()
        cursor.execute("select * from professor where CPF = '{}'".format(cpf_prof))
        verificar_prof = cursor.fetchone()
        if verificar_prof == None:
            messagebox.showinfo("Aviso", "CPF do professor não cadastrado no sistema.")
            return
        cursor.execute("select * from disciplina where Codigo = '{}'".format(cod_disc))
        verificar_cod_disc = cursor.fetchone()
        if verificar_cod_disc == None:
            messagebox.showinfo("Aviso", "Codigo de disciplina invalido, Disciplina não ofertada")
            return
        cursor.execute("update info_turmas set Periodo = '{}', Professor_CPF = '{}', Disciplina = '{}'  where Codigo = '{}'".format(periodo, cpf_prof,cod_disc, codigo ))
        messagebox.showinfo("Aviso!", "Dados alterados com sucesso!")
        connect.commit()
        cursor.close()
        connect.close()
        pass
    def exclusao_turmas(self):
        Label(self.frame_turmas, width=600, height=550, bg='azure2').place(x=140,y=35)  # Da clear na função anterior na tela
        Label(self.frame_turmas, relief=SUNKEN, width=80, height=3, bg='azure2').place(x=190, y=80)
        Label(self.frame_turmas, text='Exclusão de Turma', font=15, bg='azure2', fg='grey20').place(x=400, y=61)
        Label(self.frame_turmas, text='Codigo:', bg='azure2', fg='grey20').place(x=200, y=95)
        self.codigo_exclusao_T = Entry(self.frame_turmas, width=15)
        self.codigo_exclusao_T.place(x=250, y=97)
        Button(self.frame_turmas, width=8, height=1, text='Confirmar', command=exclusao_turma).place(x=355,y=95)
        pass

#REFERENTE AO MENU DE ALUNOS, FUNCIONALIDADES COMPLEMENTARES
def verificar_cpf_aluno(dados):
    cpf = str(dados[0])
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from aluno where CPF = ?", (cpf,))
    Database = cursor.fetchone()
    if Database == None:
        adicionar_aluno_db(dados)
        #Segue para a proxima def, que adiciona ao Database
    else:
        messagebox.showerror('Error', 'CPF já cadastrado, forneça um diferente')
    connect.commit()
    cursor.close()
    connect.close()
def verificarEexclusao_cpf_aluno(dados):
    cpf = str(dados)
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from aluno where CPF = ?", (cpf,))
    Database = cursor.fetchone()
    if Database != None:
        cursor.execute("delete from aluno where CPF = ?", (cpf,)) #COMANDO PARA EXCLUIR DA TABELA NO BANCO DE DADOS
        cursor.execute("select * from turmas where Aluno_CPF = '{}'".format(cpf))
        verificar = cursor.fetchall()
        if verificar != []:
            cursor.execute("delete from turmas where Aluno_CPF = '{}'".format(cpf))
        messagebox.showinfo('deletado', 'Deletado com sucesso')
    else:
        messagebox.showinfo('Erro', 'CPF não encontrado!')
    connect.commit()
    cursor.close()
    connect.close()
def adicionar_aluno_db(dados):
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("insert into aluno values(?, ?)", (dados))
    messagebox.showinfo("Aviso", "Aluno adicionado com sucesso!")
    connect.commit()
    cursor.close()
    connect.close()
def modificar_dados(dados):
    cpf = str(dados)
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from aluno where CPF = ?", (cpf,))
    Database = cursor.fetchone()
    fun.nova_entrada_aluno()
    connect.commit()
    cursor.close()
    connect.close()
#REFERENTE AO MENU DE PROFESSORES, FUNCIONALIDADES COMPLEMENTARES
def mostrarBusca_cpf_professor():
    cpf = str(fun.cpf_busca_prof.get())
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from professor where CPF = ?", (cpf,))
    Database = cursor.fetchone()
    if Database != None:
        fun.listbox_prof.delete(0, END)
        fun.listbox_prof.insert(END, Database)
        #Segue para a proxima def, que adiciona ao Database
    else:
        messagebox.showinfo("Erro", "CPF Não encontrado!")
    cursor.close()
    connect.close()
def adicionar_professor_db():
    cpf = str(fun.cpf_prof.get())
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    nome = fun.nome_prof.get()
    dep = fun.departamento.get()
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from professor where CPF = '{}'".format(cpf))
    Database = cursor.fetchone()
    if Database == None:
        cursor.execute("insert into professor values('{}', '{}', '{}')".format(cpf, nome, dep))
        connect.commit()
        cursor.close()
        connect.close()
        messagebox.showinfo("Aviso", "Professor adicionado com sucesso!")
    else:
        messagebox.showinfo("Aviso", "Dados anteriores já foram cadastrados!")
def exclusao_professor():
    cpf = str(fun.cpf_exclusao.get())
    if len(cpf) != 11 or cpf.isnumeric() == False:
        messagebox.showinfo('CPF', 'CPF fornecido não atendeu aos requisitos!')
        return
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from professor where CPF = '{}'".format(cpf))
    Database = cursor.fetchone()
    if Database != None:
        cursor.execute("delete from professor where CPF = '{}'".format(cpf))  # COMANDO PARA EXCLUIR DA TABELA NO BANCO DE DADOS
        messagebox.showinfo('deletado', 'Deletado com sucesso')
    else:
        messagebox.showinfo('Erro', 'CPF não encontrado!')
    connect.commit()
    cursor.close()
    connect.close()
    pass
#REFERENTE AO MENU DE DISCIPLINAS, FUNCIONALIDADES COMPLEMENTARES
def adicionar_disciplina_db():
    codigo = str(fun.codigo_disciplina.get())
    nome = fun.nome_disciplina.get()
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from disciplina where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database == None:
        cursor.execute("insert into disciplina values('{}', '{}')".format(nome, codigo))
        connect.commit()
        cursor.close()
        connect.close()
        messagebox.showinfo("Aviso", "Disciplina adicionado com sucesso!")
    else:
        messagebox.showinfo("Aviso", "Dados anteriores já foram cadastrados!")
    pass
def mostrarBuscar_codigo_dis():
    codigo = str(fun.codigo_disciplina_bus.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from disciplina where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database != None:
        fun.listbox_disci.delete(0, END)
        fun.listbox_disci.insert(END, Database)
    else:
        messagebox.showinfo("Aviso", "Codigo de disciplina não cadastrada!")
    cursor.close()
    connect.close()
def exclusao_disciplina():
    codigo = str(fun.codigo_exclusao.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from disciplina where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database != None:
        cursor.execute(
            "delete from disciplina where Codigo = '{}'".format(codigo))  # COMANDO PARA EXCLUIR DA TABELA NO BANCO DE DADOS
        messagebox.showinfo('Aviso', 'Deletado com sucesso')
    else:
        messagebox.showinfo('Aviso', 'Codigo não cadastrado!')
    connect.commit()
    cursor.close()
    connect.close()

#REFERENTE AO MENU DE TURMAS, FUNCIONALIDADES COMPLEMENTARES
def criar_turmas_db():
    codigo = str(fun.codigo_turmas.get())
    periodo = fun.periodo.get()
    cpf_prof = fun.cpf_prof_turmas.get()
    cod_dis_turmas = fun.cod_disc_turmas.get()
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from info_turmas where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database == None:
        cursor.execute("insert into info_turmas values('{}', '{}', '{}', '{}')".format(codigo, periodo, cpf_prof, cod_dis_turmas))
        connect.commit()
        cursor.close()
        connect.close()
        messagebox.showinfo("Aviso", "Turma cadastrada com sucesso!")
    else:
        messagebox.showinfo("Aviso", "Essa turma já foi cadastrada!")
    pass
def mostrarBuscar_codigo_turma():
    fun.listbox_turmas.delete(0, END)
    codigo = str(fun.codigo_turmas_bus.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from turmas where Codigo = '{}'".format(codigo))
    Database = cursor.fetchall()
    if Database != None:
        for x in Database:
            fun.listbox_turmas.insert(END, x)
    else:
        messagebox.showinfo("Erro", "Turma Não encontrada!")
    cursor.close()
    connect.close()
def buscar_aluno_turma():
    cpf_aluno = str(fun.aluno_em_turma.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from turmas where Aluno_CPF = '{}'".format(cpf_aluno))
    Database = cursor.fetchall()
    if Database != []:
        fun.listbox_turmas.delete(0, END)
        fun.listbox_turmas.insert(END, Database)
    else:
        messagebox.showinfo("Aviso", "Aluno Não matriculado em turmas.")
    cursor.close()
    connect.close()
def exclusao_turma():
    codigo = str(fun.codigo_exclusao_T.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from info_turmas where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database != None:
        cursor.execute("delete from info_turmas where Codigo = '{}'".format(codigo))  # COMANDO PARA EXCLUIR DA TABELA NO BANCO DE DADOS
        cursor.execute("delete from turmas where Codigo = '{}'".format(codigo))  # COMANDO PARA EXCLUIR DA TABELA NO BANCO DE DADOS
        messagebox.showinfo('Aviso', 'Deletado com sucesso')
    else:
        messagebox.showinfo('Aviso', 'Codigo não cadastrado!')
    connect.commit()
    cursor.close()
    connect.close()
def adicionar_aluno_turma_db():
    cpf = str(fun.cpf_aluno_add_turma.get())
    codigo = str(fun.codigo_turma_add.get())
    connect = sqlite3.connect('Database.db')
    cursor = connect.cursor()
    cursor.execute("select * from turmas where Aluno_CPF = '{}'".format(cpf))
    verificar = cursor.fetchone()
    if verificar != None:
        messagebox.showinfo("Aviso", "CPF já cadastrado anteriormente.")
        return
    cursor.execute("select * from info_turmas where Codigo = '{}'".format(codigo))
    Database = cursor.fetchone()
    if Database != None:
        cursor.execute("select * from aluno where CPF = '{}'".format(cpf))
        verif = cursor.fetchone()
        if verif != None:
            cursor.execute("insert into turmas values('{}', '{}')".format(codigo, cpf))
            messagebox.showinfo("Aviso", "Aluno cadastrado com Sucesso!!")
        else:
            messagebox.showinfo("Aviso", "CPF incorreto!")
    else:
        messagebox.showinfo("Aviso", "Codigo da turma incorreto")
    cursor.close()
    connect.commit()
    connect.close()
    pass

janela = Tk()
janela.title("Sistema de Controle Academico")
janela.geometry('800x600+10+10')
fun = interface(janela)
janela.mainloop()
