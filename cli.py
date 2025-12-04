import typer
import asyncio
from training import training_loop
from user_query import agent
from async_training import async_training_loop
from shortest_path import run_algorithm

app = typer.Typer()

@app.command()
def train(cycles: int):
    """
    Run the training workflow for a given number of cycles.
    """
    training_loop(cycles)

@app.command()
def async_train(cycles: int):
    """
    Run the asynchronous version of the training workflow for a given number of cycles.
    """
    asyncio.run(async_training_loop(cycles))

@app.command()
def ask():
    """
    Ask Knowledge Graph for Unit Conversions
    """
    query:str = input("Ask anything related to the conversion of units: ")
    print(agent(query))

@app.command()
def shortest_path():
    """
    Multi-hop Algorithm to find shortest path between two nodes
    """
    run_algorithm()

if __name__ == "__main__":
    app()
