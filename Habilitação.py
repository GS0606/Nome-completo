def habilitacao():
    idade = input('Qual sua idade? ')
    idade = int(idade)
    if idade >= 18:
        print('Pode tirar habilitação')
    else:
        tempo = 18 - idade
        print(f'Calma... espere {tempo} ano(s) para tirar habilitação')

habilitacao()
