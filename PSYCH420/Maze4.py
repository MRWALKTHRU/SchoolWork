import random as r
import numpy as np
import matplotlib.pyplot as p
import time


# Initialising Variables
maze = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

goal = (2, 2)
start = (0, 0)
actions = [0, 1, 2, 3]

stored_rewards = []

numstates = maze.shape[0] * maze.shape[1]
numactions = len(actions)

# Initialise Q table, not with zeros because it leads to loops
Qtable = np.random.rand(numstates, numactions) * 0.01

# Walls
restricted = {
    (0, 0): [0, 2], (0, 1): [0, 1], (0, 2): [0, 1, 3],
    (1, 0): [2], (1, 1): [0, 1], (1, 2): [3],
    (2, 0): [1, 2], (2, 1): [0, 1, 3], (2, 2): [1, 2, 3]
}




# State (integer) to index (coordinates) and vice-versa
def statetoindex(row, col):
    return row * maze.shape[1] + col


def indextostate(index):
    return index // maze.shape[1], index % maze.shape[1]


# Reward so that it wants to find the end of the maze and discourages standing still or not finding the end
def reward(state, prev_state):
    row, col = indextostate(state)
    if (row, col) == goal:
        return 10  # Goal reward
    elif state == prev_state:
        return -5
    return -0.1  # Small penalty for each move


# Check if movement is valid
def canmove(state, action):
    row, col = indextostate(state)
    return action not in restricted.get((row, col), [])


# Get the next part of maze we are in after taking an action
def nextstate(state, action):
    row, col = indextostate(state)
    if not canmove(state, action):
        return state

    if action == 0:
        row -= 1  # Up
    elif action == 1:
        row += 1  # Down
    elif action == 2:
        col -= 1  # Left
    elif action == 3:
        col += 1  # Right

    return statetoindex(row, col)

def animate_path(path):
    for step in path:
        grid = [[" . " for _ in range(3)] for _ in range(3)]
        row, col = step
        grid[row][col] = " A "
        grid[goal[0]][goal[1]] = " G "

        print("\n".join("".join(row) for row in grid))
        print("\n")
        time.sleep(0.5)


# Q-learning function
def qlearn(Qtable, epochs=1000, alpha=0.6, gamma=0.9, epsilon=0.1):
    for epoch in range(epochs):
        state = statetoindex(start[0], start[1])  # Start at (0,0)
        total_reward = 0
        steps = 0  # Reset step counter for each episode

        while state != statetoindex(goal[0], goal[1]) and steps < 100:
            steps += 1  # Avoid infinite loops

            # If we get a random number between 0 and 1 that is less than epsilon (0.1), we "explore"
            if r.random() < epsilon:
                action = r.choice(actions)
            else:
                action = np.argmax(Qtable[state, :])  # else choose best action available according to table

            next_state = nextstate(state, action)
            R = reward(next_state, state)
            total_reward = total_reward + R

            # Q-learning update formula
            Qmax = np.max(Qtable[next_state, :])
            Qtable[state, action] += alpha * (R + gamma * Qmax - Qtable[state, action])

            state = next_state
            # stop once at the goal
            if state == statetoindex(goal[0], goal[1]):
                break

        stored_rewards.append(total_reward)


# Test the q-table
def qtest(Qtable):
    state = statetoindex(start[0], start[1])
    path = [indextostate(state)] # Save the path we take so we can print it out and make sure it's right

    for _ in range(10):
        action = np.argmax(Qtable[state, :])
        next_state = nextstate(state, action)

        path.append(indextostate(next_state))
        state = next_state

        if state == statetoindex(goal[0], goal[1]):
            break

    return path


def main():
    print("Starting Q-Learning...")
    qlearn(Qtable)
    print("Learning Complete")
    print(f"Qtable:\n{np.round(Qtable, 0)}")

    optimal = qtest(Qtable)
    print("Optimal Path:\n")
    animate_path(optimal)

    p.plot(stored_rewards)
    p.xlabel("Epoch")
    p.ylabel("Total Reward")
    p.title("Learning over time")
    p.grid(True)
    p.show()

while True:
    main()
    restart = input("Do you want to run the simulation again? (yes/no): ")
    if restart.lower() != "yes":
        break

