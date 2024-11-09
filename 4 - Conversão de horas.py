#Programa que recebe um hora, calcule e mostre: 1- a hora convertida em minutos. 
# 2- O total de minutos  digitados mais a conversão anterior. 
# 3-Minutos em segundos.

#Entrada
horas = int(input("Digite as horas aqui: "))
minutos = int(input("Digite os minutos: "))

#       Processo
#hora/min
hora_minutos = horas * 60
print (f"Total de horas em minutos: {hora_minutos}")

#Total min
total_minutos = minutos + hora_minutos
print (f"Total de de minutos: {total_minutos}")

#Minutos em segundos
minutos_segundos = total_minutos * 60
print (f"Total de miutos em sgundos: {minutos_segundos}")


#mascara int/float
#  f" Saída: {variavel:.2f}
#  f" Saída: {variavel:}