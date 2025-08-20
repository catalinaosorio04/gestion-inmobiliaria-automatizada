import pandas as pd
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def asignar_captadores():
    cartelera = pd.read_excel("data/Cartelera.xlsx")
    subzonas = pd.read_excel("data/SubZonas.xlsx")

    cartelera["barrio_norm"] = cartelera["barrio"].str.lower().str.strip()
    subzonas["barrio_norm"] = subzonas["barrio"].str.lower().str.strip()

    subzonas.rename(columns={
        "Captador": "captador_asignado",
        "Correo": "correo_captador"
    }, inplace=True)

    merged = cartelera.merge(
        subzonas[["barrio_norm", "sede", "captador_asignado", "correo_captador"]],
        on="barrio_norm", how="left"
    )

    merged["captador_asignado"].fillna("SIN ASIGNAR", inplace=True)

    merged.to_excel(f"{OUTPUT_DIR}/Cartelera_Asignada.xlsx", index=False)
    return merged