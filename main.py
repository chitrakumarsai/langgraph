import random
from langgraph.graph import Graph

# Define the nodes
def generate_random_number(state):
    return {"number": random.randint(1, 10)}

def square_number(state):
    number = state.get("number")
    if number is not None:
        return {"result": number ** 2}
    return {}

# Create the graph
graph = Graph()

# Add nodes
graph.add_node("generate_number", generate_random_number)
graph.add_node("square_number", square_number)

# Define edges
graph.add_edge("generate_number", "square_number")

# Set the entry point
graph.set_entry_point("generate_number")

# Compile the graph
graph = graph.compile()
