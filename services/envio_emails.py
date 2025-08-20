import pandas as pd
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ASUNTO = "Disponibilidad inmueble {codigo} - {barrio}"
CUERPO = (
    "Hola {propietario},\n\n"
    "Soy {captador} de Inmobiliaria AA. ¿Sigue disponible el inmueble "
    "con código {codigo} ubicado en {barrio}?\n\n"
    "Saludos,\n{captador}\nInmobiliaria AA"
)

def generar_emails(df):
    emails = []
    for _, row in df.iterrows():
        if not row["correo_pp"]: 
            continue
        emails.append({
            "para": row["correo_pp"],
            "asunto": ASUNTO.format(codigo=row["codigo"], barrio=row["barrio"]),
            "cuerpo": CUERPO.format(
                propietario=row["propietario"],
                captador=row["captador_asignado"],
                codigo=row["codigo"],
                barrio=row["barrio"]
            )
        })
    pd.DataFrame(emails).to_excel(f"{OUTPUT_DIR}/Emails_Previo.xlsx", index=False)
    return emails


def enviar_emails(emails):
    print(f"Correos: {len(emails)} (simulación de correo enviado)")
