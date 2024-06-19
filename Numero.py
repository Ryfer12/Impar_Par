while True:
  par_impar = lambda num: "Par" if num % 2 == 0 else "Impar"

  pergunta = input('Gostaria de saber se um número é par ou ímpar? [S/N]: ')
  print()
  if pergunta.lower() == 'sim' or pergunta.lower() == 's':
    print()
    numero = int(input('Digite um numero: '))
    print(f'O numero {numero} é {par_impar(numero)}')
    print()
  elif pergunta.lower() == 'não' or pergunta.lower() == 'n':
    print()  
    print('Ok, até mais!')
    break