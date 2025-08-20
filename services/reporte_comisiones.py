import pandas as pd
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

COMISION = 0.10

def generar_comisiones(periodo=None):
    contratos = pd.read_excel("data/Cierres.xlsx")  

    if periodo and "fecha" in contratos.columns:
        contratos["fecha"] = pd.to_datetime(contratos["fecha"])
        contratos = contratos[contratos["fecha"].dt.strftime("%Y-%m") == periodo]

    contratos["Canon"] = pd.to_numeric(contratos["Canon"], errors="coerce")

    contratos["comision"] = contratos["Canon"] * COMISION
    resumen = contratos.groupby("captador")["comision"].sum().reset_index()

    with pd.ExcelWriter(f"{OUTPUT_DIR}/Comisiones.xlsx") as writer:
        contratos.to_excel(writer, sheet_name="Detalle", index=False)
        resumen.to_excel(writer, sheet_name="Resumen", index=False)


def actualizar_cartelera():
    cart = pd.read_excel("data/Cartelera.xlsx")
    contratos = pd.read_excel("data/Cierres.xlsx")
    cart = cart[~cart["codigo"].isin(contratos["codigo"])]
    cart.to_excel(f"{OUTPUT_DIR}/Cartelera_Actualizada.xlsx", index=False)
