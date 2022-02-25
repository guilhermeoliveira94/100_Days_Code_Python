import sys

segundos = int(input())

minutos = (sys.stdin.readline(1))
segundos = int(segundos - (minutos * 60))
horas = math.floor(int(((segundos / 60)/60)))
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))



import sys

a = int(sys.stdin.readline(1))  # Lê a linha de entrada

print(a)  # Imprime o dado

segundos = int(input())

minutos = #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))