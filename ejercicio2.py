entrada = """4
32 11 6 4 4 3 1
32 1 3 4 4 6 11
128 1 1 1 1 1 1
4 1 1 1 1 0 0"""


for n, line in enumerate(entrada.split("\n")):
    if n == 0:
        continue
    
    else:
        teams_n = int(line.split(" ")[0])
        conf = list(map(int, line.split(" ")[1:]))
        conf = sum(conf)
    print(teams_n - conf)