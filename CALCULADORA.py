from tkinter import *
from tkinter import ttk


#cores digite no google:  'colour picker'
cor1 = "#040a06"   #preto
cor2 = "#61c984"    #verde claro
cor3= "#c9f02e"      #amarelo escuro
cor4 = "#ed7a0e"     #laranja
cor5= "#aeb0b8"     #cinza
cor6 = "#ffffff"    #branco
cor7= "#464975"    #azul escuro

janela = Tk() #-> cria uma instância do objeto Tk, que representa a janela principal do aplicativo. Essa janela é a base da interface gráfica e é necessária para criar e exibir outros widgets, como botões, campos de entrada, rótulos, entre outros.
janela.title("Calculator A2Tecnology")  #---> seleciona o titulo da janela
janela.geometry("280x323")    #--> seleciona a dimensão do aplicativo
janela.config(bg=cor1)


#dividindo a janela em duas partes com display e os botoes:

# criando os frames

frame_tela = Frame(janela, width=280 , height=65 , bg= cor2) #-> define o tamanhos do display a onde ira aparecer os resultados bg: siginifca a cor do background
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=280 , height=285 , bg= cor1)
frame_corpo.grid(row=1, column=0)    #-> row serve para separar as partes do programa, pesquisar no chatgpt

todos_valores = ""

def entrar_valores(event):

    global todos_valores   #--> Qualquer alterações que fizermos nessa variavel ela sera mantida e reusada

    todos_valores = todos_valores + str(event)


    #passando valor para tela:
    valor_texto.set(todos_valores)

#função para calcular os valores

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função para zerar a tela:

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")

#criando label

valor_texto = StringVar()
                                #textvariable é o que faz aparecer os numeros no display
app_label = Label(frame_tela , textvariable=valor_texto, width=18, height=2, padx=3, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial', 19 ,'bold'), fg=cor6 , bg=cor7) #labbel é o display
app_label.place(x=0,y=0)

#criando botoes:

b_1= Button(frame_corpo,command= limpar_tela, text="C", width=9 , height=2,bg=cor5, font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_1.place(x=0,y=0)

b_2= Button(frame_corpo,command= lambda: entrar_valores("%") , text="%", width=9 , height=2,bg=cor5,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_2.place(x=95,y=0) #text é titulo do bota, width-> largura, height-> altura, bg-> cor, front-> estilo da letra, relief-> deixa o botao em 3d, overrelief-> quando passa o mouse por cima do botão ele aponta um relevo

b_3= Button(frame_corpo,command= lambda: entrar_valores("/") , text="/", width=9 , height=2,bg=cor4,fg=cor6,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_3.place(x=190,y=0)

###############################################
###############################################

b_4= Button(frame_corpo,command= lambda: entrar_valores("7") , text="7", width=6 , height=2,bg=cor5, font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_4.place(x=0,y=52)

b_5= Button(frame_corpo,command= lambda: entrar_valores("8") , text="8", width=6 , height=2,bg=cor5,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_5.place(x=71,y=52) #text é titulo do bota, width-> largura, height-> altura, bg-> cor, front-> estilo da letra, relief-> deixa o botao em 3d, overrelief-> quando passa o mouse por cima do botão ele aponta um relevo

b_6= Button(frame_corpo,command= lambda: entrar_valores("9") , text="9", width=6 , height=2,bg=cor5,fg=cor1,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_6.place(x=142,y=52)

b_7= Button(frame_corpo,command= lambda: entrar_valores("*") , text="*", width=6 , height=2,bg=cor4,fg=cor6,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_7.place(x=213,y=52)

##############################################
##############################################

b_8= Button(frame_corpo,command= lambda: entrar_valores("4") , text="4", width=6 , height=2,bg=cor5, font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_8.place(x=0,y=104)

b_9= Button(frame_corpo,command= lambda: entrar_valores("5") , text="5", width=6 , height=2,bg=cor5,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_9.place(x=71,y=104) #text é titulo do bota, width-> largura, height-> altura, bg-> cor, front-> estilo da letra, relief-> deixa o botao em 3d, overrelief-> quando passa o mouse por cima do botão ele aponta um relevo

b_10= Button(frame_corpo,command= lambda: entrar_valores("6") , text="6", width=6 , height=2,bg=cor5,fg=cor1,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_10.place(x=142,y=104)

b_11= Button(frame_corpo,command= lambda: entrar_valores("-") , text="-", width=6 , height=2,bg=cor4,fg=cor6,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_11.place(x=213,y=104)

#################################################
#################################################

b_12= Button(frame_corpo,command= lambda: entrar_valores("1") , text="1", width=6 , height=2,bg=cor5, font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_12.place(x=0,y=156)

b_13= Button(frame_corpo,command= lambda: entrar_valores("2") , text="2", width=6 , height=2,bg=cor5,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_13.place(x=71,y=156) #text é titulo do bota, width-> largura, height-> altura, bg-> cor, front-> estilo da letra, relief-> deixa o botao em 3d, overrelief-> quando passa o mouse por cima do botão ele aponta um relevo

b_14= Button(frame_corpo, command= lambda: entrar_valores("3") , text="3", width=6 , height=2,bg=cor5,fg=cor1,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_14.place(x=142,y=156)

b_15= Button(frame_corpo, command= lambda: entrar_valores("+") , text="+", width=6 , height=2,bg=cor4,fg=cor6,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_15.place(x=213,y=156)

#####################################################
#####################################################

b_16= Button(frame_corpo, command= lambda: entrar_valores("0") , text="0", width=9 , height=2,bg=cor5, font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_16.place(x=0,y=208)

b_17= Button(frame_corpo, command= lambda: entrar_valores(".") , text=".", width=9 , height=2,bg=cor5,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_17.place(x=95,y=208) #text é titulo do bota, width-> largura, height-> altura, bg-> cor, front-> estilo da letra, relief-> deixa o botao em 3d, overrelief-> quando passa o mouse por cima do botão ele aponta um relevo

b_18= Button(frame_corpo, command= calcular, text="=", width=9 , height=2,bg=cor4,fg=cor6,font=('Arial', 12 ,'bold'), relief="raised",overrelief=RIDGE)
b_18.place(x=190,y=208)









janela.mainloop()


































