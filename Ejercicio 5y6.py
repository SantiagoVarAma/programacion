#Ejercicio 5: Tablas de verdad en Python

a= input("Ingrese el primer valor: ")
b= input("Ingrese un segundo valor: ")
    #c= input("Ingrese el tercer valor: ")
    #d= input("Ingrese el cuarto valor: ")

#Definir las variables como enteros 

a= int (a)
b= int (b)
    #c= int (c)
    #d= int (d)

print("Esta es la tabla de la verdad de AND") #conjunción
print(str(a==a) + " AND " + str(b==b) + " --> " + str(a==a))
print(str(a==a) + " AND " + str(b>b) + " --> " + str(a<a))
print(str(a>a) + " AND " + str(b==b) + " --> " + str(b!=b))
print(str(a==b) + " AND " + str(b<a) + " --> " + str(b!=b))

print("Esta es la tabla de la verdad de OR") #disyunción
print(str(a==a) + " OR " + str(b==b) + "--> " + str(a==a))
print(str(a==a) + " OR " + str(b!=b) + " --> " + str(b==b))
print(str(a<a) + " OR " + str(b==b) + " --> " + str(b==b))
print(str(a!=a) + " OR " + str(b>b) + " --> " + str(a<a))

print("Esta es la tabla de la verdad de THEN") #condicional
print(str(a==a) + " THEN " + str(b==b) + " --> " + str(a==a))
print(str(a==a) + " THEN " + str(b!=b) + " --> " + str(b<b))
print(str(a<a) + " THEN " + str(b==b) + " --> " + str(b==b))
print(str(a!=a) + " THEN " + str(b>b) + " --> " + str(a==a))









#Ejercicio 6 Python

print("""
¡Buenas! ¿Qué va a llevar vecinito?
1. Huevos   2. Pollo    3. Carne     4. Harina""")

order= input("Escoja una de las opciones: ")
order= str(order)