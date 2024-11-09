""" Sabe-se que, para iluminar de maneira correta os cômodos de
 uma casa, para cada m2, deve-se usar 18 W de potência. Faça um programa
 que receba as duas dimensões de um cômodo (em metros), calcule e mostre
 a sua área (em m2) e a potência de iluminação que deverá ser utilizada. """

#Entrada

#medidas: a, b 

a = float(input("Digite aqui a primeira médida: (Ex: 0.0) "))

b = float(input("Digite aqui a segunda médida: "))

area = a * b
print(f"area comodo: {area:.2f} m²") 

watts  = area * 18
print(f"potência de iluminação necessária: {watts:.2f} m²")
