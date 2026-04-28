import collections
from data_store import MOCK_WEB

def bfs(start_node):
    """Breadth-First Search: Level-order exploration."""
    visited = []
    frontier = collections.deque([start_node])
    
    while frontier:
        # Yield current state to UI
        yield list(frontier), visited, f"Current Frontier: {list(frontier)}"
        
        current = frontier.popleft()
        
        if current not in visited:
            visited.append(current)
            yield list(frontier), visited, f"Visiting: {current}"
            
            # Get neighbors from data_store
            neighbors = MOCK_WEB.get(current, {}).get("links", [])
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
            
            yield list(frontier), visited, f"Found {len(neighbors)} links on {current}"

def dfs(start_node):
    """Depth-First Search: Goes deep into one path first."""
    visited = []
    frontier = [start_node] # Using a list as a Stack (LIFO)
    
    while frontier:
        yield frontier, visited, f"Current Stack: {frontier}"
        
        current = frontier.pop()
        
        if current not in visited:
            visited.append(current)
            yield frontier, visited, f"Visiting: {current}"
            
            neighbors = MOCK_WEB.get(current, {}).get("links", [])
            # Reverse neighbors to maintain order when popping from stack
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    frontier.append(neighbor)
            
            yield frontier, visited, f"Following deep path from {current}..."

def dls(start_node, limit):
    """Depth-Limited Search: DFS but stops at a specific depth."""
    visited = []
    # Frontier stores (node, depth) tuples
    frontier = [(start_node, 0)]
    
    while frontier:
        yield [node for node, depth in frontier], visited, f"Current Frontier (with depths): {frontier}"
        
        current, depth = frontier.pop()
        
        if current not in visited:
            visited.append(current)
            yield [node for node, depth in frontier], visited, f"Visiting {current} at depth {depth}"
            
            if depth < limit:
                neighbors = MOCK_WEB.get(current, {}).get("links", [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        frontier.append((neighbor, depth + 1))
                yield [node for node, depth in frontier], visited, f"Adding neighbors of {current} (Depth {depth+1})"
            else:
                yield [node for node, depth in frontier], visited, f"Depth limit reached at {current}. Backtracking..."