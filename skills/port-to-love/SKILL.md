---
name: port-to-love
description: Port an existing game to LÖVE (Love2D) and Lua, preserving gameplay, adapting controls and rendering, and packaging a playable .love. Includes an optional RG353V and PortMaster deployment workflow.
---

# Portar un juego a LÖVE

Partí del juego que se puede jugar. Localizá sus entradas, reglas, datos, recursos y guardado. Armá un inventario breve de modos, pantallas y acciones que defina qué significa completar ese port. Si el encargo incluye todo el juego, usá una escena representativa para probar la arquitectura y luego recorré el inventario completo.

## Preservar el comportamiento

- Identificá si los tiempos del original están expresados en segundos, frames o ticks. Conservá la frecuencia de simulación cuando determine ventanas de combos, físicas o reglas. Con un acumulador en `love.update`, guardá las pulsaciones entre ticks y consumí cada una una sola vez. Leé por separado pulsación, botón sostenido y liberación.
- Conservá las coordenadas y colisiones del mundo. Aplicá la escala y la proyección en la vista. Al adaptar la relación de aspecto, verificá los extremos del mapa, el HUD y los indicadores de peligro. Cuando cambie el tamaño de una hoja de sprites, escalá también los puntos de anclaje de manos, proyectiles y sombras.
- Importá las tablas de balance desde su fuente cuando sea posible. Al convertir índices de base cero a tablas Lua, distinguí el índice de acceso del identificador persistido. En Lua, cero y la cadena vacía se evalúan como verdaderos. Probá explícitamente temporizadores en cero y estados como empate o primer personaje.
- Mantené una identidad estable de guardado con `love.conf` y usá `love.filesystem`. Probá cargar datos anteriores cuando agregues opciones. Separá el guardado de pruebas para que los tests del circuito o los desbloqueos puedan repetirse.
- Usá fuentes de audio en streaming para música y fuentes estáticas reutilizables para efectos cortos. Comprobá el cambio de escena, volumen cero, pausa, recuperación del foco y desconexión de un mando. En multijugador local, verificá el segundo dispositivo por separado.

## Empaquetar y probar

Generá el archivo .love con `main.lua` en la raíz y rutas que coincidan en mayúsculas y minúsculas con los nombres del código. Incluí sólo los recursos de ejecución. Si el proyecto ya cuenta con un empaquetador, usalo. El helper `python3 scripts/check_love.py juego.love`, ejecutado desde esta skill, verifica la estructura y la integridad del ZIP sin extraerlo.

Ejecutá el **archivo empaquetado** con la versión de LÖVE elegida. Compará una secuencia de entradas contra el original y verificá sus resultados observables, como la posición al aterrizar, el daño al liberar una carga o el guardado después de ganar. Recorré los modos y asegurate de que se decodifiquen los recursos de uso tardío. Indicá qué probaste en escritorio y qué pudiste probar en el dispositivo final.

Para consola RG353V, SD o PortMaster, consultá [el flujo de instalación en portátil](references/rg353v.md).
