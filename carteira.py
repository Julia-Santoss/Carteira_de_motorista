idade = int(input("Digite a sua idade:"))

exame = str(input("Você passou no exame médico? (Digite = S/N)")).upper()

violacao = str(input("Você possui alguma violação? (Digite = S/N)")).upper()
if(idade >=18) and (exame =="S") and (violacao == "N"):
  print("Você pode pegar a carteira de motorista")
else:
  print("Você não pode pegar a carteira de motorista")
