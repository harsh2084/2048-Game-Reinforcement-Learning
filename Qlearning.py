import numpy as np

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        # actions: list of possible actions
        self.actions = actions
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.q_table = {}  # Q-table
        
    def choose_action(self, state):
        # With probability epsilon, choose a random action
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(self.actions)
        
        # Otherwise, choose the action with the highest Q-value for the current state
        q_values = [self.q_table.get((state, action), 0) for action in self.actions]
        max_q_value = max(q_values)
        
        # If multiple actions have the same max Q-value, choose randomly among them
        actions_with_max_q_value = [action for action, q_value in enumerate(q_values) if q_value == max_q_value]
        return np.random.choice(actions_with_max_q_value)
    
    def learn(self, state, action, reward, next_state):
        # Q-learning update rule
        predict = self.q_table.get((state, action), 0)
        target = reward + self.gamma * max([self.q_table.get((next_state, a), 0) for a in self.actions])
        self.q_table[(state, action)] = predict + self.alpha * (target - predict)

    def get_state_representation(self, board):
        # Convert the board to a simplified state representation
        state = np.log2(board + 1)
        state[state == -np.inf] = 0
        return tuple(map(tuple, state))

# Initialize agent
agent = QLearningAgent(actions=[0, 1, 2, 3])
