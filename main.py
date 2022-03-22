from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from view  import *

################# cores ###############
co0 = "#000000"  # Preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelho
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue
co10 = "#2651ac"
co11= '#9eb5e6'
verde = '#008000' 
################# Janela ###############

janela = Tk()
janela.title("FACULDADE TECHDEV")
janela.geometry('1105x653')
janela.configure(background= co9)
janela.resizable(width=1505, height=853)

################# Dividindo Janela ###############
frame_cima = Frame(janela, widt=410, height=80, bg=co10, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, widt=410, height=603, bg=co11, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1 )

frame_direita = Frame(janela, widt=88, height=503, bg=co9, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# Label Cima ###############
lc_nome = Label(frame_cima, text='Formulário de Aluno', anchor=NW, font=('Ivy 18 bold'),fg=co1, bg=co10, relief='flat')
lc_nome.place(x=75, y=20)

################# Label Baixo ###############
#nome
lb_nome = Label(frame_baixo, text='Nome*', anchor=NW, font=('Ivy 12 bold'),fg=co0, bg=co11, relief='flat')
lb_nome.place(x=25, y=15)
input_nome = Entry(frame_baixo, width=55, justify='left', relief='solid')
input_nome.place(x=25, y=45)

#email
lb_email = Label(frame_baixo, text='Email*', anchor=NW, font=('Ivy 12 bold'),fg=co0, bg=co11, relief='flat')
lb_email.place(x=25, y=85)
input_email = Entry(frame_baixo, width=55, justify='left', relief='solid')
input_email.place(x=25, y=115)

#telefone
lb_telefone = Label(frame_baixo, text='Telefone*', anchor=NW, font=('Ivy 12 bold'),fg=co0, bg=co11, relief='flat')
lb_telefone.place(x=25, y=145)
input_telefone = Entry(frame_baixo, width=55, justify='left', relief='solid')
input_telefone.place(x=25, y=175)

#nascimento
lb_nascimento = Label(frame_baixo, text='Data de Nascimento*', anchor=NW, font=('Ivy 10 bold'),fg=co0, bg=co11, relief='flat')
lb_nascimento.place(x=25, y=205)
input_nascimento = DateEntry(frame_baixo, width=18, background='dark', foreground='white', borderwidth=2, year=2000)
input_nascimento.place(x=25, y=230)

#Ativo
var1= IntVar()
ativo = Checkbutton(frame_baixo, text="ATIVO", variable=var1,bg=co11)
ativo.place(x=195, y=230)

# botão inserir
bt_inserir = Button(frame_baixo, text='Inserir', width=10, font=('Ivy 12 bold'), bg=verde, fg=co1, relief='raised', overrelief='ridge')
bt_inserir.place(x=25, y=500)

# botão atualizar
bt_atualizar = Button(frame_baixo, text='Atualizar', width=10, font=('Ivy 12 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
bt_atualizar.place(x=145, y=500)

# botão deletar
bt_deletar = Button(frame_baixo, text='Deletar', width=10, font=('Ivy 12 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
bt_deletar.place(x=265, y=500)


######################### FRAME DIREITA ##############

lista = [[1,'Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Sim'],
           [2,'Fortnato Mpngo', 'joao@mail.com', 123456789, "12/19/2010", 'Sim'],
           [3,'Usando Python',  'joao@mail.com', 123456789, "12/19/2010", 'Não'],
           [4,'Clinton Berclidio', 'joao@mail.com', 123456789, "12/19/2010", 'Sim'],
           [5,'A traicao da Julieta','joao@mail.com', 123456789, "12/19/2010", 'Não']
           ]

campos_tabela = ['ID', 'Nome', 'Email', 'Telefone', 'Nascimento', 'Ativo']
# criando a tabela
tree = ttk.Treeview(frame_direita, selectmode="extended", columns=campos_tabela, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_direita.grid_rowconfigure(0, weight=12)


hd=["nw","nw","nw","nw","nw","center","center"]
h=[40,180,150,110,130,60,110]
n=0

for col in campos_tabela:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n],anchor=hd[n])
    
    n+=1

for item in lista:
    tree.insert('', 'end', values=item)

janela.mainloop()