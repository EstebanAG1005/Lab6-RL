import numpy as np
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import random
import time
from math import sqrt  # Importar sqrt desde el módulo math


class DynaQPlusAgent:
    def __init__(self, env, alpha=0.1, gamma=0.99, epsilon=0.1, n=10, exploration_bonus=0.01):
        self.env = env
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Probabilidad de exploración
        self.n = n  # Número de pasos de planificación
        self.exploration_bonus = exploration_bonus  # Bonificación de exploración

        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))  # Tabla Q
        self.model = {}  # Modelo del entorno
        self.time_since_last_visit = np.zeros((env.observation_space.n, env.action_space.n))  # Contador de visitas

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return self.env.action_space.sample()  # Acción aleatoria (exploración)
        else:
            return np.argmax(self.q_table[state])  # Acción con mayor valor Q (explotación)

    def learn(self, state, action, reward, next_state):
        # Actualización de Q-learning
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state, best_next_action]
        self.q_table[state, action] += self.alpha * (td_target - self.q_table[state, action])

        # Actualizar el modelo del entorno
        self.model[(state, action)] = (reward, next_state)
        self.time_since_last_visit[state, action] = 0  # Resetear el contador de tiempo desde la última visita

        # Incrementar el contador de tiempo para todas las acciones
        self.time_since_last_visit += 1

        # Pasos de planificación (simulación)
        for _ in range(self.n):
            s, a = random.choice(list(self.model.keys()))  # Escoger una experiencia aleatoria del modelo
            r, s_next = self.model[(s, a)]
            exploration_reward = self.exploration_bonus * sqrt(
                self.time_since_last_visit[s, a])  # Bonificación de exploración
            td_target = r + exploration_reward + self.gamma * self.q_table[s_next, np.argmax(self.q_table[s_next])]
            self.q_table[s, a] += self.alpha * (td_target - self.q_table[s, a])

    def train(self, episodes):
        for episode in range(episodes):
            state = self.env.reset()[0]
            done = False
            total_reward = 0
            steps = 0

            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _, _ = self.env.step(action)
                self.learn(state, action, reward, next_state)
                state = next_state

                total_reward += reward
                steps += 1

            # Mostrar información del episodio
            print(f"Episode {episode + 1}/{episodes}")
            print(f"Total reward: {total_reward}")
            print(f"Steps taken: {steps}")
            print(f"Final state: {state}")
            print("-" * 30)

    def test(self, episodes=100):
        wins = 0
        for episode in range(episodes):
            state = self.env.reset()[0]
            done = False
            total_reward = 0
            steps = 0

            while not done:
                action = np.argmax(self.q_table[state])  # Tomar la mejor acción según la tabla Q
                next_state, reward, done, _, _ = self.env.step(action)
                state = next_state
                total_reward += reward
                steps += 1

                if done and reward == 1:
                    wins += 1

            # Mostrar información del episodio de prueba
            print(f"Test Episode {episode + 1}/{episodes}")
            print(f"Total reward: {total_reward}")
            print(f"Steps taken: {steps}")
            print(f"Final state: {state}")
            print("-" * 30)

        print(f"Number of wins in {episodes} episodes: {wins}")
        return wins


# Crear el entorno de Frozen Lake
desc = generate_random_map(size=4)
env = gym.make("FrozenLake-v1", render_mode="human", desc=desc, is_slippery=True)
env.metadata["render_fps"] = 30

# Crear un agente Dyna-Q+
agent = DynaQPlusAgent(env, alpha=0.1, gamma=0.99, epsilon=0.1, n=10, exploration_bonus=0.01)

# Entrenar al agente
training_episodes = 1000
agent.train(training_episodes)

# Probar al agente entrenado
testing_episodes = 100
wins = agent.test(testing_episodes)

env.close()
