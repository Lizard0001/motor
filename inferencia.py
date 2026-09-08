#1 base de conociminetos con estructuras de datos
hechos = {"llueve": True, "tiene_paraguas": True}

rules =[ {"id": "R1", "condiciones": {"llueve": True, "tiene_paraguas": False}, "conclusion":{ "se_moja":True}},
        {"id": "R2", "condiciones": {"se_moja": True}, "conclusion":{ "se_resfria":True} },
        {"id": "R3", "condiciones": {"tiene_paraguas": True}, "conclusion":{ "buena salud":True} }
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
