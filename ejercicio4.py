#Suma de Subarrays Contiguos:

#  Dado un array de enteros y un entero k, 
#  escribe una función que encuentre la suma 
#  máxima de cualquier subarray contiguo de 
#  longitud k.

l = [1,2,3,4,2,2,4,4,5,9,2,1,1]

k = 3

start = 0
end = 3
max_sum = 0

while end != len(l):
    curr_sum = sum(l[start:end+1])
    max_sum = max(max_sum, curr_sum)
    end += 1
    start += 1
    print(max_sum)


