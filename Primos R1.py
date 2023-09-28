import time

print(" A FABULOSA MÁQUINA DE CALCULAR NUMEROS PRIMOS ")

primeiro_numero = int(input("Informe o menor número do intervalo: "))
ultimo_numero = int(input("Informe o maior número do intervalo: "))
x = primeiro_numero

timer_on = time.time()
lista_de_primos = []

if primeiro_numero == 2:
    lista_de_primos = [2]
    primeiro_numero = primeiro_numero + 1
else:
    if primeiro_numero % 2 != 0:                # Significa que é impar
        pass
    else:
        primeiro_numero = primeiro_numero - 1   # Recua em 1 unidade o primeiro número, que é par, tornando-o ímpar.


for numero_testado in range(primeiro_numero, ultimo_numero + 1, 2):
    primo = True
    raiz_do_numero_testado = float(numero_testado**(1/2))
    raiz_inteira = int(raiz_do_numero_testado)

    for divisor in range(3, raiz_inteira + 1, 2):
        if numero_testado % divisor == 0:
            primo = False
            break

    if primo:
        lista_de_primos.append(numero_testado)

timer_off = time.time()
time = timer_off - timer_on

for i in range(0, len(lista_de_primos)):
    print(f'O {i+1}° número primo é {lista_de_primos[i]}.')
print(f'Foram encontrados {len(lista_de_primos)} números primos no intervalo entre {x} e {ultimo_numero}.')
print(f'Foram necessários {time} segundos para determinar esse números.')

'''
Alguns resultados obtidos com essa versão:
3 até 10.000.000 = 664.578 primos encontrados em 134,19 s.
3 até 1.000.000 = 78.497 primos encontrados em 4.71 s.
3 até 100.000 = 9.591 primos encontrados em 0,192s
3 até 10.000 = 1.228 primos encontrados em 0,013s

********

99.000.000 ate 100.000.000 = 54.332 primos encontrados em 47,06s
'''