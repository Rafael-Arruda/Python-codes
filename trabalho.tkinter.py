from tkinter import *
janela = Tk()
janela.title('Cálculo de média')
janela['bg'] = 'blue'
def bt_click():
    num1 = float(ed1.get())
    num2 = float(ed2.get())

    lb6['text'] = ((2*num1) + (3*num2))/5
    if lb6['text'] < 7:
        lb8['text'] = 'REPROVADO'
    else:
        lb8['text'] = 'APROVADO'

lb1 = Label(janela, text='ATIVIDADE DE FUNDAMENTOS DE PROGRAMAÇÃO UTILIZANDO A BIBLIOTECA TKINTER')
lb1.place(x=5, y=2)
lb2 = Label(janela, text='Cálculo da média e situação do aluno')
lb2.place(x=80, y=70)
lb3 = Label(janela, text='Nota 1 :')
lb3.place(x=60, y=100)
lb4 = Label(janela, text='Nota 2 :')
lb4.place(x=60, y=130)
lb5 = Label(janela, text='Média:')
lb5.place(x=60, y=190)
lb6 = Label(janela, text='resultado')
lb6.place(x=120, y=190)
lb7 = Label(janela, text='Situação do aluno :')
lb7.place(x=7, y=220)
lb8 = Label(janela, text='resultado')
lb8.place(x=120, y=220)

ed1 = Entry(janela)
ed1.place(x=120, y=100)
ed2 = Entry(janela)
ed2.place(x=120, y=130)

bt = Button(janela, text='Calcular', width=20, command=bt_click)
bt.place(x=110, y=155)

janela.geometry('500x300+200+200')

janela.mainloop()
