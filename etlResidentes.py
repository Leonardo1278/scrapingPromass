import json
import pandas as pd

# Cargar archivo JSON
with open("residentes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extraer las ofertas principales
rows = []
for plan in data.get("planes", []):
    for fpago in plan.get("fpagos", []):
        for oferta in fpago.get("ofertas", []):
            for cobertura in oferta.get("coberturas", []):
                rows.append({
                    "producto": oferta.get("producto"),
                    "socio": oferta.get("socio"),
                    "descripcion": oferta.get("desc"),
                    "monto_recibo": oferta.get("recibos", {}).get("montorecibo1"),
                    "cobertura": cobertura.get("cobertura"),
                    "deducible": cobertura.get("deducible"),
                    "suma": cobertura.get("suma"),
                    "prima": cobertura.get("prima")
                })

# Convertir a DataFrame y guardar CSV
df = pd.DataFrame(rows)
df.to_csv("ofertas_residentes.csv", index=False, encoding="utf-8-sig")

print("Archivo ofertas_residentes.csv generado.")
