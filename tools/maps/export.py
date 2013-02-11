#!/usr/bin/env python
import commands
import sys

SRC_FILE = 'tmx/map.tmx'

TEMP_FILE = SRC_FILE+'.json'

mode = sys.argv[1] if len(sys.argv) > 1 else 'client'
if mode == 'client':
    DEST_FILE = '../../client/maps/world_client' # Esto le ahorrará dos archivos (Ver exportmap.js)
else:
    DEST_FILE = '../../server/maps/world_server.json'

# Convertir el archivo TMX Temporalmente a un archivo JSON
print commands.getoutput('./tmx2json.py '+SRC_FILE+' '+TEMP_FILE)

# Exportando Mapa
print commands.getoutput('./exportmap.js '+TEMP_FILE+' '+DEST_FILE+' '+mode)

# Eliminar archivos temporales JSON
print commands.getoutput('rm '+TEMP_FILE)

# Enviar una notificación Growl cuando el proceso de exportación se ha completado
print commands.getoutput('growlnotify --appIcon Tiled -name "Map export complete" -m "'+DEST_FILE+' was saved"')
