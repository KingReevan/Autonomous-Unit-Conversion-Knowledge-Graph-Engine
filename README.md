# Unit Conversion Knowledge Graph Engine  
*A fully automated, LLM-powered system for discovering, validating, and storing unit conversions in a Neo4j knowledge graph.*

---

## 🚀 Overview

This project builds an **autonomous unit-conversion engine** that continuously learns new unit-to-unit relationships using:

- **DSPy** for structured LLM pipelines  
- **OpenAI models** for generating questions & formulas  
- **Pydantic** for strict validation  
- **Neo4j** for graph storage  
- **AsyncIO & multithreading** for high-performance training  
- **Typer CLI** for user interaction  

The engine automatically:

1. Generates natural-language unit-conversion questions  
2. Extracts the pair of units (A → B)  
3. Asks an LLM for the mathematical conversion formula  
4. Stores forward + inverse relations in Neo4j  
5. Repeats the process autonomously for multiple cycles  

This produces a scalable **knowledge graph** of unit conversions.

---

## 🧠 Core Features

### ✅ Automated Training Pipeline
- End-to-end question generation → unit extraction → formula derivation → graph storage  
- Fully asynchronous version available  
- Thread-parallelized DSPy predictions  

### ✅ LLM-Driven Formula Generation
Strict DSPy signatures guarantee:
- full unit names (no abbreviations)  
- strict math syntax (`*`, `/`, `**`)  
- minimal operations  
- target unit on the LHS  

### ✅ Neo4j Knowledge Graph
- Nodes represent units  
- Edges are typed as `CONVERTS_TO`  
- Automatic inverse formula generation  

### ✅ Reliable Validation
- Pydantic validates all extraction & formula outputs  
- Invalid LLM responses are gracefully skipped  

### ✅ Typer-Based CLI
Commands:
python cli.py train <cycles>
python cli.py async-train <cycles>
python cli.py ask
python cli.py shortest-path


---

## 📁 Project Structure

project/
│── async_training.py # Async training pipeline
│── training.py # Synchronous training loop
│── generate_questions.py # DSPy question generator
│── extract.py # DSPy unit extractor
│── engine.py # Formula parsing, inversion
│── neo.py # Neo4j driver + operations
│── mass_edge_storage.py # Async batch graph storage
│── timing.py # @timeit decorator
│── cli.py # Typer CLI
│── README.md
│── requirements.txt


---

## ⚙️ Installation

### 1. Create environment
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Set API keys
Create a .env file:

ini
Copy code
OPENAI_API_KEY=your_api_key
4. Run Neo4j
Make sure Neo4j is running locally or remotely.

🧵 Synchronous Training
Run:

bash
Copy code
python cli.py train 2
This performs:

2 training cycles

10 generated questions per cycle

unit extraction

formula generation

graph storage

⚡ Asynchronous Training
The async version is significantly faster due to:

asyncio.gather for concurrent LLM calls

asyncio.to_thread() for CPU-bound DSPy predictions

async Neo4j writes

Run:

bash
Copy code
python cli.py async-train 4
🧩 How the Async Pipeline Works
1. Async Question Generation
python
Copy code
await genq_async(...)
2. Parallel Unit Extraction
python
Copy code
await asyncio.gather(*unit_tasks)
3. Formula Generation in Threads
python
Copy code
asyncio.to_thread(ask_formula, from_unit, to_unit)
4. Async Neo4j Storage
python
Copy code
await save_all_conversions_async(formulas)
🔍 Querying the Graph
Interactive mode:

bash
Copy code
python cli.py ask
Example:

yaml
Copy code
Ask anything: convert liters to milliliters
Result: liters → milliliters: milliliters = liters * 1000
🏗️ Graph Schema
Nodes
css
Copy code
(:Unit { name: "<full unit name>" })
Relationship
css
Copy code
(a:Unit)-[:CONVERTS_TO { formula: "<equation>" }]->(b:Unit)
Inverse Relations
Automatically computed via formula inversion and stored.

📈 Performance
Async training is 4–10× faster

DSPy unit extraction + formula generation supports multithreading

Neo4j storage runs concurrently

Execution time measured with @timeit

📘 Future Improvements
Caching identical conversions

Normalizing singular/plural unit representations

Adding a web UI to explore the graph

Automatic periodic training cycles

🔑 License
MIT License.
