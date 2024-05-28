entrada = """10
300 Fuera de juego de Russo
1749 Gol de Olga Carmona
2241 Disparo a puerta de Alba Redondo
2791 Sale Alessia Ruso
2791 Entra Lauren James
3076 Saque de esquina
3333 Tarjeta amarilla para Lauren Hemp
5433 Sale Mariona Caldentey
5433 Entra Alexia Putellas
6327 Fin del partido
3
1
5
7"""


lineas = entrada.split("\n")

casos = int(lineas[0])

eventos = lineas[1:casos+1]

consultas_n = int(lineas[casos+1])

consultas = list(map(int,lineas[-consultas_n:]))

timings = []

for evento in eventos:
    timings.append(int(evento.split(" ")[0]))
    
def consultar(consulta):
    inicio = 0
    final = 0
    min_time = 1000
    curr_events = 0
    last_time = timings[0]
    while final 
         
        