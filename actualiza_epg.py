import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import os

# Cambiar al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cargar el archivo XML
# Verificamos si tu_archivo.xml existe para evitar errores
if not os.path.exists('tu_archivo.xml'):
    # Si por alguna razón no existe, intentamos usar dummy.xml como base 
    # o crear una advertencia.
    print("Error: tu_archivo.xml no encontrado.")
else:
    tree = ET.parse('tu_archivo.xml')
    root = tree.getroot()

    # Obtener la fecha actual en UTC
    current_date = datetime.now(timezone.utc)

    # Establecer la fecha de inicio como la fecha actual
    formatted_start_date = current_date.strftime("%Y%m%d%H%M%S %z")

    # Establecer la fecha de fin como 30 días después de la fecha actual
    future_date = current_date + timedelta(days=30)
    formatted_stop_date = future_date.strftime("%Y%m%d%H%M%S %z")

    # Actualizar las fechas de inicio y fin de cada programa en el archivo XML
    for program in root.iter('programme'):
        program.set('start', formatted_start_date)
        program.set('stop', formatted_stop_date)

    # Guardar los cambios en el archivo XML
    tree.write('tu_archivo_actualizado.xml', encoding='utf-8', xml_declaration=True)
    print("XML actualizado correctamente.")
