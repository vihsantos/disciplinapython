quantfita= int (input("Insira a quantidade de fita: "))
valorfita= float (input("Insira o valor da fita: "))

faturamentoanual=quantfita/3*valorfita*12

print(faturamentoanual)

multa= quantfita/10 * (valorfita + valorfita*0.1)

print("O valor ganho com multas é: ")
print(multa)

quantfinal= quantfita - quantfita*0.02 + quantfita*0.1

print (f'A quantidade final é {quantfinal}')
