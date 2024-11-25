import matplotlib.pyplot as plt
import networkx as nx

# Define the DFD Level 0 graph
dfd_level_0 = nx.DiGraph()

# Add nodes for entities and process
dfd_level_0.add_node("Passengers", shape="ellipse", style="filled", color="#FFC300")
dfd_level_0.add_node("Lift Optimization System", shape="rectangle", style="filled", color="#00BFFF")
dfd_level_0.add_node("Lift System", shape="ellipse", style="filled", color="#FFC300")

# Add edges for data flow
dfd_level_0.add_edges_from([
    ("Passengers", "Lift Optimization System"),
    ("Lift Optimization System", "Lift System")
])

# Define positions for the nodes
pos_level_0 = {
    "Passengers": (-1, 0),
    "Lift Optimization System": (0, 0),
    "Lift System": (1, 0)
}

# Create Level 0 DFD
plt.figure(figsize=(8, 4))
nx.draw_networkx(dfd_level_0, pos=pos_level_0, with_labels=True, node_size=3000,
                 node_color=["#FFC300", "#00BFFF", "#FFC300"], font_size=10, font_color="black")
nx.draw_networkx_edge_labels(dfd_level_0, pos=pos_level_0, edge_labels={
    ("Passengers", "Lift Optimization System"): "Lift Call Requests",
    ("Lift Optimization System", "Lift System"): "Optimized Commands"
}, font_color="green")
plt.title("DFD Level 0: Lift Optimization System", fontsize=12)
plt.axis("off")
plt.show()

# Define the DFD Level 1 graph
dfd_level_1 = nx.DiGraph()

# Add nodes for Level 1 components
dfd_level_1.add_node("Input Validation", shape="ellipse", style="filled", color="#FFA07A")
dfd_level_1.add_node("Passenger Detection", shape="ellipse", style="filled", color="#FFA07A")
dfd_level_1.add_node("Routing Algorithm", shape="ellipse", style="filled", color="#FFA07A")
dfd_level_1.add_node("Command Dispatch", shape="ellipse", style="filled", color="#FFA07A")
dfd_level_1.add_node("Lift Optimization System", shape="rectangle", style="filled", color="#00BFFF")

# Add edges for data flow between components
dfd_level_1.add_edges_from([
    ("Input Validation", "Passenger Detection"),
    ("Passenger Detection", "Routing Algorithm"),
    ("Routing Algorithm", "Command Dispatch"),
    ("Command Dispatch", "Lift Optimization System")
])

# Define positions for the Level 1 nodes
pos_level_1 = {
    "Input Validation": (-2, 0),
    "Passenger Detection": (-1, 0),
    "Routing Algorithm": (0, 0),
    "Command Dispatch": (1, 0),
    "Lift Optimization System": (2, 0)
}

# Create Level 1 DFD
plt.figure(figsize=(10, 5))
nx.draw_networkx(dfd_level_1, pos=pos_level_1, with_labels=True, node_size=3000,
                 node_color=["#FFA07A", "#FFA07A", "#FFA07A", "#FFA07A", "#00BFFF"],
                 font_size=10, font_color="black")
nx.draw_networkx_edge_labels(dfd_level_1, pos=pos_level_1, edge_labels={
    ("Input Validation", "Passenger Detection"): "Validated Requests",
    ("Passenger Detection", "Routing Algorithm"): "Passenger Presence Data",
    ("Routing Algorithm", "Command Dispatch"): "Optimized Route",
    ("Command Dispatch", "Lift Optimization System"): "Lift Commands"
}, font_color="green")
plt.title("DFD Level 1: Lift Optimization System", fontsize=12)
plt.axis("off")
plt.show()
