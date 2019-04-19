mercadoria = int (input ("Digite o valor da mercadoria "))

desconto = int (input ("Digite a porcentagem do desconto "))

print ("Com desconto a mercadoria custará: ", mercadoria - (mercadoria * desconto / 100))

print ("O Desconto foi de", desconto * mercadoria / 100, "reais")
