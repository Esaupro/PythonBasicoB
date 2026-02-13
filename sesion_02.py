#Tuplas
mi_Tupla = (2, 4)
print("Mi tupla: ",mi_Tupla)

#lista
mi_lista = [1, 3.1416, "Esau", mi_Tupla]
print("El primer elemento de mi lista: ",mi_lista[0])
print("El cuarto elemento de mi lista: ",mi_lista[3])
print("El tercer elemento de mi lista: ",mi_lista[2])

#Diccionarios
mi_Diccionario = {
     "mi_lista": mi_lista,
    "nombre": "Esau",
    "Pi" : 3.1416,
    "Tel": "355436555"
}
print("llave para accesar a mi diccionario mi_lista ",mi_Diccionario["mi_lista"])
print("llave para accesar a mi diccionario Pi ",mi_Diccionario["Pi"])
print("llave para accesar a mi diccionario Tel ",mi_Diccionario["Tel"])