from random import randrange
nome = str(input("Digite o nome do Jogador: "))
print(''' >>>OPÇÕES<<<
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA ''')

jogador = int(input("ESCOLHA SUA OPÇÃO: "))


maquina = randrange(1,3)

if jogador == 1 and maquina == 1:
   print(nome + " você escolheu PEDRA e a maquina PEDRA, EMPATE!")
elif jogador == 1 and maquina == 2:
  print(nome + " você escolheu PEDRA e a maquina PAPEL, MAQUINA VENCEU!!")
elif jogador == 1 and maquina == 3:
  print(nome + " você escolheu PEDRA e a maquina TESOURA, JOGADOR VENCEU!!")
elif jogador == 2 and maquina == 1:
  print(nome + " você escolheu PAPEL e a maquina PEDRA, JOGADOR VENCEU!!!")
elif jogador == 2 and maquina == 2:
  print(nome + " você escolheu PAPEL e a maquina PAPEL EMPATE!!!" )
elif jogador == 2 and maquina == 3:
  print(nome + " você escolheu PAPEL e a maquina TESOURA, MAQUINA VENCEU!!!")
elif jogador == 3 and maquina == 1:
  print(nome + " você escolheu TESOURA e a maquina PEDRA, MAQUINA VENCEU!!!")
elif jogador == 3 and maquina == 2:
  print(nome + " você escolheu TESOURA e a maquina PAPEL,JOGADOR VENCEU!!!")
elif jogador == 3 and maquina == 3:
  print(nome + " você escolheu TESOURA e a maquina TESOURA,EMPATE!!!") 
else:
  print("OPÇÃO INVALIDA")