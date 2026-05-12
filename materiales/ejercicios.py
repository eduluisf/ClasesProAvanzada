# # Ejercicios 1

# a=int(input("Ingrese un número: "))
# b=int(input("Ingrese otro número: "))
# c=int(input("Ingrese otro número: "))


# if a+b>c and a+c>b and b+c>a:
#     print("La suma de los dos primeros números es mayor que el tercero.")

#     if a==b==c:
#         tipo_triangulo = "equilátero"
#     elif a==b or a==c or b==c:
#         tipo_triangulo = "isosceles"
#     else:      
#         tipo_triangulo = "escaleno"


#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#        es_rectangulo = " y rectángulo"
#     else:
#         es_rectangulo = ""

#     print(f"Los números ingresados forman un triángulo {tipo_triangulo}{es_rectangulo}.")

# else:
#     print("Los números ingresados no forman un triángulo.")


# #ejerciicios 2

# tipo_de_carga=input("Ingrese el tipo de carga (Estandar, Fragil o Peligrosa): ").lower()
# peso=float(input("Ingrese el peso de la carga en kg: "))
# horas=int(input("Cuantas horas se debe tardar en entregar el paquete: "))
# distancia=float(input("Ingrese la distancia a recorrer en km: "))

# costo=0

# if tipo_de_carga=="estandar":
#         if distancia<=100:
#             costo=500*distancia
#         elif 100 < distancia <=500:
#             costo=450*distancia
#         else:
#             costo=400*distancia

# elif tipo_de_carga=="fragil":
#     if distancia<=100:
#         costo=700*distancia
#     elif 100 < distancia <=500:
#         costo=650*distancia
#     else:
#         costo=600*distancia

# elif tipo_de_carga=="peligrosa":
#     if distancia<=100:
#         costo=1000*distancia
#     elif 100 < distancia <=500:
#         costo=900*distancia
#     else:
#         costo=850*distancia

# else:
#     print("Tipo de carga no válido.")



# if costo != 0:
#     if peso > 1000:
#         costo = costo*1.15

#     if horas < 24:
#         costo = costo*1.25
#     print(f"El costo total del envío es: ${costo}")
# else:
#     print("No se pudo calcular el costo debido a un tipo de carga no válido.")

# # Ejercicios 3

# nota=float(input("Ingrese la nota del estudiante: "))

# if 0 <= nota <= 100:

#     if nota >= 90:
#         print("La calificación es A y aprueba.")
#         print("¡Excelente trabajo! Sigue así.")

#     elif nota >= 80:
#         print("La calificación es B y aprueba .")
#         print("Muy buen desempeño, puedes mejorar un poco más.")
#         diferencia = 90-nota
#         print(f"Faltan {diferencia} puntos para la A.")

#     elif nota >= 70:
#         print("La calificación es C y aprueba .")
#         print("Buen esfuerzo, pero hay espacio para mejorar.")
#         diferencia = 80-nota
#         print(f"Faltan {diferencia} puntos para la B.")
#     elif nota >= 60:
#         print("La calificación es D y aprueba.")
   
#         diferencia = 70-nota
#         print(f"Faltan {diferencia} puntos para la C.")
#     else:
#         diferencia = 60-nota
#         print("Debes esforzarte más y repasar el contenido.")
#         print(f"Faltan {diferencia} puntos para la D.")
#         print("La calificación es F y reprueba.")
# else:
#     print("Nota no válida. Por favor, ingrese una nota entre 0 y 100.")


#Ejercicios 4

por