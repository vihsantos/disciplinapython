e= int(input("Digite o valor do empréstimo: \n"))
tj= float(input("Digite a taxa de juros em decimal:\n"))
t= int(input("Digite a quantidade de meses: \n"))

j=e*tj*t

JuroseEmprestimo= e+j

TT= JuroseEmprestimo/t

print("O valor da prestação é: \n")
print(TT)
