# Verificación

Revisión del 1 de octubre de 2026.

- Cuatro pruebas del modelo Python: inicio/pausa, límite, secuencia, limpieza, Unicode y JSON.
- Sintaxis de `app.py` e importación de Tkinter comprobadas. La ventana Python no tuvo una prueba manual completa; la captura mostrada es de la versión web.
- Playwright verificó eventos reales al escribir, acciones keydown/keyup, exclusión de controles, pausa, JSON descargado, limpieza y ancho de 360 px.
- Cero errores JavaScript durante el recorrido.
- Capturas del navegador en escritorio, móvil y formato 1440×1080 (4:3), inspeccionadas visualmente.

La demo web es una implementación funcional independiente; no simula captura de otras aplicaciones. No se probó ninguna escucha global porque el producto no la implementa.
