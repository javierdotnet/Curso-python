# Variable global

a = 5

# Funcion


def f1(a, b):
    sumar = a + b
    return sumar


def f2(b):
    global sumar  # convierte una variable local en global
    sumar = a + b
    return sumar

print(f1(3, 3))
print(f2(4))

print(sumar)