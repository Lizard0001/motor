#memoria de trabajo
variables_estado_pc={
    "ventilador_prendido":False,
    "temperatura_grados_celsius":90,
    "procesador_sobrecalentado":True,  
    "memoria_ram_usada":8.2,
    "ping_respuesta":True,
    "cpu_uso":75,
    }
#base de raglas de motor de inferencia estatico
def diagnosticar_servidor(hechos):
    #regla de sobrecalentamiento
    if hechos["temperatura_grados_celsius"] > 80 and hechos["procesador_sobrecalentado"] and not hechos["ventilador_prendido"]:
        return "ALERTA: Servidor sobrecalentado, apagar inmediatamente"
    #regla de uso de CPU alto
    if hechos["cpu_uso"] > 90:
        return "ADVERTENCIA: Uso de CPU muy alto, revisar procesos"
    #regla de memoria RAM insuficiente
    if  hechos["memoria_ram_usada"] > 8:
        return "ADVERTENCIA: Memoria RAM insuficiente, considerar actualizacion capacidad de memoria"
    #regla de ping fallido
    if not hechos["ping_respuesta"]:
        return "ERROR: No hay respuesta al ping, verificar conexión de red"
    
    return "SERVIDOR OPERANDO NORMALMENTE"

#ejecucion del motor de inferencia
diagnostico = diagnosticar_servidor(variables_estado_pc)
print("Diagnóstico del servidor:", diagnostico)