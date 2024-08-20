## Task 2
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