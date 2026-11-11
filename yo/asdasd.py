lista = ["2", 5, "hola"]

print(lista[1])


### PUNTO 4 

numero = "5"

resultado = numero + 2 

print(resultado)


### PUNTO 5 

for i in range(3):
    print(i)

### PUNTO 8 

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ano = int(input("Ingresa el año actual: "))

while True:
    edad += 1
    ano += 1 
    if edad == 100:
        break

print("Felicidades Shinji, tu edad es ", edad, "estás cada día más cerca de la muerte")
print("Año esperado: ", ano)

### PUNTO 7 

lista = []

while True:
    num = int(input("Digite el número: "))
    
    if num == 0:
        print("Fin del bucle")
        break
    elif num % 2 == 0 and  num % 3 == 0:
        lista.append(num)        
print(lista)
