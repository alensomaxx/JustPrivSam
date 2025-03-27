import tkinter as tk
from tkinter import ttk
import psutil
import gc
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import logging
import csv
from datetime import datetime

class GarbageCollectionMonitor:
    def __init__(self, master):
        self.master = master
        master.title("Garbage Collection Monitor")
        master.geometry("1200x800")

        # Configure logging
        logging.basicConfig(
            filename='gc_monitor.log', 
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

        # Tracking variables
        self.is_monitoring = False
        self.memory_data = {
            'timestamps': [],
            'memory_usage': [],
            'gc_count': []
        }

        # Create UI components
        self.create_ui()

    def create_ui(self):
        """Create the main user interface"""
        # Main frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Memory Usage Section
        memory_frame = ttk.LabelFrame(main_frame, text="Memory Usage")
        memory_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Memory Usage Labels
        self.total_memory_label = ttk.Label(memory_frame, text="Total Memory: N/A")
        self.total_memory_label.grid(row=0, column=0, sticky=tk.W)

        self.available_memory_label = ttk.Label(memory_frame, text="Available Memory: N/A")
        self.available_memory_label.grid(row=1, column=0, sticky=tk.W)

        # Garbage Collection Section
        gc_frame = ttk.LabelFrame(main_frame, text="Garbage Collection Stats")
        gc_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.gc_count_label = ttk.Label(gc_frame, text="GC Count: 0")
        self.gc_count_label.grid(row=0, column=0, sticky=tk.W)

        self.gc_collected_label = ttk.Label(gc_frame, text="Memory Collected: N/A")
        self.gc_collected_label.grid(row=1, column=0, sticky=tk.W)

        # Control Buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, padx=10, pady=10)

        self.start_button = ttk.Button(control_frame, text="Start Monitoring", command=self.toggle_monitoring)
        self.start_button.grid(row=0, column=0, padx=5)

        self.export_button = ttk.Button(control_frame, text="Export Report", command=self.export_report)
        self.export_button.grid(row=0, column=1, padx=5)

        # Matplotlib Figure for Memory Graph
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().grid(row=3, column=0, padx=10, pady=10)

    def toggle_monitoring(self):
        """Start or stop monitoring"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.start_button.config(text="Stop Monitoring")
            self.monitoring_thread = threading.Thread(target=self.monitor_system, daemon=True)
            self.monitoring_thread.start()
            self.logger.info("Monitoring started")
        else:
            self.is_monitoring = False
            self.start_button.config(text="Start Monitoring")
            self.logger.info("Monitoring stopped")

    def monitor_system(self):
        """Continuously monitor system memory and garbage collection"""
        initial_gc_count = gc.get_count()
        
        while self.is_monitoring:
            try:
                # Memory Usage
                memory = psutil.virtual_memory()
                total_memory = memory.total / (1024 * 1024)  # Convert to MB
                available_memory = memory.available / (1024 * 1024)
                memory_percent = memory.percent

                # Update Memory Labels
                self.total_memory_label.config(text=f"Total Memory: {total_memory:.2f} MB")
                self.available_memory_label.config(text=f"Available Memory: {available_memory:.2f} MB ({memory_percent}%)")

                # Garbage Collection Stats
                gc_count = gc.get_count()
                gc_collected = gc.get_collected()
                
                self.gc_count_label.config(text=f"GC Count: {gc_count[0]}")
                self.gc_collected_label.config(text=f"Memory Collected: {len(gc_collected)} objects")

                # Store data for graphing
                current_time = time.time()
                self.memory_data['timestamps'].append(current_time)
                self.memory_data['memory_usage'].append(memory_percent)
                self.memory_data['gc_count'].append(gc_count[0])

                # Update graph
                self.update_graph()

                # Log important events
                if gc_count[0] > initial_gc_count[0]:
                    self.logger.info(f"Garbage Collection triggered. Objects collected: {len(gc_collected)}")

                time.sleep(1)  # Update every second

            except Exception as e:
                self.logger.error(f"Monitoring error: {e}")
                break

    def update_graph(self):
        """Update matplotlib graph with memory usage data"""
        # Limit to last 50 data points
        timestamps = self.memory_data['timestamps'][-50:]
        memory_usage = self.memory_data['memory_usage'][-50:]

        # Clear previous plot
        self.ax.clear()
        
        # Plot new data
        self.ax.plot(timestamps, memory_usage, label='Memory Usage (%)')
        self.ax.set_title('Memory Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Memory Usage (%)')
        self.ax.legend()

        # Redraw canvas
        self.canvas.draw()

    def export_report(self):
        """Export monitoring data to CSV"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gc_monitor_report_{timestamp}.csv"
            
            with open(filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['Timestamp', 'Memory Usage (%)', 'GC Count'])
                
                for i in range(len(self.memory_data['timestamps'])):
                    csvwriter.writerow([
                        self.memory_data['timestamps'][i],
                        self.memory_data['memory_usage'][i],
                        self.memory_data['gc_count'][i]
                    ])
            
            # Show export success message
            tk.messagebox.showinfo("Export Successful", f"Report exported to {filename}")
            self.logger.info(f"Report exported: {filename}")
        
        except Exception as e:
            tk.messagebox.showerror("Export Failed", str(e))
            self.logger.error(f"Report export failed: {e}")

def main():
    root = tk.Tk()
    app = GarbageCollectionMonitor(root)
    root.mainloop()


main()