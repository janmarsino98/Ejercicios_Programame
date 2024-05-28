#Dígito posición impar => *3 & suma menor dígito a la derecha
# Dígito par => *2 & suma mayor dígito a la izquierda

entrada = """3
7214
10
1001"""


def tratar_entrada(numero):
    nums = []
    for character in numero:
        i = int(character)
        nums.append(i)
    value = 0
    for n, num in enumerate(nums):
        if (n+1) % 2 == 1:
            value += num*3 + min(nums[n+1:])
            
        else:
            value += num * 2 + max(nums[:n])
            
    return value
    

def resolver(entrada: str):
    for n, line in enumerate(entrada.split("\n")):
        if n == 0: 
            continue
        else:
            print(tratar_entrada(line))
        
        
resolver(entrada)
    