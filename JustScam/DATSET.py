import pybullet as p
import pybullet_data
import numpy as np
import time
import matplotlib.pyplot as plt

# Connect to PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
plane = p.loadURDF("plane.urdf")

# Parameters
n_robots = 10
w, c1, c2, k = 0.7, 2.0, 2.0, 0.05
max_steps = 200

# Initialize robots, goals, obstacles
robots = [p.loadURDF("sphere2.urdf", [np.random.uniform(0, 10), np.random.uniform(0, 10), 0.5]) for _ in range(n_robots)]
goals = [[np.random.uniform(0, 10), np.random.uniform(0, 10), 0.5] for _ in range(n_robots)]
obstacles = [p.loadURDF("cube.urdf", [5 + np.sin(i*0.1), 5 + np.cos(i*0.1), 0.5], useFixedBase=False) for i in range(5)]

# TDM-PSO variables
positions = np.array([[p.getBasePositionAndOrientation(r)[0][:2] for r in robots]])
velocities = np.zeros((n_robots, 2))
pbest = positions.copy()
gbest = positions[0].copy()
t_pbest = np.zeros(n_robots)
t_gbest = 0
t = 0

# Fitness function
def fitness(pos, goal, obs):
    goal_dist = np.linalg.norm(pos - goal[:2])
    obs_dist = min([np.linalg.norm(pos - p.getBasePositionAndOrientation(o)[0][:2]) for o in obs])
    return goal_dist + (1000 if obs_dist < 1 else 0)

# Simulation loop
for t in range(max_steps):
    # Update obstacle positions (dynamic)
    for i, o in enumerate(obstacles):
        p.resetBasePositionAndOrientation(o, [5 + np.sin(t*0.1 + i), 5 + np.cos(t*0.1 + i), 0.5], [0, 0, 0, 1])

    # TDM-PSO update
    for i in range(n_robots):
        pos = positions[-1][i]
        goal = goals[i]
        fit = fitness(pos, goal, obstacles)

        # Update pbest
        if fit < fitness(pbest[i], goal, obstacles):
            pbest[i] = pos
            t_pbest[i] = t

        # Update gbest
        if fit < fitness(gbest, goals[np.argmin([fitness(gbest, g, obstacles) for g in goals])], obstacles):
            gbest = pos
            t_gbest = t

        # Velocity update with TDM-PSO
        decay_p = np.exp(-k * (t - t_pbest[i]))
        decay_g = np.exp(-k * (t - t_gbest))
        r1, r2 = np.random.rand(2)
        velocities[i] = (w * velocities[i] + 
                         c1 * r1 * (pbest[i] - pos) * decay_p + 
                         c2 * r2 * (gbest - pos) * decay_g)

        # Position update
        new_pos = pos + velocities[i]
        positions = np.append(positions, [[new_pos if j == i else positions[-1][j] for j in range(n_robots)]], axis=0)
        p.resetBasePositionAndOrientation(robots[i], [new_pos[0], new_pos[1], 0.5], [0, 0, 0, 1])

    p.stepSimulation()
    time.sleep(0.01)

# Plot paths (optional 2D visualization)
plt.figure()
for i in range(n_robots):
    plt.plot(positions[:, i, 0], positions[:, i, 1], label=f"Robot {i+1}")
plt.scatter([g[0] for g in goals], [g[1] for g in goals], c='red', marker='x', label="Goals")
plt.legend()
plt.show()