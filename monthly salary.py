renda = float(input('Precisamos de dados p/ saber se você é elegível p/ receber empréstimos. '
                    'Qual sua renda mensal?'))

score = int(input('Qual o seu score de crédito?'))

fiadscore = str(input('você tem um fiador de score?[S/N]'))

if fiadscore.upper()=='S':
    scorefiador = int(input('qual o score do seu fiador?'))
    if (scorefiador>700):
     print('voce é elegível para o empréstimo')
elif (renda>=2000) and (score>=600):
    print('você é elegível para o empréstimo')
else:
    print('você não é elegível para o empréstimo')
