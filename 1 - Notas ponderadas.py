#Programa onde se pede duas notas, e calcule a media ponderada.

#Entrada de dados
nota1 = float(input("Coloque aqui sua primeira nota: "))
nota2 = float(input("Coloque aqui sua segunda nota: "))
#processamento de dados
#n1=peso2  n2=peso3
media = (nota1*2+nota2*3)/5
#saída de dados
print(f"A media de suas notas é: {media:.2f}")