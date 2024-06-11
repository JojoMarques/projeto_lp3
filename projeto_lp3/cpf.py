from validate_docbr import CPF #importa a classe CPF

cpf = CPF() #cria uma instância de CPF (um objeto)

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("435.543.548-21"))
print(cpf.validate("43554354821"))
