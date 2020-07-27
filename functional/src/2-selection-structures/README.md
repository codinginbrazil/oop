## Selection Structures 

###  Verificar valor 
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#### Solução

### Número primo
Faça um programa que exiba verdadeiro se o número for primo (falso caso contrário)

### Tipo de triângulo
Pedir os valores dos catetos e hipotenusa, por intermédio deles informar se o triângulo é equilátero; isóscele; escaleno 
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/triangulo.pas)

### Energia elétrica
Calcule o valor da fatura do cliente, por intermédio do consumo em Kw/H e a categoria de consumo, sendo:
* residencial =  consumo em KwH * 0.6);
* comercio = consumo em KwH * 0.48);
* industria = consumo em KwH * 1.29);
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/energia-eletrica.pas)

###  Votar
Perguntar a idade do usuário e verificar se ele pode votar, de acordo com seguinte regra:  
* idade>=16 não pode votar
* idade>=18 obrigado a votar 
* idade>=65 pode votar
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/votar.pas)

### Mini Calculadora
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/minicalculadora.pas)

### Cálculo de churrasco
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/churrasco.pas)

### Cálculo de peso ideal
Leia altura, sexo e peso de uma pessoa, construa um algoritmo que calcule seu peso ideal.  
Informe se o peso da pessoa está dentro, acima ou abaixo do peso 
(Considere a margem de erro de 1 Kg para mais ou para menos como estando no peso ideal). 
Utilizando as seguintes fórmulas:
* Para homens: peso - (72.7*h) - 58
* Para mulheres: peso - (62.1*h) - 44.7
#### Solução
> [Julia](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/julia/peso-ideal.jl)

### Reajuste salarial
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/reajuste-salarial.pas)

### Salário de Professor
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/pascal/salario-prof.pas)

### Comissão de vendas
Dado o salário fixo, o valor das vendas efetuadas pelo vendedor de uma empresa e sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 e 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
#### Solução em:
 > [Julia](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/julia/comissao-venda.jl)  

### Gasto em lavanderia
Prepare um algoritmo para informar o total gasto em uma lavanderia. 
O algoritmo inicialmente deverá perguntar o total de camisas, o total de calças e o total de meias e informar o total gasto, levando em conta a seguinte tabela de preços:

* 02.00 = Meias 
* 05.00 = Camisas 
* 10.00 = Calças 

Depois de informar o total gasto, o algoritmo deverá perguntar ao usuário se o mesmo deseja fazer um novo cálculo de gasto, caso a resposta seja positiva, o algoritmo deverá retornar ao seu início, caso contrário deverá ser finalizado
#### Solução em:

### Loja de tintas
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
* Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* comprar latas e galões, a combinação de melhor resultado.
#### Solução em:

 ### Notas para representar um valor
Escrever um algoritmo que leia um valor e calcule qual o menor número possível de notas e
moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido pode ser decomposto. 
Escrever o valor lido e a relação de notas necessárias.
#### Solução em:

### Segundos para dia
Desafio do vídeo "Entrada de Dados": Reescreva o programa conta
Segundos para imprimir também a quantidade de dias,
ou seja, faça um programa em Python que dada a quantidade de segundos,
o programa "quebra" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.

#### Solução em:
 > [Python](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/python/second2day.py)  


### Dezena
Faca um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:

Digite um número inteiro: 78615

Saída de Dados:

O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:

Digite um número inteiro: 2

Saída de Dados:

O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto,
ou seja, aquilo que é menor que o divisor.
O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado,
ou seja, tudo que é maior ou igual ao divisor.

#### Solução em:
 > [Python](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/python/dezena.py)  


### Equação do segundo grau

programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente,
e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente,
ou seja, X deve ser menor ou igual a Y.

#### Solução em:
 > [Python](https://github.com/computersciencebr/algoritmo/tree/master/functional/src/2-selection-structures/python/segundo_grau.py)  