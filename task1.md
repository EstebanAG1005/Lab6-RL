## Task 1
1. ¿Qué es Prioritized sweeping para ambientes determinísticos?
Es una técnica de planificación que actualiza los valores de estado de manera eficiente, priorizando las actualizaciones más significativas. En ambientes determinísticos, actualiza los estados cuyas estimaciones de valor han cambiado significativamente, propagando rápidamente la información relevante.

2. ¿Qué es Trajectory Sampling?
Es un método de muestreo que se centra en recopilar experiencias a lo largo de trayectorias completas en lugar de estados individuales. Esto permite una exploración más coherente del espacio de estados y acciones, lo que puede ser beneficioso para aprender políticas efectivas.

3. ¿Qué es Upper Confidence Bounds para Árboles (UCT por sus siglas en inglés)?
UCT es un algoritmo utilizado en la búsqueda de árboles Monte Carlo. Equilibra la exploración y la explotación al seleccionar acciones basándose en su valor estimado y la incertidumbre asociada. Es particularmente útil en problemas con espacios de búsqueda grandes, como en juegos.

### Referencias:
- https://paperswithcode.com/method/prioritized-sweeping
- https://iopscience.iop.org/article/10.1088/1367-2630/abd7bd/meta
- https://www.linkedin.com/pulse/upper-confidence-bounds-trees-yeshwanth-n-jnfwc/