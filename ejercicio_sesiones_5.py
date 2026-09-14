import numpy as np
import skfuzzy as fuzz  

#definir el universo de discurso
X_bono = np.arange(0, 1001, 1)  

#2 simulamos la curva resultante tras aplicar mamdani 
#(para el ejemplo, un conjunto triangular truncado)
curva_resultado = fuzz.trimf(X_bono, [200, 500, 800])

#supongamos que la regla corto el triangulo a una altura maxima de 0.66
curva_truncada = np.fmin(curva_resultado, 0.66)

#desfuzzificacion por el metodo del centroide COG
bono_final_cisp = fuzz.defuzz(X_bono, curva_truncada, 'centroid')

print(f"el bono exacto a pagar es: {bono_final_cisp:.2f}")