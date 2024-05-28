s = """35
Colombia Australia-NuevaZelanda Australia-NuevaZelanda Colombia
Australia-NuevaZelanda Australia-NuevaZelanda Colombia Australia-NuevaZelanda
Colombia Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Colombia Colombia Colombia Colombia Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda
Colombia Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Colombia Colombia Australia-NuevaZelanda
Colombia Colombia Australia-NuevaZelanda
5
Brasil Brasil Bolivia Bolivia Argentina
0"""

s1 = """Colombia Australia-NuevaZelanda Australia-NuevaZelanda Colombia
Australia-NuevaZelanda Australia-NuevaZelanda Colombia Australia-NuevaZelanda
Colombia Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Colombia Colombia Colombia Colombia Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Australia-NuevaZelanda
Colombia Australia-NuevaZelanda Australia-NuevaZelanda
Australia-NuevaZelanda Colombia Colombia Australia-NuevaZelanda
Colombia Colombia Australia-NuevaZelanda"""

s2 = """Brasil Brasil Bolivia Bolivia Argentina"""

def get_winner(entry: str):
    votes_d = {}
    for country in entry.split(" "):
        if country in votes_d.keys():
            votes_d[country] += 1
            
        else:
            votes_d[country] = 1
    max_v = 0
    max_k = ""        
    for k, v in votes_d.items():
        if v > max_v:
            max_v = v
            max_k = k
            
        if v != max_v != 0:
            max_k = "EMPATE"
            
    return max_k

def solve_exercise1(entrada):
    entradas = []
    lineas = entrada.split("\n")
    palabras = " ".join(lineas)
    palabras = palabras.split(" ")
    new_element = ""
    for palabra in palabras:
        try:
            n_palabras = int(palabra)
            if new_element != "":
                entradas.append(new_element)
                new_element = ""            
        except:
            if new_element == "":
                new_element = palabra
            new_element += " " + palabra

    for element in entradas:
        winner = get_winner(element)
        print(winner)
        
solve_exercise1(s)
            
                   
        
        
