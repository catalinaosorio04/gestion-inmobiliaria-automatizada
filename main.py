import argparse
from services.asignacion_captadores import asignar_captadores
from services.envio_emails import generar_emails, enviar_emails
from services.reporte_comisiones import generar_comisiones, actualizar_cartelera

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--asignar", action="store_true")
    parser.add_argument("--emails", action="store_true")
    parser.add_argument("--comisiones", action="store_true")
    parser.add_argument("--actualizar", action="store_true")
    parser.add_argument("--periodo", type=str, help="Periodo YYYY-MM")
    args = parser.parse_args()

    df_asignada = None
    if args.asignar:
        df_asignada = asignar_captadores()

    if args.emails:
        if df_asignada is None:
            import pandas as pd
            df_asignada = pd.read_excel("output/Cartelera_Asignada.xlsx")
        emails = generar_emails(df_asignada)
        enviar_emails(emails)

    if args.comisiones:
        generar_comisiones(periodo=args.periodo)

    if args.actualizar:
        actualizar_cartelera()
