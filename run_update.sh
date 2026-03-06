#!/bin/bash

# Ruta real de OneDrive en macOS para evitar problemas de enlaces simbólicos
DIR="/Users/gcasanga/Library/CloudStorage/OneDrive-AlignTechnology,Inc/Movies"
cd "$DIR"

# 1. Ejecutar el script de Python para actualizar las fechas
python3 actualiza_epg.py

# 2. Copiar el resultado a dummy.xml (que es lo que GitHub espera)
# Usaremos 'tu_archivo_actualizado.xml' como backup si el principal falla
if [ -f "tu_archivo_actualizado.xml" ]; then
    cp tu_archivo_actualizado.xml dummy.xml
fi

# 3. Preparar los cambios para Git
git add dummy.xml actualiza_epg.py tu_archivo.xml .gitignore run_update.sh

# 4. Hacer commit (solo si hay cambios reales en el XML)
if ! git diff-index --quiet HEAD --; then
    git commit -m "Auto-update EPG: $(date +'%Y-%m-%d %H:%M:%S')"
    
    # 5. Push a tu GitHub personal
    # Si tienes problemas de permisos, se detendrá aquí con un mensaje.
    git push origin main
fi
