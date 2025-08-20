# 💻 Automatización Python

Este proyecto automatiza el proceso de gestión inmobiliaria, eliminando tareas manuales repetitivas como la asignación de captadores, el envío de correos, el cálculo de comisiones y la actualización de la cartelera de inmuebles.

---

## 📊 Estructura de datos

Datos de entrada

Cartelera.xlsx → listado de inmuebles disponibles.

Cierres.xlsx → contratos cerrados (inmuebles arrendados).

SubZonas.xlsx → asignación de barrio → captador.


Datos de salida (carpeta output/)

Cartelera_Asignada.xlsx → cartelera con captador asignado automáticamente.

Emails_Previo.xlsx → previsualización de los correos a enviar.

Comisiones.xlsx → cálculo de comisiones (detalle por contrato y resumen por captador).

Cartelera_Actualizada.xlsx → cartelera depurada, quitando los inmuebles que ya aparecen en Cierres.xlsx (es decir, solo muestra los inmuebles aún disponibles).

---

### 📌 Manejo de errores
- Si falta el correo del propietario → se deja vacío en `Emails_Previo.xlsx`.  
- Si un barrio no tiene captador en SubZonas → se marca como `SIN ASIGNAR`.  
- Si la columna `Canon` no es numérica → se convierte a número antes de calcular.  
- Si el archivo Excel está abierto → se muestra error de permiso (hay que cerrarlo).  

---

## 🚀 Instrucciones de ejecución

1. Instalar dependencias:
   ```bash
Instalar dependencias
pip install -r requirements.txt

Asignar captadores
python main.py --asignar

Generar correos de prueba
python main.py --emails

Generar reporte de comisiones
python main.py --comisiones

Ejecutar todos los archivos 
python main.py --asignar --emails --comisiones --actualizar

---




