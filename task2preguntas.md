## Task 2

### Análisis de los resultados de MCTS y Dyna-Q+

#### a. Comparación de resultados de MCTS y Dyna-Q+

1. **Tasa de éxito**:
   - **MCTS**: La tasa de éxito para MCTS comienza a mejorar rápidamente en los primeros episodios y se estabiliza alrededor del 0.75 después de unas 20,000 iteraciones. El comportamiento parece ser consistente con una tasa de éxito que se acerca a un valor máximo cercano a 0.75 a lo largo del tiempo.
   - **Dyna-Q+**: El comportamiento de la tasa de éxito de Dyna-Q+ es bastante similar a MCTS, con una rápida convergencia inicial, alcanzando un valor estable cercano a 0.78 después de 20,000 episodios y manteniéndose constante a partir de ahí.

2. **Número de pasos hasta el éxito (Convergencia)**:
   - **MCTS**: La cantidad de pasos para alcanzar el éxito se estabiliza en un rango de 40 a 50 pasos por episodio una vez que el agente ha aprendido la tarea. Esto muestra que MCTS logra encontrar una estrategia bastante consistente que toma entre 40 y 50 pasos para completar la tarea de manera repetida.
   - **Dyna-Q+**: En contraste, Dyna-Q+ tiene una variabilidad mucho mayor en el número de pasos para alcanzar el éxito, con algunos episodios requiriendo tan solo unos pocos pasos (alrededor de 50), mientras que otros requieren más de 200 pasos. Esto indica que el comportamiento de Dyna-Q+ es menos consistente en términos de eficiencia por episodio.

#### b. Fortalezas y debilidades de cada enfoque en el contexto de FrozenLake-v1

1. **MCTS**:
   - **Fortalezas**: MCTS parece ser bastante robusto en términos de consistencia. Una vez que ha convergido, el número de pasos por episodio se mantiene estable en un rango relativamente estrecho (40-50 pasos), lo que sugiere que sigue una política bien definida. Su tasa de éxito también se estabiliza en un valor relativamente alto (~0.75).
   - **Debilidades**: A pesar de la consistencia, MCTS puede tener dificultades en entornos extremadamente estocásticos como FrozenLake, ya que la toma de decisiones basada en la búsqueda de árboles puede no capturar completamente la variabilidad del entorno. Además, el proceso de búsqueda puede ser computacionalmente costoso en comparación con otros métodos.

2. **Dyna-Q+**:
   - **Fortalezas**: Dyna-Q+ tiene la ventaja de incorporar actualizaciones de modelos y planificaciones en su aprendizaje, lo que le permite aprender de manera eficiente y tener un comportamiento que converge rápidamente. Además, su tasa de éxito es ligeramente superior a la de MCTS, lo que indica que, en promedio, es capaz de adaptarse mejor a las incertidumbres del entorno.
   - **Debilidades**: La mayor debilidad de Dyna-Q+ es la variabilidad en el número de pasos para completar un episodio. Aunque su tasa de éxito es alta, la eficiencia en términos de pasos es mucho menos estable, lo que podría causar problemas en situaciones donde la eficiencia en el número de pasos es crítica.

#### c. Impacto de la naturaleza estocástica del entorno en el rendimiento de ambos algoritmos

La naturaleza estocástica de FrozenLake introduce incertidumbre en la transición entre los estados, lo que afecta el rendimiento de ambos algoritmos de diferentes maneras:

- **MCTS**: En entornos estocásticos, la búsqueda de árboles puede volverse ineficiente si el árbol generado durante la simulación no es representativo de las transiciones reales debido a la variabilidad del entorno. Esto puede explicar por qué, aunque MCTS es consistente en el número de pasos, su tasa de éxito no alcanza valores tan altos como podría esperarse en un entorno determinista.

- **Dyna-Q+**: La planificación en Dyna-Q+ le permite aprender sobre transiciones estocásticas al realizar actualizaciones basadas en experiencias reales y simuladas. Sin embargo, la estocasticidad también introduce incertidumbre en el número de pasos para completar una tarea, lo que podría explicar la alta variabilidad observada en la cantidad de pasos por episodio, incluso después de muchas iteraciones.

