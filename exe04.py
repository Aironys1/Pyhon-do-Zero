# Faça um programa que leia algo
# Todo objeto string tem esses métodos

a = input ("Digite algo: ")
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços', a.isspace())
print('É um número ? ', a.isnumeric())
print('É alfabético ?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Está em maiuscula ?', a.isupper())
print('Está em minusculas ?', a.islower())
print('Está capitalizada?',a.istitle())




