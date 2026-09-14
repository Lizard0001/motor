#grados de membresia actuales (resultados de la fuzzificación)
grados= {
            "rentabilidad_alta":  0.88,
            "impacto_alto": 0.88,
            "riesgo_bajo": 0.91,
            "riesgo_alto": 0.75
        }
#evaluacion de reglas Mamdani
def evaluar_reglas_proyecto(grados):
    #regla 1: si (rentabilidad es alta o impacto_alto) y riesgo_bajo entonces Aprobacion = SEGURA
    fuerza_or = max(grados["rentabilidad_alta"], grados["impacto_alto"])
    activacion_regla1 = min(fuerza_or, grados["riesgo_bajo"])
    
    #regla 2: si riesgo es alto entonces no APROBADO
    activacion_regla2 =  grados["riesgo_alto"]

    return { "SEGURO": activacion_regla1, "DENEGADO": activacion_regla2 }
#ejecucion
fuerza_de_conclusion = evaluar_reglas_proyecto(grados)
print("Fuerza de activacoin para cada conclusion: ", fuerza_de_conclusion)
