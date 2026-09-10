def memebresia_triangula(x, a, b, c):
    """
    Función de membresía triangular.
    
    Parámetros:
    x : float
        Valor de entrada.
    a : float
        Punto donde la función comienza a aumentar.
    b : float
        Punto donde la función alcanza su valor máximo (1).
    c : float
        Punto donde la función comienza a disminuir.
        
    Retorna:
    float
        Valor de membresía entre 0 y 1.
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
#fuzzificacion de la variable de entrada
#velocidad actual 45
velocidad_actual = 45
#definir los parametros de la funcion de membresia triangular para cada conjunto difuso 
grado_lento = memebresia_triangula(velocidad_actual, 0,10, 30) #lento
grado_moderado = memebresia_triangula(velocidad_actual, 20, 50, 80) #moderado
grado_rapido = memebresia_triangula(velocidad_actual, 60, 90, 120) #rapido

print(f"Grado de pertenencia a 'lento': {grado_lento*100}%")
print(f"Grado de pertenencia a 'moderado': {grado_moderado*100}%")
print(f"Grado de pertenencia a 'rápido': {grado_rapido*100}%")