"""
Dada la siguiente lista de estudiantes, cree un script usando ciclos, condiciones, variables y si quiere, funciones, que almacene los valores en las siguientes variables:

 promedio_edad -> el promedio de las edades de los estudiantes.
 num_menores_edad -> el numero de estudiantes menores de edad.
 num_mayores_edad -> el numero de estudiantes mayores de edad.
 porcentaje_mujeres -> el porcentaje de mujeres en el grupo.
 porcentaje_hombres -> el porcentaje de hombres en el grupo.
 estudiantes_activos -> numero de estudiantes activos.
"""

my_students = [
    {
        "nombre": "Juan",
        "edad": 23,
        "genero": "M",
        "activo": False
    },
    {
        "nombre": "Maria",
        "edad": 25,
        "genero": "F",
        "activo": True
    },
    {
        "nombre": "Lucia",
        "edad": 35,
        "genero": "F",
        "activo": False
    },
    {
        "nombre": "Pedro",
        "edad": 30,
        "genero": "M",
        "activo": True
    },
    {
        "nombre": "Luis",
        "edad": 15,
        "genero": "M",
        "activo": True
    }
]

# inicialmente creamos una nueva lista para guardar las edades y los generos de cada estudiante

edades= [my_students[0]["edad"], my_students[1]["edad"],my_students[2]["edad"], # lista para edades
 my_students[3]["edad"],my_students[4]["edad"]]

generos = [my_students[0]["genero"], my_students[1]["genero"], my_students[2]["genero"], #lista para los generos 
my_students[3]["genero"], my_students[4]["genero"]]

activos =[my_students[0]["activo"],my_students[1]["activo"],my_students[2]["activo"], #lista estudiantes activos
my_students[3]["activo"],my_students[4]["activo"]]


#cremamos la variables donde vamos a guardar y calcular el promedio usando una cadena de caracteres .
pro_edades = sum(edades)/len(edades)

print(f"el promedio de las edades de los estudiantes son: {pro_edades} \n")
 
#para calcular  cual es el numero de estudiantes menores de edad realizamos un ciclo for con un condicional if
#  y ademas le agregamos una variable contador para que nos diga la cantidad de estudiantes

num_menores_edad = 0  #contadores para deternimar si los estudiantes son mayores o menores de edad
num_mayores_edad = 0
for item in edades:   #ciclo usado para hacer el recorrido dentro de la lista 
   if item <= 18:     # condicional para determinar si el estudiante es mayor o menor de edad
    num_menores_edad+=1
   else:
     num_mayores_edad+=1

mujeres = 0           #contadores para deternimar  los sexos de los estudiantes
hombres = 0
for item in generos:  #ciclo usado para hacer el recorrido dentro de la lista 
   if item == "F":    # condicional para determinar si el estudiante es hombre o mujer
    mujeres+=1 
    porcentaje_mujeres = mujeres*100/5  #formula para determinar el porcentaje de estudiantes mujeres y hombres en la lista
   else:
    hombres +=1
    porcentaje_hombres = hombres*100/5

estudiantes_activos = 0 #contador para deternimar  que estudiantes siguen activos
for item in activos:     #ciclo usado para hacer el recorrido dentro de la lista 
   if item == True:      # condicional para determinar si el sigue activo en la institucion o ya se retiro
    estudiantes_activos +=1

print(f"el numero de estudiantes menores de edad es: {num_menores_edad} \n")
print(f"el numero de estudiantes mayores de edad es: {num_mayores_edad} \n")
print(f"el porcentaje de mujeres en el grupo  es: {porcentaje_mujeres} \n")
print(f"el el porcentaje de hombres en el grupo es: {porcentaje_hombres} \n")
print(f"el numero de estudiantes activos es: {estudiantes_activos} \n")