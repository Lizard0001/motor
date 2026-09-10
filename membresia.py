
#definimos la función de membresía triangular donde x es el valor de entrada, a es el punto donde la
# función comienza a aumentar, b es el punto donde la función alcanza su valor máximo (1) y 
# c es el punto donde la función comienza a disminuir. La función retorna un valor de membresía entre 0 y 1.
def membresia_triangular(x, a, b, c):

    if x <= a or x >= c:
        return 0

    elif a < x <= b:
        return (x - a) / (b - a)

    elif b < x < c:
        return (c - x) / (c - b)


# Conjuntos difusos
novato = (0, 0, 5)
intermedio = (2, 5, 8)
experto = (5, 10, 20)

# Años de experiencia de los conductores
conductores = [3, 6, 12]


for experiencia in conductores:

    grado_novato = membresia_triangular(experiencia, *novato)
    grado_intermedio = membresia_triangular(experiencia, *intermedio)
    grado_experto = membresia_triangular(experiencia, *experto)

    grados = {
        "Novato": grado_novato,
        "Intermedio": grado_intermedio,
        "Experto": grado_experto
    }

    categoria = max(grados, key=grados.get)

    print(f"\nExperiencia: {experiencia} años")
    print(f"Novato:      {grado_novato:.2f}")
    print(f"Intermedio:  {grado_intermedio:.2f}")
    print(f"Experto:     {grado_experto:.2f}")
    print(f"Categoría:   {categoria}")