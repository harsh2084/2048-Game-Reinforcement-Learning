from game_logic import Game2048
from Qlearning import QLearningAgent
import numpy as np


# direction can be: 0 (up), 1 (right), 2 (down), 3 (left)
directions={
    0: 'up',
    1: 'right',
    2:'down',
    3:'left'
}
def train_agent(agent, game, episodes=500):
    scores = []
    for episode in range(episodes):
        game.reset()
        current_state = agent.get_state_representation(game.get_board())
        total_reward = 0
        
        while not game.game_over():
            action = agent.choose_action(current_state)
            prev_score = game.get_score()
            game.move(action)
            reward = game.get_score() - prev_score  # Change in score is the reward
            next_state = agent.get_state_representation(game.get_board())
            
            agent.learn(current_state, action, reward, next_state)
            current_state = next_state
            total_reward += reward
            if episode<2: 
             print("after moving ",directions[action])
             print(game.get_board())
        
        scores.append(total_reward)
    return scores

agent = QLearningAgent(actions=[0, 1, 2, 3])
game = Game2048()
scores = train_agent(agent, game)
print("Average score:", np.mean(scores))
