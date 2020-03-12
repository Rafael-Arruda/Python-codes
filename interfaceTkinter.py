from tkinter import *
janela = Tk()
janela.title('Cálculo de média')
janela['bg'] = 'blue'

def bt_click():
    num1 = float(ed1.get())
    num2 = float(ed2.get())
    m = ((2*num1) + (3*num2))/5
    if m >= 9:
        lb12['text'] = 'Parabéns'

    lb6['text'] = m
    if lb6['text'] > 7:
        lb8['text'] = 'APROVADO'
    elif lb6['text'] < 3:
        lb8['text'] = 'REPROVADO'
    else:
        def bt1_click():
            num3 = float(ed3.get())
            mf = (num3 + m)/2
            if mf >= 5:
                lb11['text'] = 'APROVADO NA RECUPERAÇÃO'
            else:
                lb11['text'] = 'REPROVADO NA RECUPERAÇÃO'
        lb8['text'] = 'RECUPERAÇÃO'
        lb9 = Label(janela, text='nota final :')
        lb9.place(x=45, y=250)
        lb10 = Label(janela, text='Situação final :')
        lb10.place(x=25, y=320)
        lb11 = Label(janela, text='resultado')
        lb11.place(x=120, y=320)
        ed3 = Entry(janela)
        ed3.place(x=120, y=250)
        bt1 = Button(janela, text='Calcular', width=20, command=bt1_click)
        bt1.place(x=110, y=280)

lb1 = Label(janela, text='ATIVIDADE DE FUNDAMENTOS DE PROGRAMAÇÃO UTILIZANDO A BIBLIOTECA TKINTER')
lb1.place(x=5, y=2)
lb2 = Label(janela, text='Cálculo da média e situação do aluno')
lb2.place(x=80, y=70)
lb3 = Label(janela, text='Nota 1 :')
lb3.place(x=60, y=100)
lb4 = Label(janela, text='Nota 2 :')
lb4.place(x=60, y=130)
lb5 = Label(janela, text='Média:')
lb5.place(x=62, y=190)
lb6 = Label(janela, text='')
lb6.place(x=120, y=190)
lb7 = Label(janela, text='Situação do aluno :')
lb7.place(x=2, y=220)
lb8 = Label(janela, text='')
lb8.place(x=120, y=220)
lb12 = Label(janela, text='')
lb12.place(x=180, y=190)

ed1 = Entry(janela)
ed1.place(x=120, y=100)
ed2 = Entry(janela)
ed2.place(x=120, y=130)

bt = Button(janela, text='Calcular', width=20, command=bt_click)
bt.place(x=110, y=155)

janela.geometry('500x350+200+200')

janela.mainloop()
