import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import LinearRegression
import heapq

# First Come First Serve (FCFS) - Non-Preemptive
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    schedule = []
    for pid, arrival, burst in processes:
        start = max(time, arrival)
        end = start + burst
        schedule.append((pid, start, end))
        time = end
    return schedule

# Shortest Job First (SJF) - Non-Preemptive
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))
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

# Round Robin (Preemptive)
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

# Priority Scheduling (Preemptive)
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3]))
    time, schedule, pq = 0, [], []
    while processes or pq:
        while processes and processes[0][1] <= time:
            heapq.heappush(pq, (processes[0][3], processes.pop(0)))
        if pq:
            _, (pid, arrival, burst, priority) = heapq.heappop(pq)
            start, end = time, time + burst
            schedule.append((pid, start, end))
            time = end
        else:
            time += 1
    return schedule

# GUI

def create_gui():
    root = tk.Tk()
    root.title("CPU Scheduling Simulator")
    
    tk.Label(root, text="Process ID").grid(row=0, column=0)
    tk.Label(root, text="Arrival Time").grid(row=0, column=1)
    tk.Label(root, text="Burst Time").grid(row=0, column=2)
    tk.Label(root, text="Priority").grid(row=0, column=3)
    
    process_entries = []
    for i in range(5):
        pid_entry = tk.Entry(root)
        at_entry = tk.Entry(root)
        bt_entry = tk.Entry(root)
        pr_entry = tk.Entry(root)
        pid_entry.grid(row=i+1, column=0)
        at_entry.grid(row=i+1, column=1)
        bt_entry.grid(row=i+1, column=2)
        pr_entry.grid(row=i+1, column=3)
        process_entries.append((pid_entry, at_entry, bt_entry, pr_entry))
    
    selected_algo = tk.StringVar(root)
    selected_algo.set("FCFS")
    algo_menu = ttk.Combobox(root, textvariable=selected_algo, values=["FCFS", "SJF", "Round Robin", "Priority"])
    algo_menu.grid(row=6, column=1)
    
    def run_scheduler():
        processes = [(int(p[0].get()), int(p[1].get()), int(p[2].get()), int(p[3].get()) if p[3].get() else 0) 
                     for p in process_entries if p[0].get()]
        algo = selected_algo.get()
        
        if algo == "FCFS":
            schedule = fcfs_scheduling(processes)
        elif algo == "SJF":
            schedule = sjf_scheduling(processes)
        elif algo == "Round Robin":
            schedule = round_robin_scheduling(processes)
        elif algo == "Priority":
            schedule = priority_scheduling(processes)
        
        visualize_schedule(schedule)
    
    tk.Button(root, text="Run Scheduler", command=run_scheduler).grid(row=7, column=1)
    root.mainloop()

# Visualization
def visualize_schedule(schedule):
    fig, ax = plt.subplots()
    for pid, start, end in schedule:
        ax.barh(pid, end - start, left=start)
    plt.xlabel("Time")
    plt.ylabel("Process ID")
    plt.title("Gantt Chart for CPU Scheduling")
    plt.show()


create_gui()