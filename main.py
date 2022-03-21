from tkinter import *

################# cores ###############
co0 = "#000000"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue
co10 = "#2651ac"
co11= '#9eb5e6'

################# Janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background= co9)
# janela.resizable(width=False, height=False)

################# Dividindo Janela ###############
frame_cima = Frame(janela, widt=310, height=50, bg=co10, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, widt=310, height=403, bg=co11, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1 )

frame_direita = Frame(janela, widt=588, height=403, bg=co9, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# Label Cima ###############
app_nome = Label(frame_cima, text='Formulário de Cadastro', anchor=NW, font=('Ivy 13 bold'),fg=co1, bg=co10, relief='flat')
app_nome.place(x=45, y=15)

janela.mainloop()