import numpy as np
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import time
import random
from math import sqrt, log

# Función para resetear el ambiente y actualizar el conteo de victorias
def reset_environment_and_update_wins(env, reward, wins, iterationInfo, cantIterations):
    if reward == 1:
        print("Win\n")
        wins += 1
        iterationInfo.append(cantIterations)
        cantIterations = 0
    else:
        print("Game Over\n")
    return env, wins, iterationInfo, cantIterations

# Parámetros de MCTS
class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.reward = 0.0

    def is_fully_expanded(self):
        return len(self.children) == env.action_space.n

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.reward / child.visits) + c_param * sqrt((2 * log(self.visits) / child.visits))
            for child in self.children.values()
        ]
        return list(self.children.values())[np.argmax(choices_weights)]

    def add_child(self, action, state):
        child = MCTSNode(state=state, parent=self)
        self.children[action] = child
        return child

    def update(self, reward):
        self.visits += 1
        self.reward += reward

# Función de política MCTS
def mcts_policy(env, state, num_simulations=100):
    root = MCTSNode(state=state)

    for _ in range(num_simulations):
        node = root
        env.reset()

        # Selección
        while node.is_fully_expanded():
            node = node.best_child()

        # Expansión
        if not node.is_fully_expanded():
            action = random.choice([a for a in range(env.action_space.n) if a not in node.children])
            next_state, reward, done, _, _ = env.step(action)
            node = node.add_child(action, next_state)

        # Simulación
        while not done:
            action = env.action_space.sample()
            next_state, reward, done, _, _ = env.step(action)

        # Propagación inversa
        while node is not None:
            node.update(reward)
            node = node.parent

    # Elegir la mejor acción
    return max(root.children.keys(), key=lambda x: root.children[x].visits)

# Crear el entorno de Frozen Lake
desc = generate_random_map(size=4)
env = gym.make("FrozenLake-v1", render_mode="human", desc=desc, is_slippery=True)
env.metadata["render_fps"] = 30

# Entrenando al agente con MCTS
training_episodes = 10  # Puedes ajustar el número de episodios de entrenamiento

for episode in range(training_episodes):
    state = env.reset()[0]
    done = False

    while not done:
        action = mcts_policy(env, state)
        next_state, reward, done, _, _ = env.step(action)
        state = next_state

    print(f"Training progress: Episode {episode + 1} of {training_episodes}")

# Probando al agente entrenado con MCTS
wins = 0
iterationInfo = []
cantIterations = 0
testing_episodes = 300  # Número de episodios de prueba

for episode in range(testing_episodes):
    print(f"Iteration no. {episode + 1}")
    cantIterations += 1

    state = env.reset()[0]
    env.render()
    done = False

    while not done:
        action = mcts_policy(env, state)
        next_state, reward, done, _, _ = env.step(action)
        state = next_state
        env.render()
        time.sleep(0.5)

        if done:
            (
                env,
                wins,
                iterationInfo,
                cantIterations,
            ) = reset_environment_and_update_wins(
                env, reward, wins, iterationInfo, cantIterations
            )
            break

print(f"Number of wins: {wins}")
for x in range(len(iterationInfo)):
    print(f"{x + 1}: {iterationInfo[x]}")

env.close()
