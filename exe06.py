# Faça um programa que leia um número inteiro e mostra na tela o seu sucesso e seu antecessor.

numero  = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero +  1

print('Analisando o valor {}, seu antecessor é {} e sucessor é {}'.format(numero, antecessor, sucessor))

# Podemos fazer de outra forma
# Vamos usar uma única variável para guardar o valor número

numero2  = int(input('Digite um número inteiro: '))
print('Analisando o valor {}, seu antecessor é {} e sucessor é {}'.format(numero2, (numero2-1), (numero2+1)))
