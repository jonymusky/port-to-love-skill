# Port to LÖVE

Una skill para agentes de código que te ayuda a llevar un juego existente a **LÖVE (Love2D) y Lua**, conservar cómo responde a los controles y entregar un archivo `.love` jugable. Incluye una guía para la portátil Anbernic RG353V y PortMaster.

```bash
npx skills add jonymusky/port-to-love-skill
```

Ejecutá el comando desde el proyecto que querés portar y elegí tu agente en el instalador. Si preferís instalarla a mano en Codex, copiá `skills/port-to-love` a `~/.codex/skills/` o a la carpeta `skills/` de tu `CODEX_HOME`.

## Pedile un port a tu agente

> Usá $port-to-love para portar este juego de navegador a LÖVE 11.5. Conservá la carga manual del ataque y las partidas guardadas. Prepará un .love y probalo con dos mandos.

> El juego abre en mi Mac pero vuelve al menú de Ports en la RG353V. Revisá el registro del lanzador y compará el paquete de la SD con el que probamos en escritorio.

## Qué conviene probar

| Momento | Prueba concreta |
|---|---|
| Al trasladar los controles | Sostené un ataque después de llenar la barra. Comprobá que el daño se aplique una sola vez al soltar el botón. |
| Al cambiar la resolución | Recorré los bordes del escenario. Comprobá que se vea al personaje durante una caída y que el proyectil siga saliendo de su mano. |
| Al empaquetar | Abrí el archivo que vas a distribuir. Probá una escena que cargue gráficos y audio después del menú. |
| Al instalar en la consola | Compará el archivo leído desde la SD con el original. Si vuelve a Ports, identificá en el registro qué ejecutable se inició y cómo terminó. |

## Verificar un paquete sin agente

Desde una copia de este repositorio, ejecutá el verificador con Python 3. Comprueba que `main.lua` esté en la raíz del ZIP, detecta nombres duplicados y rutas problemáticas, y lee los archivos para verificar su integridad. Después podés abrir ese mismo paquete con LÖVE.

```bash
python3 skills/port-to-love/scripts/check_love.py release/juego.love
love release/juego.love
```

## De dónde salió

La escribí al portar **Tenkū Arena**, un juego de peleas isométrico con 14 luchadores. El paquete de la microSD abrió en la Mac y pasó las pruebas de los 28 ataques. En la RG353V, el registro mostró un `Bus error`. Al comparar el motor con la copia de referencia encontré una biblioteca a la que le faltaban 59.888 bytes. Ese caso dio origen a la guía de diagnóstico. [Leer la historia y ver las capturas](https://me.jonymusky.com/es/blog/tenku-arena-port-to-love)

- [Flujo de porting y pruebas de gameplay](skills/port-to-love/SKILL.md)
- [Instalación y diagnóstico en RG353V](skills/port-to-love/references/rg353v.md)
- [Código del verificador de paquetes](skills/port-to-love/scripts/check_love.py)
