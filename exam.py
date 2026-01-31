# suma = 0
# for numero in range(1,101):
#     if numero % 2 == 0:
#         suma += numero
# print(suma)


# resultado = ()
# t = [0, 1, 2, 3, 4, 5]
# x = [0, 10, 20, 30, 40, 50]
# for i in range (0, len(t)-2):
#     dt = t[i+1] - t[i]
#     dx = x[i+1] - x[i]
#     v = dx / dt 
#     print(f"dt = {dt}, v = {v}")


# contador = 0
# h = int(input("ingrese la altura inicial: "))
# v = int(input("ingrese la velocidad inicial: "))
# e = float(input("ingrese el coeficiente de restitucion:  "))
# while h > 0.01:
#     v = e * v
#     h = (v**2) / (2 * 9.81)
#     contador += 1
# print(f"altura: {h}, velocidad: {v}, contador: {contador}") 


# def estado(T):
    # if T <= 0:
        # return "solido"
    # elif T < 100:
        # return "liquido"
    # else:
        # return "gas"
# print(estado(float(input("ingrese la temperatura:  "))))


# h = float(input("ingrese la altura: "))
# m = float(input("ingrese la masa: "))
# energia_potencial = m * h * 9.81
# if energia_potencial < 100:
#     print("baja") 
# elif energia_potencial >= 100 and energia_potencial <= 500:
#     print ("media")
# else:
#     print ("alta")
# print(f"la energia potencial es: {energia_potencial} ")



# entrada = input("Ingrese las aceleraciones separadas por espacio: ")
# valores = entrada.split()   # separa por espacios
# lista = []
# for dato in valores:
#     if dato == "None":
#         continue
#     ac = float(dato)
#     if ac > 50:
#         break
#     lista.append(ac)
# print(lista)



# entrada = [60, 70, 88, 106, 98]
# for dato in entrada:
#     if dato > 100:
#         print("Exceso!")
#         break
#     else:
#         print("Todas seguras")



# def primo(numero):
#     if numero <= 1:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False
#     return True
# numero = int(input("ingresa un numero: "))
# if primo(numero):
#     print("es primo")
# else:
#     print("no es primo")



# f = lambda x: x**2
# g = lambda x: 2*x
# def componer(f,g):
#     h = lambda x: f(g(x))
#     return h
# h = componer(f,g)
# resultado = h(3)
# print(resultado)



# def ordenar(*valores):
#     duplicados = set(valores)
#     orden = sorted(duplicados)
#     return tuple(orden)
# print("Los valores son:" ,ordenar(9,15,7))



# def ecuacion_mrua(s0, v0, a, t):
#     x = s0 + v0*t + ((1)/(2))* a * t**2
#     return  x

# print("La posicion es:" ,ecuacion_mrua(0, 10, 2, 3))



# puntos = ((3,5), (6,7), (2,3))
# distancias = [round((x**2+y**2)**0.5, 2) for x,y in puntos]
# print(distancias)



# energias = [105, 600, 340, 56, 800]
# valores_unicos = [x for x in energias if x > 100]
# print(valores_unicos)



# class rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def area(self):
#         return self.base * self.altura
    
#     def perimetro(self):
#         return (self.base + self.altura)*2
    
# r1 = rectangulo(4,5)
# print(f"el area es: {r1.area()}, el perimetro es: {r1.perimetro()}")