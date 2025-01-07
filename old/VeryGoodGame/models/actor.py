import pygame
import random

class Actor:
    def __init__(self,WINDOW, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 1
        self.direction = 1
        self.color = (0, 0, 0)
        self.WINDOW = WINDOW
        self.holding = []
        self.grabbing = False
        self.points = 0

        # RL Parameters
        self.actions = ['LEFT', 'RIGHT', 'UP', 'DOWN', 'GRAB']  # Action space
        self.q_table = {}  # State-action mapping for Q-learning
        self.epsilon = 0.1  # Exploration rate
        self.alpha = 0.5  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.visit_count = {}
        self.episode = 0
        self.committed_action = None
        self.commitment_frames = 0
    
    def get_state(self):
        state = (self.x, self.y, bool(self.holding))
        return state

    # Epsilon-greedy policy with decaying epsilon.
    def choose_action(self, state):
        epsilon = max(0.01, self.epsilon * (0.99 ** self.episode))  
        if random.uniform(0, 1) < epsilon:
            return random.choice(self.actions)  
        else:
            return max(self.actions, key=lambda action: self.q_table.get((state, action), 0)) 


    def take_action(self, action):
        if action == 'LEFT' and self.x - self.speed >= 0:
            self.x -= self.speed
        elif action == 'RIGHT' and self.x + self.width + self.speed <= self.WINDOW.get_width():
            self.x += self.speed
        elif action == 'UP' and self.y - self.speed >= 0:
            self.y -= self.speed
        elif action == 'DOWN' and self.y + self.height + self.speed <= self.WINDOW.get_height():
            self.y += self.speed
        elif action == 'GRAB':
            self.grabbing = True
        else:
            self.grabbing = False
            self.holding = []
        self.episode += 1

    def update_q_table(self, state, action, reward, next_state):
        old_value = self.q_table.get((state, action), 0)
        next_max = max([self.q_table.get((next_state, a), 0) for a in self.actions])
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[(state, action)] = new_value

    def movement(self):
        state = self.get_state()

        if self.commitment_frames == 0:
            if self.episode < 100000:
                action = random.choice(self.actions)
            else:
                action = self.choose_action(state)

            self.committed_action = action
            self.commitment_frames = 30  
        else:
            action = self.committed_action

   
        self.take_action(action)
        self.commitment_frames -= 1

        reward = self.calculate_reward()
        next_state = self.get_state()
        self.update_q_table(state, action, reward, next_state)
        

    def calculate_reward(self):
        state = self.get_state()
        self.visit_count[state] = self.visit_count.get(state, 0) + 1

        reward = self.points * 100000
        reward += 100 / (1 + self.visit_count[state])
        reward += len(self.holding) * 10

        return reward



    def draw(self):
        pygame.draw.ellipse(self.WINDOW, self.color, (self.x, self.y, self.width, self.height))

    