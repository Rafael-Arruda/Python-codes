def aumento(salario):
    y = (5/100)*salario
    return y

sal = float(input('digite seu salario:R$'))
print('o aumento foi de : R$', aumento(sal))
