#Programa para calcular quantos sálarios mininmos você ganha.

print("Olá,\nseja bem-vindo!" )
print("Nesse software você vai conseguir calcular quantos sálarios mínimos você recebe!")

#Entrada dados
salario_min = float(input(" - Digite aqui o salário mínimo atual: "))
salario_func = float(input(" - Agora digite aqui seu salário atual: ")) 
#Processamento
quant_sal = salario_min = salario_func/salario_min

print(f" - Você recebe: {quant_sal:.2f} salários mínimos!") 
