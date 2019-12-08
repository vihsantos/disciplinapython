digito= (input("Insira o digito da conta: \n"))
print(digito)

digitoc= digito[::-1]

print(digitoc)

digitoo=int(digito) + int(digitoc)

digitoo= int(digitoo/100) * 1 + int (digitoo%100/10) * 2 + int (digitoo%10/1) * 3

print(digitoo%10)
