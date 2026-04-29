# Web Crawler Search Algorithm Simulator

This project is a Python Tkinter desktop application that visualizes how classic AI search algorithms crawl through a simulated web graph. It demonstrates Breadth-First Search, Depth-First Search, and Depth-Limited Search using a mock collection of connected web pages.

The application uses a terminal-style interface to show the crawler's frontier, visited nodes, and step-by-step traversal log.

## Features

- Visual simulation of web crawling behavior
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Adjustable depth limit for DLS
- Live display of:
  - Current frontier
  - Visited nodes
  - Algorithm progress messages
- Mock web dataset with cycles, deep paths, and multiple routes to a target node

## Project Structure

```text
.
├── algorithms.py    # BFS, DFS, and DLS generator implementations
├── data_store.py    # Mock web graph used by the crawler
├── interface.py     # Tkinter GUI application
├── reserve.txt      # Older/simple mock graph kept as reference data
└── README.md        # Project documentation
```

## How It Works

The mock web is represented as a graph in `data_store.py`. Each URL is a node, and each link is an edge to another node.

Example:

```python
"https://www.cyberspace.com": {
    "title": "Main Frame",
    "links": [
        "https://www.cyberspace.com/network",
        "https://social.meta.com",
        "https://dev.blog.io"
    ]
}
```

The algorithms in `algorithms.py` are written as Python generators. Each algorithm yields its current frontier, visited set, and a status message after each important step. The GUI consumes these generator steps and updates the interface every 700 milliseconds.

## Search Algorithms

### Breadth-First Search (BFS)

BFS explores nodes level by level. It uses a queue, so nodes discovered first are visited first.

Best for finding the shortest path in an unweighted graph.

### Depth-First Search (DFS)

DFS explores as deeply as possible before backtracking. It uses a stack.

Useful for showing path-first exploration behavior.

### Depth-Limited Search (DLS)

DLS is a DFS variation that stops expanding nodes after a selected depth limit.

Useful when the search space is large or potentially infinite.

## Requirements

- Python 3
- Tkinter

Tkinter is included with many Python installations. On some Linux systems, you may need to install it separately:

```bash
sudo apt install python3-tk
```

## Running the Project

From the project directory, run:

```bash
python3 interface.py
```

When the application opens:

1. Set `ROOT_NODE` to:

   ```text
   https://www.cyberspace.com
   ```

2. Choose an algorithm from the `PROTOCOL` dropdown.
3. If using DLS, set the desired `DEPTH_MAX`.
4. Click `EXECUTE`.

## Important Note

The current GUI default root node is `home`, but the active mock web graph in `data_store.py` uses full URL-style node names. To see the full simulation, use:

```text
https://www.cyberspace.com
```

If `home` is used, the crawler will not find links in the current dataset.

## Example Start Nodes

You can try any node from `data_store.py`, such as:

```text
https://www.cyberspace.com
https://social.meta.com
https://dev.blog.io
https://security.defense.gov
https://archive.org/vault
```

## Educational Purpose

This project is useful for learning:

- Graph traversal
- Search algorithms in Artificial Intelligence
- Queue-based vs stack-based exploration
- Cycle prevention using visited sets
- How a crawler can model links between web pages
- Basic GUI programming with Tkinter

## Possible Improvements

- Change the default root node from `home` to `https://www.cyberspace.com`
- Add target-node search and stop when the target is found
- Display page titles from `data_store.py`
- Add a graph visualization panel
- Show traversal order as a numbered list
- Add reset and pause controls