![Average Reward] (./img/average_reward_per_episode)


1. Estrategias de exploración:

a. ¿Cómo influye la bonificación de exploración en Dyna-Q+ en la política en comparación con el equilibrio de exploración-explotación en MCTS? ¿Qué enfoque conduce a una convergencia más rápida en el entorno FrozenLake-v1?

La bonificación de exploración en Dyna-Q+ influye en la política al promover una mayor exploración de estados desconocidos o menos visitados. Esto puede llevar a una convergencia más rápida en el entorno FrozenLake-v1 en comparación con el equilibrio de exploración-explotación en MCTS. MCTS tiende a concentrarse más en la explotación de las acciones que han demostrado ser más prometedoras, lo que puede ralentizar la exploración de todo el espacio de estados. La bonificación de exploración en Dyna-Q+ ayuda a que el agente explore más activamente el entorno, lo que puede resultar en una convergencia más rápida a la política óptima.

2. Rendimiento del algoritmo:

a. ¿Qué algoritmo, MCTS o Dyna-Q+, tuvo un mejor rendimiento en términos de tasa de éxito y recompensa promedio en el entorno FrozenLake-v1? Analice por qué uno podría superar al otro dada la naturaleza estocástica del entorno.

En general, el rendimiento de Dyna-Q+ suele ser mejor que MCTS en el entorno FrozenLake-v1, con una mayor tasa de éxito y recompensa promedio. Esto se debe a que Dyna-Q+ puede aprovechar mejor la naturaleza estocástica del entorno. Al actualizar el modelo interno y planificar utilizando este modelo, Dyna-Q+ puede anticipar y adaptarse mejor a las transiciones probabilísticas. Por otro lado, MCTS se basa más en la exploración aleatoria del árbol de búsqueda, lo que puede ser menos eficiente en entornos con alta aleatoriedad.

3. Impacto de las transiciones estocásticas:

a. ¿Cómo afectan las transiciones probabilísticas en FrozenLake-v1 al proceso de planificación en MCTS en comparación con Dyna-Q+? ¿Qué algoritmo es más robusto a la aleatoriedad introducid por el entorno?

Las transiciones probabilísticas en FrozenLake-v1 afectan más al proceso de planificación en MCTS que a Dyna-Q+. MCTS debe explorar el árbol de búsqueda de forma más exhaustiva para tener en cuenta la aleatoriedad, lo que puede ralentizar la convergencia. En cambio, Dyna-Q+ puede aprovechar su modelo interno para anticipar y adaptarse mejor a las transiciones estocásticas. Esto hace que Dyna-Q+ sea más robusto a la aleatoriedad introducida por el entorno.

4. Sensibilidad de los parámetros:

a. En la implementación de Dyna-Q+, ¿cómo afecta el cambio de la cantidad de pasos de planificación 𝑛 y la bonificación de exploración a la curva de aprendizaje y al rendimiento final? ¿Se necesitarían diferentes configuraciones para una versión determinista del entorno?

En la implementación de Dyna-Q+, el aumento del número de pasos de planificación 'n' y de la bonificación de exploración generalmente mejorará la curva de aprendizaje y el rendimiento final. Un mayor 'n' permite al agente planificar más a fondo utilizando su modelo interno, mientras que una mayor bonificación de exploración lo incentiva a explorar estados menos conocidos. Sin embargo, existe un equilibrio, ya que valores excesivamente altos de estos parámetros pueden llevar a una exploración demasiado agresiva y afectar negativamente el aprendizaje.

En una versión determinista del entorno FrozenLake-v1, se podrían requerir diferentes configuraciones de los parámetros de Dyna-Q+. La bonificación de exploración podría ser menor, ya que la aleatoriedad del entorno ya no sería un factor, y se podrían reducir los pasos de planificación 'n' sin afectar tanto el rendimiento.


