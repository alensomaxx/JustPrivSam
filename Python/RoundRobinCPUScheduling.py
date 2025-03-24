import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import LinearRegression

# Stage 1: Basic FCFS Scheduler
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    schedule = []
    for pid, arrival, burst in processes:
        start = max(time, arrival)
        end = start + burst
        schedule.append((pid, start, end))
        time = end
    return schedule

# Stage 2: Add SJF and Round Robin
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time then burst time
    time, schedule = 0, []
    while processes:
        available = [p for p in processes if p[1] <= time]
        if available:
            available.sort(key=lambda x: x[2])
            pid, arrival, burst = available.pop(0)
            start, end = time, time + burst
            schedule.append((pid, start, end))
            time = end
            processes.remove((pid, arrival, burst))
        else:
            time += 1
    return schedule

def round_robin_scheduling(processes, quantum=2):
    queue = sorted(processes, key=lambda x: x[1])
    time, schedule = 0, []
    while queue:
        pid, arrival, burst = queue.pop(0)
        start = max(time, arrival)
        execute = min(burst, quantum)
        end = start + execute
        schedule.append((pid, start, end))
        if burst > quantum:
            queue.append((pid, end, burst - quantum))
        time = end
    return schedule

# Stage 3: Add Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time then priority
    time, schedule = 0, []
    while processes:
        available = [p for p in processes if p[1] <= time]
        if available:
            available.sort(key=lambda x: x[3])
            pid, arrival, burst, priority = available.pop(0)
            start, end = time, time + burst
            schedule.append((pid, start, end))
            time = end
            processes.remove((pid, arrival, burst, priority))
        else:
            time += 1
    return schedule

# Stage 4: Basic GUI
def create_gui():
    root = tk.Tk()
    root.title("CPU Scheduling Simulator")
    
    tk.Label(root, text="Process ID").grid(row=0, column=0)
    tk.Label(root, text="Arrival Time").grid(row=0, column=1)
    tk.Label(root, text="Burst Time").grid(row=0, column=2)
    
    process_entries = []
    for i in range(5):
        pid_entry = tk.Entry(root)
        at_entry = tk.Entry(root)
        bt_entry = tk.Entry(root)
        pid_entry.grid(row=i+1, column=0)
        at_entry.grid(row=i+1, column=1)
        bt_entry.grid(row=i+1, column=2)
        process_entries.append((pid_entry, at_entry, bt_entry))
    
    def run_scheduler():
        processes = [(int(p[0].get()), int(p[1].get()), int(p[2].get())) for p in process_entries if p[0].get()]
        schedule = fcfs_scheduling(processes)
        visualize_schedule(schedule)
    
    tk.Button(root, text="Run FCFS", command=run_scheduler).grid(row=6, column=1)
    root.mainloop()

# Stage 5: Visualization with Gantt Chart
def visualize_schedule(schedule):
    fig, ax = plt.subplots()
    for pid, start, end in schedule:
        ax.barh(pid, end-start, left=start)
    plt.xlabel("Time")
    plt.ylabel("Process ID")
    plt.title("Gantt Chart for CPU Scheduling")
    plt.show()

# Stage 6: Machine Learning for Scheduling
def train_ml_model():
    X = np.array([[random.randint(1, 10), random.randint(1, 10)] for _ in range(50)])
    y = np.array([x[0] + x[1] + random.randint(0, 5) for x in X])
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_burst_time(arrival, priority, model):
    return model.predict([[arrival, priority]])[0]

# Stage 7: Final Optimization
def intelligent_scheduling(processes, model):
    for i in range(len(processes)):
        arrival, priority = processes[i][1], processes[i][2]
        predicted_burst = predict_burst_time(arrival, priority, model)
        processes[i] = (processes[i][0], arrival, int(predicted_burst))
    return sjf_scheduling(processes)


print("Starting GUI...")
model = train_ml_model()
create_gui()