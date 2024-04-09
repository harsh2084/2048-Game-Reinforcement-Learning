
### Report on Solving the 2048 Game using Reinforcement Learning

#### What is the 2048 game?

The 2048 game is a sliding puzzle game played on a 4x4 board. The objective of the game is to combine tiles with the same number, which then merge to form a tile with the sum of the two numbers. The game starts with two tiles, usually of value 2 or 4. Players use arrow keys (or swipes on mobile devices) to slide all tiles in one of the four directions (up, down, left, right). If two tiles of the same number collide during the slide, they merge into a single tile with their combined value. The game ends when the board is full and no further moves are possible. The goal is to create a tile with the value 2048, though play can continue to achieve even higher values.

#### How is it solved by Reinforcement Learning?

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize some notion of cumulative reward. In the context of the 2048 game:

- **Environment**: The 2048 game board.
- **Agent**: The RL model that decides which move to make (up, down, left, right).
- **State**: The current configuration of the game board.
- **Action**: One of the four possible moves.
- **Reward**: The change in the game's score after a move. This gives the agent feedback about how good the move was.

The agent learns an optimal strategy by playing the game repeatedly, receiving feedback through rewards, and adjusting its strategy to maximize future rewards.

#### Why using Q-learning instead of any other models?

Q-learning is a model-free, off-policy RL algorithm used to find the optimal action-selection policy for a given finite Markov decision process. Here's why it's a suitable choice for the 2048 game:

- **Simplicity**: Q-learning is straightforward to implement, making it a good starting point for many RL problems.
- **Model-free**: Q-learning doesn't require a model of the environment, making it suitable for situations where the model is unknown or difficult to build.
- **Off-policy**: Q-learning learns the optimal policy even when it's not following it, which allows for exploration.

While there are other RL algorithms, like Deep Q Networks (DQN) and Policy Gradient methods, Q-learning is a foundational algorithm that provides a good balance between complexity and performance for many problems, including 2048.

#### What is the accuracy?

In our simplified implementation, the agent achieved an average score of approximately 253.66 over 500 episodes. While "accuracy" in the traditional sense doesn't apply to RL problems, the average score provides an indication of the agent's performance. Higher scores indicate better performance.

#### Future Scope

1. **Deep Q Networks**: While Q-learning with a Q-table is a good starting point, the state space of 2048 is vast. Using neural networks, specifically DQNs, can help generalize over this large state space.
2. **Experience Replay**: Storing and then randomly sampling previous experiences can help stabilize and improve learning.
3. **Exploration Strategies**: More advanced exploration strategies, like epsilon-decreasing policies, can be used to balance exploration and exploitation better.
4. **Transfer Learning**: Once an agent is trained on 2048, its knowledge could potentially be transferred to other similar games or puzzles, reducing the training time for those tasks.

