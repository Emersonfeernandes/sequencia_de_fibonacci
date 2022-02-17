from func_fibo import fibonacci_

y = int(input('Digite quantos números para a sequência: '))
valor ={k:v for k,v in enumerate(fibonacci_(y))}
print(valor)
