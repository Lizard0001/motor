#diccionario de estados actuales de los grados de membresia (resultados de la fuzzificación)
grados= {"desempeno_bajo": 0.02, "desempeno_alto": 0.98, 
         "antiguedad_corta": 0.1, "antiguedad_larga": 0.9 
         }

def evaluar_reglas_empleado(grados):
    #regla 1: si (desempeno es alto o antiguedad es larga) entonces bono alto = SEGURO
    fuerza_medida= max(grados["desempeno_alto"], grados["antiguedad_larga"])
    fuerza_medida2= min(fuerza_medida, grados["desempeno_alto"])
    activacion_regla1 = fuerza_medida2
    
    fuerza_or2= min(grados["desempeno_alto"], grados["antiguedad_corta"])
    activacion_regla2 =  fuerza_or2
    
    activacion_regla3 =  min(grados["desempeno_bajo"], grados["antiguedad_corta"])
    activacion_regla4 =  min(grados["desempeno_alto"], grados["antiguedad_corta"])

    return { "BONO ALTO": activacion_regla1, "SIN BONO": activacion_regla2,
            "BONO MEDIO": activacion_regla4, "BONO MINIMO": activacion_regla3 }

#ejecucion
fuerza_de_conclusion = evaluar_reglas_empleado(grados)
print("Fuerza de activacoin para cada conclusion: ", fuerza_de_conclusion)
