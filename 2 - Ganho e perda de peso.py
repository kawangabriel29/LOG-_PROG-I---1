#Programa onde recebe um peso inicial, e cálcule ganho de 15%, ou perda de 20% no peso inicial.
#   a = peso inicial
#   b = peso gordo 15%
#   c = peso magro 20%
print("Olá! Tudo bem?")

#Entrada de dados
a = float(input("Digite aqui seu peso atual (em kg): "))
#processamento dos dados
b = a+(a*0.15)
c = a-(a*0.20)
#saída dos dados
print(f"O seu peso atual é: {a:.2f} kg.")
print(f"Aqui está o seu peso com um aumento de 15%: {b:.2f}kg")
print(f"Aqui está o seu peso com uma diminuição de 20%: {c:.2f}kg")
print("Muito obrigado!")
