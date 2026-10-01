# Diseño del laboratorio

Qué es: banco de pruebas de eventos de entrada. Para quién: desarrolladores y usuarios que quieren inspeccionar su teclado. Objetivo: escribir, pausar, observar y exportar una sesión real.

Ciruela #38234F para texto, lavanda #F3EFF8 para fondo, blanco #FFFFFF para áreas de trabajo, violeta #7445A5 para acción, gris #665B72 para secundario y verde #256A50 para registro activo. Segoe UI para controles y Consolas para eventos. Layout alineado a la izquierda: escritura y teclado visual junto a consola.

```text
marca                              código Python
título                       alcance de captura
iniciar / pausar / limpiar
área de prueba        | eventos en directo
teclado visual        | exportar JSON
```

La pulsación real ilumina una tecla y aparece en consola. Registro explícito y limitado, sin estética de intrusión, cifras inventadas ni simulación de captura global. Se comprueba 360 px, foco visible, pausa y descarga real.
