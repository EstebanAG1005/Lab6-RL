import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from tqdm import tqdm  # Progress bar library
from scipy.ndimage import uniform_filter1d  # For smoothing
import os  # For directory creation

class OptimizedMCTS:
    def __init__(self, env, num_simulations=100, exploration_weight=1.4):
        self.env = env
        self.num_simulations = num_simulations
        self.exploration_weight = exploration_weight
        self.Q = {}  # Cumulative reward table
        self.N = {}  # Visit count table
        self.actions = list(range(env.action_space.n))

    def simulate(self, state):
        """Simulate a random sequence of actions until a terminal state"""
        total_reward = 0
        done = False

        # Simulate until the terminal state
        while not done:
            action = random.choice(self.actions)  # Random actions
            state, reward, done, _, _ = self.env.step(action)
            total_reward += reward

        return total_reward

    def expand(self, state):
        """Expand a new state in the search tree"""
        action = random.choice(self.actions)
        new_state, reward, done, _, _ = self.env.step(action)
        return new_state, reward, done

    def best_action(self, state):
        """Select the best action using Upper Confidence Bound for Trees (UCT)"""
        best_action = None
        best_value = -float('inf')

        # Iterate over all possible actions
        for action in self.actions:
            state_action = (state, action)

            # Initialize values if we encounter this state-action pair for the first time
            if state_action not in self.Q:
                self.Q[state_action] = 0
                self.N[state_action] = 1  # Initialize to 1 to avoid division by zero

            # Calculate exploitation and exploration
            exploitation = self.Q[state_action] / self.N[state_action]
            exploration = self.exploration_weight * math.sqrt(
                math.log(sum(self.N.get((state, a), 1) for a in self.actions)) / self.N[state_action]
            )
            value = exploitation + exploration

            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    def tree_policy(self, state):
        """Action selection using UCT in the tree"""
        while True:
            action = self.best_action(state)
            new_state, reward, done = self.expand(state)
            state = new_state
            if done:
                break
        return state, reward

    def backpropagate(self, path, reward):
        """Backpropagate the rewards obtained in the simulation"""
        for state_action in path:
            if state_action not in self.Q:
                self.Q[state_action] = 0
                self.N[state_action] = 0
            self.Q[state_action] += reward
            self.N[state_action] += 1

    def run(self, total_episodes=100000):
        """Run the MCTS algorithm with progress display"""
        success_rate = []
        rewards_per_episode = []
        steps_per_episode = []

        # Use tqdm for progress display
        for episode in tqdm(range(total_episodes), desc="Running MCTS", unit="episode"):
            state, _ = self.env.reset()
            done = False
            episode_reward = 0
            steps = 0
            path = []

            while not done:
                action = self.best_action(state)
                path.append((state, action))
                state, reward, done, _, _ = self.env.step(action)
                episode_reward += reward
                steps += 1

            # Backpropagate the reward through the path
            self.backpropagate(path, episode_reward)

            # Record metrics
            success_rate.append(1 if reward == 1 else 0)
            rewards_per_episode.append(episode_reward)
            steps_per_episode.append(steps)

        return success_rate, rewards_per_episode, steps_per_episode

def plot_results(success_rate, rewards_per_episode, steps_per_episode):
    """Generate and save the requested plots to the 'img' folder"""
    
    # Create the 'img' directory if it doesn't exist
    os.makedirs("img", exist_ok=True)
    
    episodes = np.arange(1, len(success_rate) + 1)

    # Success rate per episode
    plt.figure(figsize=(10, 6))
    success_rate_per_episode = np.cumsum(success_rate) / episodes
    plt.plot(episodes, success_rate_per_episode, label="Success Rate", color='b')
    plt.title("Success Rate per Episode (MCTS)")
    plt.xlabel("Episodes")
    plt.ylabel("Cumulative Success Rate")
    plt.legend()
    plt.grid(True)
    plt.savefig("img/success_rate_per_episode.png")  # Save the figure
    plt.show()

    # Average reward per episode (Smoothed)
    plt.figure(figsize=(10, 6))
    smoothed_rewards = uniform_filter1d(rewards_per_episode, size=500)  # Smoothing for better visibility
    plt.plot(episodes, smoothed_rewards, label="Smoothed Reward per Episode", color='g')
    plt.title("Average Reward per Episode (Smoothed) (MCTS)")
    plt.xlabel("Episodes")
    plt.ylabel("Average Reward")
    plt.legend()
    plt.grid(True)
    plt.savefig("img/average_reward_per_episode.png")  # Save the figure
    plt.show()

    # Convergence rate (Steps per episode) (Smoothed)
    plt.figure(figsize=(10, 6))
    smoothed_steps = uniform_filter1d(steps_per_episode, size=500)  # Smoothing for better visibility
    plt.plot(episodes, smoothed_steps, label="Smoothed Steps per Episode", color='r')
    plt.title("Convergence Rate (Smoothed Steps per Episode) (MCTS)")
    plt.xlabel("Episodes")
    plt.ylabel("Number of Steps")
    plt.legend()
    plt.grid(True)
    plt.savefig("img/convergence_rate_per_episode.png")  # Save the figure
    plt.show()

if __name__ == "__main__":
    env = gym.make("FrozenLake-v1", render_mode='ansi', is_slippery=True)
    mcts = OptimizedMCTS(env)
    
    # Run MCTS with 100,000 episodes and show progress
    success_rate, rewards_per_episode, steps_per_episode = mcts.run(total_episodes=100000)

    # Plot and save the results as images
    plot_results(success_rate, rewards_per_episode, steps_per_episode)
