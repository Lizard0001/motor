#1 base de conociminetos con estructuras de datos
hechos = {"retiro": 50.000, "hora": "10:00", "dia": "lunes", "pais": "colombia"}

rules =[ {"id": "R1", "condiciones": {"retiro": 50.000, "hora": "10:00"}, "conclusion":{ "sospechoso":True}},
        {"id": "R2", "condiciones": {"pais": "Argentina"}, "conclusion":{ "no_sospechoso":True} },
        {"id": "R3", "condiciones": {"sospechoso": True}, "conclusion":{ "cuenta_bloqueada":True} }
        ]

#mostrar el foward chaining
nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in rules:
        #verifica si todas la reglas ya estan iteradas en los hechos
        condiciones_cumplidas = all(hechos.get(k) == v for k, v in regla["condiciones"].items())
        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos: #si es un nuevo hecho, lo agrega a la base de conocimientos
                    hechos[clave] = valor
                    nuevos_hechos = True #se encontro un nuevo hecho, se vuelve a iterar
                    print(f"disparando{regla['id']} ->nuevo hecho: {clave} = {valor}")

print("Hechos finales:", hechos)