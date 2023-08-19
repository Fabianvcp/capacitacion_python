""" Escriba un programa en Python que acepte una ruta remota de recurso samba, y lo separe
en nombre(IP) del equipo y ruta
o Entrada: //1.1.1.1/eoi/python
o Salida: host=1.1.1.1; path=/eoi/Python """
import re

ruta_remota = input('ingrese la url a la que quiera acceder por dns:\n')
patron = r'\/\/([\d.]+)\/(.+)'

coincidencias = re.match(patron, ruta_remota)
if coincidencias:
    host = coincidencias.group(1)
    path = coincidencias.group(2)
    if not path.startswith("/"):
        path = "/" + path
    print(f"host={host}; path={path}")
else:
    print('Ruta remota de Samba inválida.')

