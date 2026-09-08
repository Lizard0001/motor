#memoria de trabajo
estado_cliente={
    "ingresos":50001,
    "historial_crediticio":"bueno",
    "deuda_actual":12000,
    "avalista":True
}
#base de reglas y motor de inferencia estatico
def motor_evaluacion_credito(hechos):
    #regla de rechazo absolutapor deuda actual alta
    if hechos["deuda_actual"] > 10000 and not hechos["avalista"]:
        return "RECHAZADO: por deuda actual alta y sin avalista"
    #rega de aprobacion
    if hechos["ingresos"] > 50000 and hechos["historial_crediticio"] == "bueno":
        return "APROBADO: ingresos y historial crediticio adecuados y avalista presente"
    #regla por defecto(fallback)
    
    return "EN REVISION MANUAL : no cumple criterios de aprobación automática"

#ejecucion del motor de inferencia
decision = motor_evaluacion_credito(estado_cliente)
print("Decisión de crédito:", decision)
