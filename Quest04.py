v_hora_aula= (int (input("Digite o valor da hora aula: \n")))
n_hora_dada= (int (input("Digite o numero de horas dada: \n")))
percent_desc=(int (input("Digite o valor do percentual de desconto: \n")))

salariobruto= v_hora_aula*n_hora_dada

desc=percent_desc*salariobruto/100

salariocomdesc= salariobruto-desc

print("O salario bruto eh: ")
print (salariobruto)

print("O desconto eh")
print(desc)

print("O salario com o desconto eh")
print (salariocomdesc)
