#Remember import random function here:
import random

my_list = [4,5,734,43,45]


for number in range(0,10):      
    my_random_number = random.randint(0,10)
    my_list.append(my_random_number)
print(my_list)
#The magic is here:


"""SOLUCION: SIN hacer el for in UNICAMENTE se agrega UN numero. Si yo creo un loop, asi genero los 10.
Creo una variable a la que igualo la funcion que crea numeros random enteros de 0 a 10.
Por ultimo, a mi lista le hago un .append para agregar mi numeros 10 numeros random."""
